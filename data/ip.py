from abc import ABC, abstractmethod
import tempfile
import tarfile


class AbstractIP(ABC):

    def __init__(self, path, temp):
        pass

    @property
    def path(self):
        return self._path

    @property
    def temp(self):
        return self._temp

    @property
    def ipid(self):
        return self._ipid

    @property
    def metadata(self):
        return self._metadata

    @property
    def files(self):
        return self._files

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

    @files.setter
    def files(self, value):
        self._files = value

    @metadata.setter
    def metadata(self, value):
        self._metadata = value

    @ipid.setter
    def ipid(self, value):
        self._ipid = value


class AIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(path, temp)
        self.parent = None
        self.preservationLevels = None
        self.itemIDs = None
        self.index = None
        self.ieid = None
        self.date = None
        self.ipid = None
        self.initSuccess = None
        self.listfiles()
        self.extractmetadata()

    def listfiles(self):
        tar = tarfile.open(self.__path__)
        # Open tar to read
        # Or unpack to temporary directory?
        # https://docs.python.org/3/library/tarfile.html#examples
        files = tar.getmembers()

        tar.close()

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
