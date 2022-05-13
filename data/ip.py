import os
import re
import sys
from abc import ABC, abstractmethod
import xml.etree.cElementTree as ET
import tarfile

# Todo: Delimiter
delim = "\\"


class AbstractIP(ABC):

    def __init__(self, temp):
        self._ipid = None
        self._temp = temp
        self._files = []
        self._metadata = None
        self._itemIDs = []
        self._initSuccess = False

    @abstractmethod
    def save(self, path):
        pass


class AIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(temp)
        self._ieinfo = {}
        self._formats = []
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
                    self.metadata = self._temp.name + delim + "DIPSARCH.xml"
                else:
                    self._files.append(f.name)

        self._extractmetadata()
        os.rename(self.metadata, self._temp.name + delim + str(self.ipid) + ".xml")
        self.metadata = self._temp.name + delim + str(self.ipid) + ".xml"

    def _extractmetadata(self):
        dipsarch = ET.parse(self.metadata)
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
                ns+"linkingObjectIdentifierValue='" + ident + "']/..")
            self._filenames.append(item.find("./" + ns + "title").text)
            self._itemIDs.append(item.find("./" + ns + "IID").text)

            # Extract file format, file size and preservation level
            item = dipsarch.find(
                "./" + ns + "technical/" + ns + "object/" + ns + "objectIdentifier[" + ns + "objectIdentifierValue='"+ident+"']/..")
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
                tar.add(self.metadata, arcname="DIPSARCH.xml")

            return 1

        except tarfile.TarError as e:
            return e.__class__.__name__
        except FileNotFoundError as e:
            return "FileNotFoundError"

    def getie(self):
        return self._ieid

    def getid(self):
        return self._ipid

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

    def getdate(self):
        return self._date

    def getindex(self):
        return self._index

    def isaip(self):
        return self._initSuccess

    def setindex(self, i):
        self._index = i

    def __lt__(self, other):
        return self._date < other._date


class DIP(AbstractIP):

    def __init__(self, path, temp, xsd, n):
        super().__init__(path, temp)
        self._origAIPs = None
        self._xsd = xsd
        self._n = n

    def save(self, path):  # Todo
        with tarfile.open(self.path, "r") as tar:
            for fname in self._files:
                tar.extractall(path=self._temp.name, members=[tar.getmember(fname)])

        with tarfile.open(path + "\\" + self._ipid + ".tar", "x") as tar:
            for fname in self._files:
                tar.add(self._temp.name + "\\" + fname, arcname=fname)
            tar.add(self._metadata, arcname="DIP_Metadata.xml")
            tar.add(self._xsd, arcname="DIP-Profile" + self._n + ".xsd")


class ViewDIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(path, temp)
        self._origAIPs = None

    def save(self, path):
        pass
