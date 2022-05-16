from datetime import datetime
import os
import re
import sys
from abc import ABC, abstractmethod
import xml.etree.cElementTree as ET
import tarfile
from saxonpy import *

# Todo: Delimiter
delim = "\\"


class AbstractIP(ABC):

    def __init__(self, temp):
        self._ipid = None
        self._temp = temp
        self._files = []
        self._metadata = None
        self._initSuccess = False

    @abstractmethod
    def save(self, path):
        pass

    def getid(self):
        return self._ipid

    def getfiles(self):
        return self._files

    def getmetadata(self):
        return self._metadata


class AIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(temp)
        self._ieinfo = {}
        self._formats = []
        self._itemIDs = []
        self._path = path
        self._parent = None
        self._preslevels = []
        self._index = None
        self._filenames = []
        self._sizes = []
        self._ieid = None
        self._date = None
        self._parse()

    def _parse(self):
        with tarfile.open(self._path) as tar:
            files = tar.getmembers()
            for f in files:
                if f.name == "DIPSARCH.xml":
                    tar.extractall(path=self._temp.name, members=[f])
                    self._metadata = self._temp.name + delim + "DIPSARCH.xml"
                else:
                    self._files.append(f.name)

        self._extractmetadata()
        os.rename(self._metadata, self._temp.name + delim + str(self.ipid) + ".xml")
        self._metadata = self._temp.name + delim + str(self.ipid) + ".xml"

    def _extractmetadata(self):
        dipsarch = ET.parse(self._metadata)
        ns = "{http://dips.bundesarchiv.de/schema}"

        self._parent = dipsarch.find("./" + ns + "AIP/" + ns + "Parent")
        if self._parent is not None:
            self._parent = self._parent.text
        self.ipid = dipsarch.find("./" + ns + "AIP/" + ns + "AIPID").text
        self._ieid = dipsarch.find("./" + ns + "intellectualEntity/" + ns + "IEID").text

        for f in self._files:
            ident = re.split("\.", f)
            ident = " ".join(ident[0:-1])

            # Extract filename and item ID
            item = dipsarch.find(
                "./" + ns + "intellectualEntity//" + ns + "linkingObjectIdentifier[" +
                ns + "linkingObjectIdentifierValue='" + ident + "']/..")
            self._filenames.append(item.find("./" + ns + "title").text)
            self._itemIDs.append(item.find("./" + ns + "IID").text)

            # Extract file format, file size and preservation level
            item = dipsarch.find(
                "./" + ns + "technical/" + ns + "object/" + ns + "objectIdentifier[" + ns + "objectIdentifierValue='" + ident + "']/..")
            self._formats.append(item.find(".//" + ns + "formatName").text)
            self._sizes.append(item.find(".//" + ns + "size").text)
            self._preslevels.append(item.find("./" + ns + "preservationLevel").text)

        # Extract AIP Date (latest event date)
        dates = dipsarch.findall("./" + ns + "technical/" + ns + "event/" + ns + "eventDateTime")
        datestrings = []
        for d in dates:
            datestrings.append(d.text)
        datestrings = sorted(datestrings)
        self._date = datestrings[-1]

        # Extract IE/non-technical information
        self._ieinfo.update({
            "iename": dipsarch.find("./" + ns + "intellectualEntity/" + ns + "title").text,
            "iedesc": dipsarch.find("./" + ns + "intellectualEntity/" + ns + "description").text,
            "ieruntime":
                dipsarch.find("./" + ns + "intellectualEntity/" + ns + "date/" + ns + "dateStart").text[0:10] +
                " - " +
                dipsarch.find("./" + ns + "intellectualEntity/" + ns + "date/" + ns + "dateEnd").text[0:10]
            ,
            "aiptype": dipsarch.find("./" + ns + "AIP/" + ns + "Type").text,
            "ietype": dipsarch.find("./" + ns + "intellectualEntity/" + ns + "type").text
        })

        self._initSuccess = True

    def save(self, path):
        if os.path.exists(path + "\\" + self.ipid + ".tar"):
            return -1

        try:
            with tarfile.open(self._path, "r") as tar:
                for fname in self._files:
                    tar.extractall(path=self._temp.name, members=[tar.getmember(fname)])

            with tarfile.open(path + "\\" + self.ipid + ".tar", "x") as tar:
                for fname in self._files:
                    tar.add(self._temp.name + "\\" + fname, arcname=fname)
                tar.add(self._metadata, arcname="DIPSARCH.xml")

            return 1

        except tarfile.TarError as e:
            return e.__class__.__name__
        except FileNotFoundError as e:
            return "FileNotFoundError"

    def getie(self):
        return self._ieid

    def getfilenames(self):
        return self._filenames

    def getsizes(self):
        return self._sizes

    def getformats(self):
        return self._formats

    def getpreslevels(self):
        return self._preslevels

    def getieinfo(self):
        return self._ieinfo

    def getieid(self):
        return self._ieid

    def getdate(self):
        return self._date

    def getpath(self):
        return self._path

    def getindex(self):
        return self._index

    def isaip(self):
        return self._initSuccess

    def setindex(self, i):
        self._index = i

    def __lt__(self, other):
        return self._date < other.getdate()


