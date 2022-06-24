class DrhError:
    """Base class for all DIP Request Handler errors.

    Provides basic getters for class properties.
    """

    def __init__(self, detail: str, fatal: bool = False):
        """Initialize and return a DrhError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type fatal: bool
        """
        self._desc = "Unknown Error"
        self._detail = detail
        self._fatal = fatal

    def getdesc(self) -> str:
        """Return the error's description."""
        return self._desc

    def getdetail(self) -> str:
        """Return the error's detail hint."""
        return self._detail

    def isfatal(self) -> bool:
        """Return the error's fatal hint (bool)."""
        return self._fatal


class NoPathError(DrhError):
    """Class for a NoPathError.

    Should be invoked when no path was supplied.
    """

    def __init__(self, detail: str, fatal: bool = True):
        """Initialize and return a NoPathError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = "No path supplied!"


class PathError(DrhError):
    """Class for a PathError.

    Should be invoked when the given simple path doesn't lead to a directory or
    at least one of the submitted list paths is a directory instead of a file.
    """

    def __init__(self, detail: str, fatal: bool = False):
        """Initialize and return a PathError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = "The given simple path doesn't lead to a directory or at least one of the submitted list paths " \
                    "is a directory (should be a file)!"


class PathExistsError(DrhError):
    """Class for a PathExistsError.

    Should be invoked when a necessary file/path can't be created, because
    this file/path does already exist.
    """

    def __init__(self, detail: str, fatal: bool = True):
        """Initialize and return a PathExistsError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = "The software couldn't create a necessary file/path, because this file/path does already exist"


class FormatError(DrhError):
    """Class for a FormatError.

    Should be invoked when at least one of the submitted files is not a TAR file.
    """

    def __init__(self, detail: str, fatal: bool = False):
        """Initialize and return a FormatError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = "At least one of the submitted files is not a TAR file!"


class AIPError(DrhError):
    """Class for an AIPError.

    Should be invoked when at least one of the submitted files
    couldn't be read because it isn't a valid AIP.
    """

    def __init__(self, detail: str, fatal: bool = False):
        """Initialize and return a AIPError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = "At least one of the submitted files couldn't be read because it isn't a valid AIP!"


class IEError(DrhError):
    """Class for an IEError.

    Should be invoked when the submitted AIPs and VZE Info don't represent the same
    Intellectual Entity. This means, at least one of the submitted files represents
    a different Entity than the others.
    """

    def __init__(self, detail: str, fatal: bool = False):
        """Initialize and return a IEError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = "The submitted AIPs and VZE Info don't represent the same Intellectual Entity. At least one of the "\
                     "submitted files represents a different Entity than the others."


class IEIncompleteError(DrhError):
    """Class for an IEIncompleteError.

    Should be invoked when it seems like the set of submitted AIPs are incomplete.
    This can be suspected, when at least one AIP mentions a parent AIP, that is not present.
    """

    def __init__(self, detail: str, fatal: bool = False):
        """Initialize and return a IEIncompleteError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = "It seems like the set of submitted AIPs for this IE is incomplete: At least one AIP mentions a " \
                     "parent AIP, that is not present."


class ParsingError(DrhError):
    """Class for a ParsingError.

    This class is meant to hold additional errors that are raised during the
    parsing of an AIP, DIP or VDIP. The _desc parameter of the class can then
    hold any traceback of those errors.
    """

    def __init__(self, detail: str, desc: str, fatal: bool = False):
        """Initialize and return a ParsingError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param desc: A custom description for the error (normally the traceback).
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type desc: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = desc


class SavingError(DrhError):
    """Class for a SavingError.

    This class is meant to hold additional errors that are raised during the
    saving of an AIP, DIP or VDIP. The _desc parameter of the class can then
    hold any traceback of those errors.
    """

    def __init__(self, detail: str, desc: str, fatal: bool = False):
        """Initialize and return a SavingError object.

        :param detail: A hint to what raised the error (normally the IP id)
        :param desc: A custom description for the error (normally the traceback).
        :param fatal: Indicates, whether the error was fatal (program stops) or not fatal (program runs on)
        :type detail: str
        :type desc: str
        :type fatal: bool
        """
        super().__init__(detail, fatal)
        self._desc = desc
