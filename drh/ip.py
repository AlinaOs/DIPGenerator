import os
import shutil
import json
import tempfile
import tarfile
import traceback
import xml.etree.cElementTree as ET
from lxml import etree
from datetime import datetime
from abc import ABC, abstractmethod

from saxonpy import PyXslt30Processor


class AbstractIP(ABC):
    """Abstract base class for all Information Package (IP) objects."""

    _ipid: str
    _temp: tempfile.TemporaryDirectory
    _metadata: str
    _files: list[str]
    _initsuccess: bool
    _tb: str

    def __init__(self, temp: tempfile.TemporaryDirectory):
        """Initialize and return an AbstractIP object.

        :param temp: Path to a temporary directory, that the IP can use during parsing/saving.
        :type temp: str
        """
        self._ipid = None
        self._temp = temp
        self._metadata = None
        self._files = []
        self._initsuccess = True
        self._tb = ""

    @abstractmethod
    def save(self, path):
        """Save the IP as .tar file to the specified path."""
        pass

    def getid(self) -> str:
        """Return the ID of the IP."""
        return self._ipid

    def getfiles(self) -> list[str]:
        """Return the files of the IP as list of path strings."""
        return self._files

    def getmetadata(self) -> str:
        """Return the path to the metadata .xml as string"""
        return self._metadata

    def initsuccess(self) -> bool:
        """Return, whether the initialization was successfull (True) or not (False)."""
        return self._initsuccess

    def gettb(self) -> str:
        """Return the current traceback of parsing- or saving errors in this IP."""
        return self._tb


