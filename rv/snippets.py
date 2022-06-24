import json
import os.path

from drh.err import DrhError


class UiTextProvider:
    """A class, that handles rich text construction and the fetching of GUI strings for the Request Viewer."""

    def __init__(self, texts: str):
        """Initializes and returns a UiTextProvider object.

        :param texts: The path to the json file containing all keyworded string components for the GUI.
        """

        with open(os.path.join(texts), "r", encoding="UTF-8") as confile:
            self.texts = json.load(confile)

    def s(self, what: str) -> str | None:
        """Returns the GUI string component for the given keyword.

        :return: The wanted string or None, if the key doesn't exist.
        """

        if what in self.texts and isinstance(self.texts[what], str):
            return self.texts[what]
        return None

    def sfl(self, list_: str, i: int) -> str | None:
        """Returns the ith GUI string component out of the list behind the given keyword.

        (sfl = string from list)

        :param list_: The keyword for the list containing the wanted string.
        :param i: The list index of the wanted string.
        :return: The wanted string or None, if the key doesn't exist or the key/index isn't a list.
        """

        if list_ in self.texts and isinstance(self.texts[list_], list):
            if len(self.texts[list_]) >= i+1 and isinstance(self.texts[list_][i], str):
                return self.texts[list_][i]
        return None

    def sfnl(self, list_: str, i1: int, i2: int) -> str | None:
        """Returns the i2th GUI string component out of the i1th list of the nested list behind the given keyword.

        (sfnl = string fro nested list)

        :param list_: The keyword for the nested list.
        :param i1: The list index of the lower level list containing the wanted string.
        :param i2: The list index of the wanted string.
        :return: The wanted string or None, if the key doesn't exist or the key/index isn't a list.
        """

        if list_ in self.texts and isinstance(self.texts[list_], list):
            if len(self.texts[list_]) >= i1+1 and isinstance(self.texts[list_][i1], list):
                if len(self.texts[list_][i1]) >= i2 + 1 and isinstance(self.texts[list_][i1][i2], str):
                    return self.texts[list_][i1][i2]
        return None

    def constructItb(self, info: dict) -> str:
        """Construct and return an infotext as rich text.

        The given infotext dictionary should have the following structure:
            * "main": The main title of the text (str).
            * "sections": A list of sections, each one being a dictionary with the following structure.

                * "sub": The subtitle of the section (str).
                * "paragraphs": A list of strings, each string representing one paragraph.

        :param info: A dictionary containing the infotext.
        :return: The given infotext as rich text (str).
        """

        ps = self._makep(info["main"], margin=(4, 10, 2, 10), fontsize=16, fontweight=600)

        for s in info["sections"]:
            ps += self._makep(s["sub"], margin=(8, 10, 2, 10), fontsize=14)

            for p in s["paragraphs"]:
                ps += self._makep(p, margin=(0, 10, 0, 20))

        ps = self._htmlwrap(ps)
        return ps

    def constructProfileItb(self, infos: list) -> str:
        """Construct and return profile specific information as rich text.

        The given infos list about the profile should contain information about the following
        aspects in this order:
        1. Full textual description.
        2. User recommendation (suitability).
        3. Which IE level metadata is contained?
        4. Which item level metadata is contained?
        5. Which metadata about the archival process is contained?
        6. Which representations can be chosen?
        7. Other information.

        Each information point must be supplied in form of a list itself, containing multiple strings, each
        representing exactly one paragraph. If one subsection is to be left empty, then an empty list can
        be supplied for this section.

        :param infos: A list containing profile specific information.
        :return: The given information as rich text (str).
        """

        ps = ""
        for i in range(len(infos)):
            if not infos[i]:
                continue
            if self.texts["profinfosubs"][i]:
                ps += self._makep(self.texts["profinfosubs"][i], margin=(0, 10, 0, 20), fontweight=600)
            ps += self._makep("<br>".join(infos[i]), margin=(0, 10, 5, 23))
        return self._htmlwrap(ps)

    def constructRepItb(self, date: str, files: list[dict]) -> str:
        """Construct and return AIP specific information as rich text.

        The given list of files contained in the AIP should consist of one dictionary
        per file, where each dictionary has the following structure:
            * "name": The main title of the text (str).
            * "format": A list of sections, each one being a dictionary with the following structure.
            * "size": The subtitle of the section (str).
            * "preslev": The preservation level of the file.

        :param date: The creation date of the AIP as string.
        :param files: A list containing an info dictionary for each file.
        :return: The given information as rich text (str).
        """

        ps = self._makep("<span style=\"font-weight: 600\">"+self.texts["aipcreated"]+": </span>" + date,
                         margin=(0, 10, 0, 20))
        ps += "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; " \
              "margin-right:0px;\" cellspacing=\"10\" cellpadding=\"0\"><tr>"
        for h in self.texts["aiptable"]:
            ps += "<td>" + self._makep(h, fontweight=600, margin=(0, 10, 0,  0)) + "</td>"
        ps += "</tr>"

        for f in files:
            ps += "<tr>"
            ps += "<td>" + self._makep(f["name"]) + "</td>"
            ps += "<td>" + self._makep(f["format"]) + "</td>"
            ps += "<td>" + self._makep(f["size"] + " KB") + "</td>"
            ps += "<td>" + self._makep(f["preslev"]) + "</td>"
            ps += "</tr>"
        ps += "</table>"
        return self._htmlwrap(ps)

    def constructIeItb(self, infos: list[str] = None) -> str:
        """Construct and return an IE overview as rich text.

        The given infos list about the IE should contain information about the following
        aspects in this order:
        1. Signature
        2. Title
        3. Runtime
        4. Contains or Description

        Each information point must be supplied in form of a string. If one subsection is to be
        left empty, then an empty string can be supplied for this section.

        :param infos: A list containing IE specific information.
        :return: The given information as rich text (str).
        """

        if not infos:
            ps = self._makep(self.texts["noIeTitle"], fontstyle="italic")
            return self._htmlwrap(ps)
        ps = ""
        for i in range(len(self.texts["ieProps"])):
            ps += self._makep(self.texts["ieProps"][i] + ":", fontstyle="italic")
            ps += self._makep(infos[i], margin=(0, 0, 0, 10))
        return self._htmlwrap(ps)

    def constructProfItb(self, no: int = None, title: str = None) -> str:
        """Construct and return a profile overview as rich text.

        :param no: The profile number (not index!) of the chosen profile.
        :param title: The short title of the chosen profile.
        :return: The given information as rich text (str).
        """

        ps = self._makep(self.texts["profTbTitle"] + ":", fontweight=600)
        if no is not None:
            ps += self._makep(str(no) + " ("+title+")", margin=(0, 0, 0, 10))
        return self._htmlwrap(ps)

    def constructOvRepItb(self, nos: list[int] = None, aip: bool = False) -> str:
        """Construct and return an aip overview as rich text.

        If the method is called with its default param values, then it will create
        a text with a "no IE chosen" message. If the method is called without nos,
        but with aip set to true, then it will create a text with a "no AIP chosen"
        message. Otherwise, it will create a rich text listing all the given AIP nos.

        :param nos: The numbers of the chosen aips as list.
        :param aip: Indicates, whether an AIP has already been chosen or not. Sie explanation above.
        :return: The given information as rich text (str).
        """

        ps = self._makep(self.texts["repTbTitle"] + ":", fontweight=600)
        if nos:
            for i in range(len(nos)):
                if i == 0:
                    title = self.texts["root"]
                else:
                    title = self.texts["rep"]
                ps += self._makep(str(nos[i]) + " (" + title + ")", margin=(0, 0, 0, 10))
        elif aip:
            ps += self._makep(self.texts["noRepTitle"], margin=(0, 0, 0, 10))
        else:
            ps += self._makep(self.texts["noIeTitle"], margin=(0, 0, 0, 10))
        return self._htmlwrap(ps)

    def constructSuccessBrowser(self, details_: list[str]) -> str:
        """Construct and return a detailed success message as rich text.

        The given details are formatted as a simple list. Each list element becomes
        a list entry and starts with a hyphen (-).

        :param details_: A list of strings, that represent detailed information.
        :return: The given details as rich text (str).
        """

        ps = ""
        for p in details_:
            ps += self._makep("- " + os.path.normpath(p))
        return self._htmlwrap(ps)

    def constructErrorBrowser(self, errs: list[DrhError]) -> str:
        """Construct and return a detailed error message as rich text.

        The given DrhErrors are formatted as a simple list. Each list element has a title
        (the error object's class name), a description (fetched from the UiTextProvider's
        loaded list of texts) and a hint, which file caused the error.

        :param errs: A list of DrhErrors, that occurred.
        :return: The given details as rich text (str).
        """

        ps = ""
        for e in errs:
            ename = e.__class__.__name__
            ps += self._makep(ename + ":", fontweight=600)
            if ename in self.texts["errors"]:
                ps += self._makep(self.texts["errors"][ename])
                if e.getdetail():
                    ps += self._makep(self.texts["impactedfile"] + ": " + e.getdetail(), margin=(0, 0, 10, 0))
            else:
                ps += self._makep(self.texts["impactedip"] + ": " + e.getdetail())
                ps += self._makep(self.texts["traceback"] + ": " + e.getdesc(), margin=(0, 0, 10, 0))
        return self._htmlwrap(ps)

    def wraptext(self, text: str) -> str:
        """Wrap the given text into a rich text paragraph and document.

        :param text: The text to be wrapped.
        :return: The given text as rich text.
        """

        ps = self._makep(text)
        return self._htmlwrap(ps)

    def _makep(self,
               text: str,
               margin: tuple = (0, 0, 0, 0),
               textindent: int = 0,
               qtblockindent: int = 0,
               fontweight: int = 400,
               fontsize: int = 12,
               font: str = "Source Sans Pro",
               fontstyle: str = "normal") -> str:
        """Wrap the given text in to a rich text paragraph snippet.

        All style parameters are optional. The function will use the default values,
        if no custom value is specified

        :param text: The text to be wrapped.
        :param margin: The margins of the paragraph (top, right, bottom, left).
        :param textindent: The indentation of the paragraph (from the left).
        :param qtblockindent: The QT-block-indent of the paragraph.
        :param fontweight: The fontweight.
        :param fontsize: The font size (in pts).
        :param font: The font family.
        :param fontstyle: The font style.
        :return: The given text as rich text paragraph
        :type text: str
        :type margin: tuple(int, int, int, int)
        :type textindent: int
        :type qtblockindent: int
        :type fontweight: int
        :type fontsize: int
        :type font: str
        :type fontstyle: str
        """

        return "<p style=\" margin-top:" + str(margin[0]) + "px; margin-bottom:" + str(margin[2]) + "px; margin-left:" \
               + str(margin[3]) + "px; margin-right:" + str(margin[1]) + "px; -qt-block-indent:" + str(
               qtblockindent) + "; text-indent:" + str(textindent) + "px; font-size:" + str(fontsize) + \
               "pt; font-weight:" + str(fontweight) + "; font-family:"+font+"; font-style:"+fontstyle+"\">" \
               + text + "</p>"

    def _htmlwrap(self, middle: str, fontsize: int = 12, font: str = "Source Sans Pro") -> str:
        """Wrap the given text in to a rich text document.

        The style parameters are optional. The function will use the default values,
        if no custom value is specified

        :param middle: The text to be wrapped.
        :param fontsize: The size of the font.
        :param font: The font family.
        :return: The given text as rich text paragraph.
        :type middle: str
        :type fontsize: int
        :type font: str
        """

        return u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" \
               "p, li { white-space: pre-wrap; }\n" \
               "</style></head><body style=\" font-family:'" + font + "'; font-size:" + str(fontsize) + \
               "pt; font-weight:400; font-style:normal;\">\n" + middle + "</body></html>"
