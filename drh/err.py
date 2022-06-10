class DrhError:
    def __init__(self, detail: str, fatal: bool = False):
        self._desc = "Unknown Error"
        self._detail = detail
        self._fatal = fatal

    def getdesc(self) -> str:
        return self._desc

    def getdetail(self) -> str:
        return self._detail

    def isfatal(self) -> bool:
        return self._fatal


class NoPathError(DrhError):
    def __init__(self, detail: str, fatal: bool = True):
        super().__init__(detail, fatal)
        self._desc = "No path supplied!"


class PathError(DrhError):
    def __init__(self, detail: str, fatal: bool = False):
        super().__init__(detail, fatal)
        self._desc = "The given simple path doesn't lead to a directory or at least one of the submitted list paths " \
                    "is a directory (should be a file)!"


class PathExistsError(DrhError):
    def __init__(self, detail: str, fatal: bool = True):
        super().__init__(detail, fatal)
        self._desc = "The software couldn't create a necessary file/path, because this file/path does already exist"


class FormatError(DrhError):
    def __init__(self, detail: str, fatal: bool = False):
        super().__init__(detail, fatal)
        self._desc = "At least one of the submitted files is not a TAR file!"


class AIPError(DrhError):
    def __init__(self, detail: str, fatal: bool = False):
        super().__init__(detail, fatal)
        self._desc = "At least one of the submitted files couldn't be read because it isn't a valid AIP!"


class IEError(DrhError):
    def __init__(self, detail: str, fatal: bool = False):
        super().__init__(detail, fatal)
        self._desc = "The submitted AIPs and VZE Info don't represent the same Intellectual Entity. At least one of the "\
                     "submitted files represents a different Entity than the others."


class IEUncompleteError(DrhError):
    def __init__(self, detail: str, fatal: bool = False):
        super().__init__(detail, fatal)
        self._desc = "It seems like the set of submitted AIPs for this IE is uncomplete: At least one AIP mentions a " \
                     "parent AIP, that is not present."


class ParsingError(DrhError):
    def __init__(self, detail: str, desc: str, fatal: bool = False):
        super().__init__(detail, fatal)
        self._desc = desc


class SavingError(DrhError):
    def __init__(self, detail: str, desc: str, fatal: bool = False):
        super().__init__(detail, fatal)
        self._desc = desc