class AIP(AbstractIP):
    """Object representation of an Archival Information Package

    Contains the following metadata about the object, taken from its metadata .xml:
        * self._ipid: The ID of the AIP, as given in its metadata .xml.
        * self._parent: The AIP ID of the AIP, from whom the AIP object was derived.
        * self._date: The date, on which the AIP was last modified (= the date of the latest event).
        * self._files: The paths to all files contained in the AIP
        * self._filenames: The original names (incl. format suffix) of all files contained in the AIP.
        * self._formats: The formats of all files contained in the AIP.
        * self._sizes: The sizes (in kb) of all files contained in the AIP.
        * self._preslevs: The preservation levels of all files contained in the AIP.
        * self._itemIDs: The IDs of all items contained in the AIP.
        * self._ieinfo: A dictionary with information about the AIP's Intellectual Entity with the following keys:

            * "title": The IE's title.
            * "contains": The IE's description.
            * "runtime": The IE's runtime (formatted like "YYYY-MM-DD - YYYY-MM-DD").
            * "aiptype": The AIP's type (e.g., file collection or e-file).
            * "type": The IE's type (e.g. "Sachakte").
    """

    _path: str
    _xsd: str
    _index: int
    _parent: str
    _date: str
    _filenames: list[str]
    _formats: list[str]
    _sizes: list[int]
    _preslevels: list[int]
    _itemIDs: list[str]
    _ieid: str
    _ieinfo: dict

    def __init__(self, path: str, xsd: str, temp: tempfile.TemporaryDirectory):
        """Initialize and return an AIP object.

        :param path: Path to the .tar file that contains the AIP
        :param xsd: Path to the .xsd file, that describes the schema of the AIP metadata .xml file.
        :param temp: Path to a temporary directory, that the IP can use during parsing/saving.
        :type path: str
        :type xsd: str
        :type temp: str
        """
        super().__init__(temp)

        self._path = path
        self._xsd = xsd
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
        """Read the AIP .tar file and parse it as an AIP object.

        The function uses the _path property of the object to find the original
        .tar file, unpacks it (with tarfile) and reads its metadata .xml (with etree).
        If the parsing is successful, the objects _initsuccess is set to True.
        Otherwise, it is set to False and the traceback of any occurring error is
        saved in the objects _traceback property.
        """

        try:
            with tarfile.open(self._path) as tar:
                files = tar.getmembers()
                for f in files:
                    if f.name == "DIPSARCH.xml":
                        tar.extractall(path=self._temp.name, members=[f])
                        self._metadata = os.path.join(self._temp.name, "DIPSARCH.xml")
                    else:
                        self._files.append(f.name)
            if not self._metadata:
                self._tb = "No metadata file (DIPSARCH.xml) found!"
                self._initsuccess = False
                return

            if not self._validateAIP():
                self._initsuccess = False
                return

            self._extractmetadata()
            os.rename(self._metadata, os.path.join(self._temp.name, str(self.ipid) + ".xml"))
            self._metadata = os.path.join(self._temp.name, str(self.ipid) + ".xml")
        except Exception as e:
            print("".join(traceback.format_exception(e, limit=10)))
            self._tb += "".join(traceback.format_exception(e, limit=10))
            self._initsuccess = False

    def _validateAIP(self):
        """Check, whether the AIP's metadata .xml represents a valid AIP XML file
        according to the schema definition file located at the path stored in
        the _xsd property.

        :return: True, if the validation is successful. Otherwise, None.
        """
        # Note: This method doesn't use the SaxonC processor, because the free
        # SaxonC Home Edition (HE) doesn't support xsd validation.
        xmlschema_doc = etree.parse(self._xsd)
        xmlschema = etree.XMLSchema(xmlschema_doc)

        xml_doc = etree.parse(self._metadata)
        if not xmlschema.validate(xml_doc):
            self._tb += "AIP DIPSARCH.xml is invalid!"
            return False

        ns = "{http://dips.bundesarchiv.de/schema}"
        dipsarch = ET.parse(self._metadata)
        metafiles = dipsarch.findall(
                "./" + ns + "intellectualEntity//" + ns + "linkingObjectIdentifier/" +
                ns + "linkingObjectIdentifierValue")
        for m in metafiles:
            if not any(os.path.splitext(f)[0] == m.text for f in self._files):
                self._tb += "AIP is incomplete! Object " + m.text +\
                            " is mentioned in DIPSARCH.xml but not present as file."
                return False

        return True

    def _extractmetadata(self):
        """Extract relevant metadata from the AIP's metadata .xml.

        The function extracts the information needed during any DIP generation (with etree)
        and saves the data as object properties (see class documentation for a list of
        the metadata stored).
        """
        # Note: This method doesn't use the SaxonC processor, because the free
        # SaxonC Home Edition (HE) doesn't support namespace declaration and can
        # therefore not be used to parse the namespaced DIPSARCH.xml
        ns = "{http://dips.bundesarchiv.de/schema}"
        dipsarch = ET.parse(self._metadata)

        parent = dipsarch.find("./" + ns + "AIP/" + ns + "Parent")
        if parent is not None:
            self._parent = parent.text
        self.ipid = dipsarch.find("./" + ns + "AIP/" + ns + "AIPID").text
        self._ieid = dipsarch.find("./" + ns + "intellectualEntity/" + ns + "IEID").text

        for f in self._files:
            ident = os.path.splitext(f)[0]

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
            "title": dipsarch.find("./" + ns + "intellectualEntity/" + ns + "title").text,
            "contains": dipsarch.find("./" + ns + "intellectualEntity/" + ns + "description").text,
            "runtime":
                dipsarch.find("./" + ns + "intellectualEntity/" + ns + "date/" + ns + "dateStart").text[0:10] +
                " - " +
                dipsarch.find("./" + ns + "intellectualEntity/" + ns + "date/" + ns + "dateEnd").text[0:10]
            ,
            "aiptype": dipsarch.find("./" + ns + "AIP/" + ns + "Type").text,
            "type": dipsarch.find("./" + ns + "intellectualEntity/" + ns + "type").text
        })

    def save(self, path: str) -> str | None:
        """Save the AIP to the given path as .tar file.

        :return: None, if saving was successful. A string with the error traceback, if it wasn't.
        """
        try:
            with tarfile.open(self._path, "r") as tar:
                for fname in self._files:
                    tar.extractall(path=self._temp.name, members=[tar.getmember(fname)])

            with tarfile.open(os.path.join(path, self.ipid + ".tar"), "x") as tar:
                for fname in self._files:
                    tar.add(os.path.join(self._temp.name, fname), arcname=fname)
                tar.add(self._metadata, arcname="DIPSARCH.xml")

        except Exception as e:
            return "".join(traceback.format_exception(e, limit=10))

    def savexsd(self, path: str) -> str | None:
        """Save the AIP's xsd to the given path.

        :return: None, if saving was successful. A string with the error traceback, if it wasn't.
        """
        try:
            shutil.copy2(self._xsd, path)
        except Exception as e:
            return "".join(traceback.format_exception(e, limit=10))

    def getfilenames(self) -> list[str]:
        """Return the filenames of the files contained in the AIP as list of strings."""
        return self._filenames

    def getsizes(self) -> list[int]:
        """Return the sizes (in kb) of the files contained in the AIP as list of integers."""
        return self._sizes

    def getformats(self) -> list[str]:
        """Return the format of the files contained in the AIP as list of strings."""
        return self._formats

    def getpreslevels(self)-> list[int]:
        """Return the preservation levels of the files contained in the AIP as list of integers."""
        return self._preslevels

    def getieinfo(self) -> dict:
        """Return informations about the AIP's Intellectual Entity as dictionary.

        The dictionary contains the following keys:
            * "title": The IE's title.
            * "contains": The IE's description.
            * "runtime": The IE's runtime (formatted like "YYYY-MM-DD - YYYY-MM-DD").
            * "aiptype": The AIP's type (e.g., file collection or e-file).
            * "type": The IE's type (e.g. "Sachakte").
        """
        return self._ieinfo

    def getieid(self) -> str:
        """Return the ID of the AIP's Intellectual Entity as string."""
        return self._ieid

    def getdate(self) -> str:
        """Return the creation date of the AIP as string."""
        return self._date

    def getpath(self) -> str:
        """Return the path of the AIP's .tar file as string."""
        return self._path

    def getindex(self) -> int:
        """Return the index of the AIP as int or None.

        The index is calculated externally and indicates the ordering
        of AIPs belonging to the same Intellectual Entity. The earlier their
        creation date ist, the lower will their index be. Indexes start at 0.
        """
        return self._index

    def getparent(self) -> str:
        """Return the ID of the AIP's parent as string."""
        return self._parent

    def setindex(self, i: int):
        """Set the index of the AIP.

        :param i: The AIP's index.
        """
        self._index = i

    def __lt__(self, other):
        return self._date < other.getdate()


