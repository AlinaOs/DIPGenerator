import json
import os.path

from drh.err import DrhError


class UiTextProvider:

    def __init__(self, texts: str):
        with open(os.path.join(texts), "r", encoding="UTF-8") as confile:
            self.texts = json.load(confile)

    def s(self, what: str) -> str | None:
        if what in self.texts and isinstance(self.texts[what], str):
            return self.texts[what]
        return None

    def sfl(self, list_: str, i: int) -> str | None:
        if list_ in self.texts and isinstance(self.texts[list_], list):
            if len(self.texts[list_]) >= i+1 and isinstance(self.texts[list_][i], str):
                return self.texts[list_][i]
        return None

    def sfnl(self, list_: str, i1: int, i2: int) -> str | None:
        if list_ in self.texts and isinstance(self.texts[list_], list):
            if len(self.texts[list_]) >= i1+1 and isinstance(self.texts[list_][i1], list):
                if len(self.texts[list_][i1]) >= i2 + 1 and isinstance(self.texts[list_][i1][i2], str):
                    return self.texts[list_][i1][i2]
        return None

    def constructItb(self, info: dict) -> str:
        ps = self._makep(info["main"], margin=(4, 10, 2, 10), fontsize=16, fontweight=600)

        for s in info["sections"]:
            ps += self._makep(s["sub"], margin=(8, 10, 2, 10), fontsize=14)

            for p in s["paragraphs"]:
                ps += self._makep(p, margin=(0, 10, 0, 20))

        ps = self._htmlwrap(ps)
        return ps

    def constructProfileItb(self, infos: dict) -> str:
        ps = ""
        for i in range(len(infos)):
            if not infos[i]:
                continue
            if self.texts["profinfosubs"][i]:
                ps += self._makep(self.texts["profinfosubs"][i], margin=(0, 10, 0, 20), fontweight=600)
            ps += self._makep("<br>".join(infos[i]), margin=(0, 10, 5, 23))
        return self._htmlwrap(ps)

    def constructRepItb(self, date: str, files: list[dict]) -> str:
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
        if not infos:
            ps = self._makep(self.texts["noIeTitle"], fontstyle="italic")
            return self._htmlwrap(ps)
        ps = ""
        for i in range(len(self.texts["ieProps"])):
            ps += self._makep(self.texts["ieProps"][i] + ":", fontstyle="italic")
            ps += self._makep(infos[i], margin=(0, 0, 0, 10))
        return self._htmlwrap(ps)

    def constructProfItb(self, no: int = None, title: str = None) -> str:
        ps = self._makep(self.texts["profTbTitle"] + ":", fontweight=600)
        if no is not None:
            ps += self._makep(str(no) + " ("+title+")", margin=(0, 0, 0, 10))
        return self._htmlwrap(ps)

    def constructOvRepItb(self, nos: list[int] = None, aip: bool = False) -> str:
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
        ps = ""
        for p in details_:
            ps += self._makep("- " + os.path.normpath(p))
        return self._htmlwrap(ps)

    def constructErrorBrowser(self, errs: list[DrhError]) -> str:
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
        return "<p style=\" margin-top:" + str(margin[0]) + "px; margin-bottom:" + str(margin[2]) + "px; margin-left:" \
               + str(margin[3]) + "px; margin-right:" + str(margin[1]) + "px; -qt-block-indent:" + str(
               qtblockindent) + "; text-indent:" + str(textindent) + "px; font-size:" + str(fontsize) + \
               "pt; font-weight:" + str(fontweight) + "; font-family:"+font+"; font-style:"+fontstyle+"\">" \
               + text + "</p>"

    def _htmlwrap(self, middle: str, fontsize: int = 12, font: str = "Source Sans Pro") -> str:
        return u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" \
               "p, li { white-space: pre-wrap; }\n" \
               "</style></head><body style=\" font-family:'" + font + "'; font-size:" + str(fontsize) + \
               "pt; font-weight:400; font-style:normal;\">\n" + middle + "</body></html>"
