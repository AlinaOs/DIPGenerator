from abc import ABC, abstractmethod


class AbstractIP(ABC):

    def __init__(self, path, temp):
        self.__path__ = path
        self.__path__ = temp
        self.id = None
        self.metadata = None
        self.files = None
        self.initialize()

    @property
    def name(self):
        return self.id

    @property
    def metadata(self):
        return self.metadata

    @property
    def files(self):
        return self.files

    @abstractmethod
    def initialize(self):
        pass

    def save(self, path):
        pass

    def delete(self):
        pass


class AIP(AbstractIP):

    def __init__(self, path, temp):
        super().__init__(path, temp)
        self.parent = None
        self.child = None
        self.preservationLevels = None
        self.itemIDs = None

    def initialize(self):
        pass


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