class DIP(AbstractIP):
    """Object representation of a Dissemination Information Package

    Contains the following metadata about the object:
        * self._ipid: The generated ID of the DIP.
        * self._date: The datetime of the DIP's creation.
        * self._aips: The AIP objects, that are contained in the DIP.
        * self._files: The paths to all files contained in the DIP.
        * self._origAIPs: The AIP('s), each file is contained in.
    """

    _conf: dict
    _date: str
    _origAIPs: list[list[AIP]]
    _aips = list[AIP]
    _xsltproc: PyXslt30Processor

    def __init__(self, req: dict, temp: tempfile.TemporaryDirectory, xsltproc: PyXslt30Processor):
        """Initialize and return a DIP object.

        The req dictionary must have the following keys:
            * "aips": A list of all the AIP objects, that shall be contained in the DIP.
            * "pconf": A dictionary with the profile specific metadata, containing the following keys:

                * "xsl": Path to the .xsl stylesheet that shall be used for the creation of the DIP's metadata .xml.
                * "xsd": Path to the .xsd schema definition, that defines the DIP's metadata .xml.
                * "generatorName": Name of the generation algorithm used to generate the DIP.
                * "generatorVersion": Version of the generation algorithm used to generate the DIP.
                * "issuedBy": Identifier of the institution that issues the DIP.
            * "vzePath": A path to an .xml file containing information about the VZE, or None.
        :param req: The request settings and user choices as dictionary.
        :param temp: Path to a temporary directory, that the IP can use during parsing/saving.
        :param xsltproc: The Saxon XSLT Processor for the transformation of the metadata .xml file.
        :type req: dict
        :type temp: str
        :type xsltproc: PyXslt30Processor
        """

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

        self._xsltproc = xsltproc
        self._filterfiles(self._aips)
        self._transformmetadata()
        self._initsuccess = True

    def _filterfiles(self, aips):
        for a in aips:
            afiles = a.getfiles()
            for i in range(0, len(afiles)):
                if not afiles[i] in self._files:
                    self._files.append(afiles[i])
                    self._origAIPs.append(a)

    def _transformmetadata(self):
        try:
            # Create new tempfolder and copy xsl to it, create dummy xml
            temp = tempfile.TemporaryDirectory()
            shutil.copy2(self._conf["xsl"], os.path.join(temp.name, "xsl.xsl"))
            with open(os.path.join(temp.name, "dummy.xml"), "w") as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><dummy></dummy>')

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
                "schema": "DIP-P" + str(self.getpno()) + ".xsd"
            }
            with open(os.path.join(temp.name, "vars.json"), "w") as jf:
                json.dump(vars_, jf)

            # Copy aip metadata to shared folder (while renaming according to index)
            aipdir = os.path.join(temp.name, "aips")
            os.mkdir(aipdir)
            for a in self._aips:
                aipname = ""
                for j in range(0, 4-len(str(a.getindex()))):
                    aipname += "0"
                aipname += str(a.getindex())
                shutil.copy2(a.getmetadata(), os.path.join(aipdir, aipname + ".xml"))

            self._metadata = os.path.join(self._temp.name, self._ipid + ".xml")

            # Start transformation
            self._xsltproc.transform_to_file(
                source_file=os.path.join(temp.name, "dummy.xml"),
                output_file=self._metadata,
                stylesheet_file=os.path.join(temp.name, "xsl.xsl"))

        except Exception as e:
            self._tb += "".join(traceback.format_exception(e, limit=10))
            self._initsuccess = False

    def save(self, path) -> None | str:
        """Save the DIP to the given path as .tar file.

        :return: None, if saving was successful. A string with the error traceback, if it wasn't.
        """
        try:
            for i in range(0, len(self._files)):
                with tarfile.open(self._origAIPs[i].getpath(), "r") as tar:
                    tar.extractall(path=self._temp.name, members=[tar.getmember(self._files[i])])

            with tarfile.open(os.path.join(path, "DIP." + self._ipid + ".tar"), "x") as tar:
                for fname in self._files:
                    tar.add(os.path.join(self._temp.name, fname), arcname=fname)
                tar.add(self._metadata, arcname="DIP-Metadata.xml")
                tar.add(self.getxsd(), arcname="DIP-P" + str(self.getpno()) + ".xsd")

        except Exception as e:
            return "".join(traceback.format_exception(e, limit=10))

    def getmetadata(self) -> str:
        """Return the path to the DIP's metadata .xml as string."""
        return self._metadata

    def getpno(self) -> int:
        """Return the index number of the DIP's profile as int."""
        return self._conf["profileMetadata"]["profileNumber"]

    def getxsd(self):
        """Return the path to the DIP's .xsd schema as string."""
        return self._conf["xsd"]

    def getorigaips(self) -> list[list[AIP]]:
        """Return the original AIPs of the files contained in the DIP as list of lists of AIPobjects."""
        return self._origAIPs