class DIP(AbstractIP):

    def __init__(self, req, temp):
        super().__init__(temp)
        self._origAIPs = []
        self._conf = req["pconf"]
        self._ipid = req["isil"] \
             + ".p" + str(self._conf["profileMetadata"]["profileNumber"]) \
             + "-v" + self._conf["profileMetadata"]["profileVersion"] \
             + "." + req["aips"][0].getieid() \
             + "." + datetime.now().strftime("%Y-%m-%d.%Hh-%Mm-%Ss")
        self._filterfiles(req["aips"])
        self._transformmetadata()
        self._initSuccess = True

    def _filterfiles(self, aips):
        for a in aips:
            afiles = a.getfiles()
            for i in range(0, len(afiles)):
                if not afiles[i] in self._files:
                    self._files.append(afiles[i])
                    self._origAIPs.append(a)

    def _transformmetadata(self):  # Todo
        self._metadata = self._origAIPs[0].getmetadata()

    def save(self, path):
        for i in range(0, len(self._files)):
            with tarfile.open(self._origAIPs[i].getpath(), "r") as tar:
                tar.extractall(path=self._temp.name, members=[tar.getmember(self._files[i])])

        with tarfile.open(path + "\\" + "DIP." + self._ipid + ".tar", "x") as tar:
            for fname in self._files:
                tar.add(self._temp.name + "\\" + fname, arcname=fname)
            tar.add(self._metadata, arcname="DIP_Metadata.xml")
            tar.add(self.getxsd(), arcname="DIP-Profile" + str(self.getpno()) + ".xsd")

    def getmetadata(self):
        return self._metadata

    def getpno(self):
        return self._conf["profileMetadata"]["profileNumber"]

    def getxsd(self):
        return self._conf["xsd"]

    def getorigaips(self):
        return self._origAIPs


class ViewDIP(AbstractIP):

    def __init__(self, dip, conf, temp):
        super().__init__(temp)
        self._dip = dip
        self.conf = conf
        self._ipid = dip.getid() + ".vdip-v" + "dev"
        self._files = dip.getfiles()
        self._origAIPs = dip.getorigaips()
        self._transformmetadata()

    def _transformmetadata(self):
        self._metadata = self._dip.getmetadata()

    def save(self, path):
        for i in range(0, len(self._files)):
            if not os.path.exists(self._temp.name + "\\" + self._files[i]):
                with tarfile.open(self._origAIPs[i].getpath(), "r") as tar:
                    tar.extractall(path=self._temp.name, members=[tar.getmember(self._files[i])])

        with tarfile.open(path + "\\" + "ViewDIP." + self._ipid + ".tar", "x") as tar:
            for fname in self._files:
                tar.add(self._temp.name + "\\" + fname, arcname=fname)
            tar.add(self._dip.getmetadata(), arcname="DIP_Metadata.xml")
            tar.add(self._metadata, arcname="ViewDIP_Metadata.xml")
            # tar.add(self.getxsd(), arcname="ViewDIP.xsd")
            tar.add(self._dip.getxsd(), arcname="DIP-Profile" + str(self._dip.getpno()) + ".xsd")

    def getxsd(self):  # Todo
        return ""
