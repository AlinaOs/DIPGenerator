import json
import tempfile
from datetime import datetime
import os
import shutil
import re
from abc import ABC, abstractmethod
import xml.etree.cElementTree as ET
import tarfile
from saxonpy import PySaxonProcessor

# Todo: Delimiter
delim = "\\"


class AbstractIP(ABC):

    def __init__(self, temp):
        self._ipid = None
        self._temp = temp
        self._metadata = None
        self._files = []
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

        self._path = path
        self._index = None
        self._parent = None
        self._date = None

        self._filenames = []
        self._formats = []
        self._sizes = []
        self._preslevels = []
        self._itemIDs = []

        self._ieid = None
        self._ieinfo = {}

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
                "./" + ns + "technical/" + ns + "object/" + ns
                + "objectIdentifier[" + ns + "objectIdentifierValue='" + ident + "']/..")
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

    def save(self, path): # Todo: ErrorHandling and SuccessHandling for DIP and ViewDIP
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

    def saveXSD(self, path, xsd):
        shutil.copy2(xsd, path)

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

        self._conf = req["pconf"]
        self._date = datetime.now().strftime("%Y-%m-%d.%Hh-%Mm-%Ss")
        self._ipid = self._conf["issuedBy"] \
                     + ".p" + str(self._conf["profileMetadata"]["profileNumber"]) \
                     + "-v" + self._conf["profileMetadata"]["profileVersion"] \
                     + "." + req["aips"][0].getieid() \
                     + "." + self._date
        self._origAIPs = []
        self._aips = req["aips"]

        self._filterfiles(self._aips)
        self._transformmetadata()
        self._initSuccess = True

    def _filterfiles(self, aips):
        for a in aips:
            afiles = a.getfiles()
            for i in range(0, len(afiles)):
                if not afiles[i] in self._files:
                    self._files.append(afiles[i])
                    self._origAIPs.append(a)

    def _transformmetadata(self):  # Todo: Error handling
        # Create new tempfolder and copy xsl to it, create dummy xml
        temp = tempfile.TemporaryDirectory()
        shutil.copy2(self._conf["xsl"], temp.name + "/xsl.xsl")
        with open(temp.name + "/dummy.xml", "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><dummy></dummy>')
            pass

        # Create config json in folder
        vars_ = {
            "id": self._ipid,
            "profileNumber": self.getpno(),
            "profileDescription": self._conf["profileMetadata"]["profileDescription"],
            "profileVersion": self._conf["profileMetadata"]["profileVersion"],
            "issuedBy": self._conf["issuedBy"],
            "generatorName": self._conf["generatorName"],
            "generatorVersion": self._conf["generatorVersion"],
            "generationDate": self._date,
            "type": "UNIVERSAL",
            "schema": "DIP-P"+str(self.getpno())+".xsd"
        }
        with open(temp.name + "/vars.json", "w") as jf:
            json.dump(vars_, jf)

        # Copy aip metadata to shared folder (while renaming according to index)
        aipdir = temp.name + "/aips/"
        os.mkdir(aipdir)
        for a in self._aips:
            aipname = ""
            for j in range(0, 4-len(str(a.getindex()))):
                aipname += "0"
            aipname += str(a.getindex())
            shutil.copy2(a.getmetadata(), aipdir + aipname + ".xml")

        self._metadata = self._temp.name + "\\" + self._ipid + ".xml"

        # Start transformation
        with PySaxonProcessor(license=False) as proc:
            proc.set_cwd(os.getcwd())
            xsltproc = proc.new_xslt30_processor()
            xsltproc.transform_to_file(
                source_file=temp.name + "/dummy.xml",
                output_file=self._metadata,
                stylesheet_file=temp.name + "/xsl.xsl")
            print(xsltproc.get_error_message(0))

        # Delete tempdir
        # temp.cleanup()

    def save(self, path):
        for i in range(0, len(self._files)):
            with tarfile.open(self._origAIPs[i].getpath(), "r") as tar:
                tar.extractall(path=self._temp.name, members=[tar.getmember(self._files[i])])

        with tarfile.open(path + "\\" + "DIP." + self._ipid + ".tar", "x") as tar:
            for fname in self._files:
                tar.add(self._temp.name + "\\" + fname, arcname=fname)
            tar.add(self._metadata, arcname="DIP-Metadata.xml")
            tar.add(self.getxsd(), arcname="DIP-P" + str(self.getpno()) + ".xsd")

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

        self._ipid = dip.getid() + ".vdip-v" + "dev"
        self._dip = dip
        self.conf = conf
        self._files = dip.getfiles()
        self._origAIPs = dip.getorigaips()

        self._transformmetadata()

    def _transformmetadata(self):  # Todo: Implement transformation with saxon and error handling
        self._metadata = self._dip.getmetadata()

    def save(self, path):
        for i in range(0, len(self._files)):
            if not os.path.exists(self._temp.name + "\\" + self._files[i]):
                with tarfile.open(self._origAIPs[i].getpath(), "r") as tar:
                    tar.extractall(path=self._temp.name, members=[tar.getmember(self._files[i])])

        with tarfile.open(path + "\\" + "VDIP." + self._ipid + ".tar", "x") as tar:
            for fname in self._files:
                tar.add(self._temp.name + "\\" + fname, arcname=fname)
            tar.add(self._dip.getmetadata(), arcname="DIP_Metadata.xml")
            tar.add(self._metadata, arcname="ViewDIP_Metadata.xml")
            # tar.add(self.getxsd(), arcname="ViewDIP.xsd")
            tar.add(self._dip.getxsd(), arcname="DIP-Profile" + str(self._dip.getpno()) + ".xsd")

    def getxsd(self):  # Todo: Implement after writing ViewDIP Config
        return ""