class ViewDIP(AbstractIP):
    """Object representation of a viewer specific Dissemination Information Package

    Contains the following metadata about the object:
        * self._ipid: The generated ID of the ViewDIP.
        * self._date: The datetime of the ViewDIP's creation.
        * self._dip: The DIP object, that the ViewDIP object is derived from.
        * self._files: The paths to all files contained in the ViewDIP.
        * self._origAIPs: The AIP('s), each file is contained in.
    """

    def __init__(self, dip, conf, temp: tempfile.TemporaryDirectory, xsltproc):
        """Initialize and return a ViewDIP object.

        :param dip: The DIP object, from which the ViewDIP will be derived.
        :param conf: The ViewDIP config.
        :param temp: Path to a temporary directory, that the IP can use during parsing/saving.
        :param xsltproc: The Saxon XSLT Processor for the transformation of the metadata .xml file.
        :type dip: DIP
        :type conf: dict
        :type temp: str
        :type xsltproc: PyXslt30Processor
        """
        super().__init__(temp)

        self._ipid = dip.getid() + ".vdip-v" + "dev"
        self._dip = dip
        self._conf = conf
        self._date = None
        self._files = dip.getfiles()
        self._origAIPs = dip.getorigaips()

        self._xsltproc = xsltproc
        self._transformmetadata()

    def _transformmetadata(self):  # Todo: Implement transformation with saxon
        try:
            self._metadata = self._dip.getmetadata()
        except Exception as e:
            self._tb += "".join(traceback.format_exception(e, limit=10))
            self._initsuccess = False

    def save(self, path):
        """Save the ViewDIP to the given path as .tar file.

        :return: None, if saving was successful. A string with the error traceback, if it wasn't.
        """
        try:
            for i in range(0, len(self._files)):
                if not os.path.exists(os.path.join(self._temp.name, self._files[i])):
                    with tarfile.open(self._origAIPs[i].getpath(), "r") as tar:
                        tar.extractall(path=self._temp.name, members=[tar.getmember(self._files[i])])

            with tarfile.open(os.path.join(path, "VDIP." + self._ipid + ".tar"), "x") as tar:
                for fname in self._files:
                    tar.add(self._temp.name + "\\" + fname, arcname=fname)
                tar.add(self._dip.getmetadata(), arcname="DIP_Metadata.xml")
                tar.add(self._metadata, arcname="ViewDIP_Metadata.xml")
                # tar.add(self.getxsd(), arcname="ViewDIP.xsd")
                tar.add(self._dip.getxsd(), arcname="DIP-Profile" + str(self._dip.getpno()) + ".xsd")

        except Exception as e:
            return "".join(traceback.format_exception(e, limit=10))

    def getxsd(self):  # Todo: Implement after writing ViewDIP Config
        return ""
