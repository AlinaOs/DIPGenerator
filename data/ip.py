import os
import re
from abc import ABC, abstractmethod
import xml.etree.cElementTree as ET
import tarfile

delim = "\\"


class AbstractIP(ABC):

    def __init__(self, path, temp):
        self.path = path
        self.ipid = None
        self.temp = temp
        self.files = []
        self.formats = []
        self.metadata = None
        self.ieinfo = {}

    @abstractmethod
    def save(self, path):
        pass


class AIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(path, temp)
        self.parent = None
        self.preservationLevels = []
        self.itemIDs = []
        self.index = None
        self.filenames = []
        self.sizes = []
        self.ieid = None
        self.date = None
        self.initSuccess = False
        self.__parse__()

    def __parse__(self):
        with tarfile.open(self.path) as tar:
            files = tar.getmembers()
            for f in files:
                if f.name == "DIPSARCH.xml":
                    tar.extractall(path=self.temp.name, members=[f])
                    self.metadata = self.temp.name + delim + "DIPSARCH.xml"
                else:
                    self.files.append(f.name)

        self.extractmetadata()
        os.rename(self.metadata, self.temp.name + delim + str(self.ipid)+".xml")
        self.metadata = self.temp.name + delim + str(self.ipid) + ".xml"

    def extractmetadata(self):
        dipsarch = ET.parse(self.metadata)
        root = dipsarch.getroot()
        ns = "{http://dips.bundesarchiv.de/schema}"

        self.parent = dipsarch.find("./" + ns + "AIP/" + ns + "Parent")
        if self.parent is not None:
            self.parent = self.parent.text
        self.ipid = dipsarch.find("./" + ns + "AIP/" + ns + "AIPID").text
        self.ieid = dipsarch.find("./" + ns + "intellectualEntity/" + ns + "IEID").text

        for f in self.files:
            ident = re.split("\.", f)
            ident = " ".join(ident[0:-1])

            # Extract filename and item ID
            item = dipsarch.find(
                "./" + ns + "intellectualEntity//" + ns + "linkingObjectIdentifier[" +
                ns+"linkingObjectIdentifierValue='" + ident + "']/..")
            self.filenames.append(item.find("./" + ns + "title").text)
            self.itemIDs.append(item.find("./" + ns + "IID").text)

            # Extract file format, file size and preservation level
            item = dipsarch.find(
                "./" + ns + "technical/" + ns + "object/" + ns + "objectIdentifier[" + ns + "objectIdentifierValue='"+ident+"']/..")
            self.formats.append(item.find(".//" + ns + "formatName").text)
            self.sizes.append(item.find(".//" + ns + "size").text)
            self.preservationLevels.append(item.find("./" + ns + "preservationLevel").text)

        # Extract AIP Date (latest event date)
        dates = dipsarch.findall("./" + ns + "technical/" + ns + "event/" + ns + "eventDateTime")
        datestrings = []
        for d in dates:
            datestrings.append(d.text)
        datestrings = sorted(datestrings)
        self.date = datestrings[-1]

        # Extract IE/non-technical information
        self.ieinfo.update({
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

        self.initSuccess = True

    def getie(self):
        return self.ieid

    def isaip(self):
        return self.initSuccess
    
    def __lt__(self, other):
        return self.date < other.date

    def setindex(self, i):
        self.index = i

    def save(self, path):
        with tarfile.open(self.path, "r") as tar:
            for fname in self.files:
                tar.extractall(path=self.temp.name, members=[tar.getmember(fname)])

        with tarfile.open(path + "\\" + self.ipid + ".tar", "x") as tar:
            for fname in self.files:
                tar.add(self.temp.name + "\\" + fname, arcname=fname)
            tar.add(self.metadata, arcname="DIPSARCH.xml")


class DIP(AbstractIP):

    def __init__(self, path, temp, xsd, n):
        super().__init__(path, temp)
        self.origAIPs = None
        self.itemIDs = None
        self.xsd = xsd
        self.n = n

    def initialize(self):
        pass

    def save(self, path):  # Todo
        with tarfile.open(self.path, "r") as tar:
            for fname in self.files:
                tar.extractall(path=self.temp.name, members=[tar.getmember(fname)])

        with tarfile.open(path + "\\" + self.ipid + ".tar", "x") as tar:
            for fname in self.files:
                tar.add(self.temp.name + "\\" + fname, arcname=fname)
            tar.add(self.metadata, arcname="DIP_Metadata.xml")
            tar.add(self.xsd, arcname="DIP-Profile"+self.n+".xsd")


class ViewDIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(path, temp)
        self.origAIPs = None
        self.itemIDs = None

    def initialize(self):
        pass

    def save(self, path):
        pass
