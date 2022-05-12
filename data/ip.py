import os
from abc import ABC, abstractmethod
import tempfile
import tarfile

delim = "\\"

class AbstractIP(ABC):

    def __init__(self, path, temp):
        self.path = path
        self.ipid = None
        self.temp = temp
        self.files = []
        self.metadata = None

    # @property
    # def path(self):
    #     return self._path
    #
    # @property
    # def temp(self):
    #     return self.temp
    #
    # @property
    # def ipid(self):
    #     return self.ipid
    #
    # @property
    # def metadata(self):
    #     return self.metadata
    #
    # @property
    # def files(self):
    #     return self.files

    def save(self, path):
        pass

    def delete(self):
        pass

    def __unpack__(self):
        tar = tarfile.open(self.__path__)
        # Open tar to read
        # Or unpack to temporary directory?
        # https://docs.python.org/3/library/tarfile.html#examples
        files = tar.getmembers()

        tar.close()

    # @path.setter
    # def path(self, value):
    #     self._path = value
    #
    # @temp.setter
    # def temp(self, value):
    #     self._temp = value
    #
    # @files.setter
    # def files(self, value):
    #     self._files = value
    #
    # @metadata.setter
    # def metadata(self, value):
    #     self._metadata = value
    #
    # @ipid.setter
    # def ipid(self, value):
    #     self._ipid = value


class AIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(path, temp)
        self.parent = None
        self.preservationLevels = None
        self.itemIDs = None
        self.index = None
        self.ieid = None
        self.date = None
        self.initSuccess = False
        self.__parse__()

    def __parse__(self):
        tar = tarfile.open(self.path)
        # Open tar to read
        # Or unpack to temporary directory?
        # https://docs.python.org/3/library/tarfile.html#examples
        files = tar.getmembers()
        for f in files:
            if f.name == "DIPSARCH.xml":
                tar.extractall(path=self.temp.name, members=[f])
                self.metadata = self.temp.name + delim + "DIPSARCH.xml"
                os.rename(self.temp.name+delim+"DIPSARCH.xml", self.temp.name+delim+"123.xml")
                print("DIPSARCH found:")
                self.extractmetadata()
                self.metadata = self.temp.name + delim + str(self.ipid) + ".xml"
                print(self.metadata)
            else:
                self.files.append(f.name)
        tar.close()
        print(self.files)

    def extractmetadata(self):
        self.ieid = 123
        self.date = 123
        self.ipid = 123
        self.initSuccess = False
        pass

    def getie(self):
        return self.ieid

    def isaip(self):
        return self.initSuccess
    
    def __lt__(self, other):
        return self.date < other.date

    def setindex(self, i):
        self.index = i


class DIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(path, temp)
        self.origAIPs = None
        self.itemIDs = None

    def initialize(self):
        pass


class ViewDIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(path, temp)
        self.origAIPs = None
        self.itemIDs = None

    def initialize(self):
        pass
