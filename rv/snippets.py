
class UiTextProvider:

    def __init__(self):
        self.profinfosubs = [
            None,
            "Empfehlung",
            "Metadaten der Ebene Intellektuelle Einheit (IE)",
            "Metadaten auf Datei-Ebene (Item)",
            "Metadaten aus dem archivischen Prozess",
            "Verfügbare Repräsentationen",
            "Sonstiges"
        ]

    def _makep(self, text, margin=(0, 0, 0, 0), textindent=0, qtblockindent=0, fontweight=400, fontsize=12,
              font="Source Sans Pro"):
        return "<p style=\" margin-top:" + str(margin[0]) + "px; margin-bottom:" + str(margin[2]) + "px; margin-left:" + \
               str(margin[3]) + "px; margin-right:" + str(margin[1]) + "px; -qt-block-indent:" + str(
            qtblockindent) + "; " \
                             "text-indent:" + str(textindent) + "px; font-size:" + str(
            fontsize) + "pt; font-weight:" + str(fontweight) + "; font-family:"+font+"\">"\
            + text + "</p>"

    def constructItb(self, info, fontsize=12, font="Source Sans Pro"):
        ps = self._makep(info["main"], margin=(4, 10, 2, 10), fontsize=16, fontweight=600)

        for s in info["sections"]:
            ps += self._makep(s["sub"], margin=(8, 10, 2, 10), fontsize=14)

            for p in s["paragraphs"]:
                ps += self._makep(p, margin=(0, 10, 0, 20))

        ps = self._htmlwrap(ps)
        return ps

    def constructProfileItb(self, infos):
        ps = ""
        for i in range(len(infos)):
            if not infos[i]:
                continue
            if self.profinfosubs[i]:
                ps += self._makep(self.profinfosubs[i], margin=(0, 10, 0, 20), fontweight=600)
            ps += self._makep("<br>".join(infos[i]), margin=(0, 10, 5, 23))
        return self._htmlwrap(ps)

    def _htmlwrap(self, middle, fontsize=12, font="Source Sans Pro"):
        return u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" \
               "p, li { white-space: pre-wrap; }\n" \
               "</style></head><body style=\" font-family:'" + font + "'; font-size:" + str(
            fontsize) + "pt; font-weight:400; font-style:normal;\">\n" + \
               middle + \
               "</body></html>"


windowTitle = "DIP Request Viewer"
menuTitles = [u"DIP-Generierung", u"Was sind DIP-Profile?", u"Was sind Repr\u00e4sentationen?", u"Programm-Info"]
menuStatuses = [u"DIP Anforderung", u"Hilfe: Was sind Profile?", u"Hilfe: Was sind Repr\u00e4sentationen?",
                     u"Hilfe: Programm-Info"]
step = "Schritt"
help = "Hilfe"
details = "Details"

stepTitles = [u"Archivale w\u00e4hlen", u"DIP-Profil w\u00e4hlen", u"Repr\u00e4sentationen w\u00e4hlen"]

spinnerPh = [
    u"AIP-Datei",
    u"Archivsoftware-Export"
]
spinnerTooltip = [
    "Datei(en) wählen",
    "Ordner wählen",
    "Datei wählen",
    "AIPs laden"
]

profile = "Profil"
profLabel = u"W\u00e4hlen Sie hier, wie die technischen Daten des Archivales f\u00fcr Sie aufbereitet werden sollen!"
repLabel = u"W\u00e4hlen Sie hier, welche technischen Repr\u00e4sentationen des Archivales Sie sehen wollen!"

overviewBtns = [
    "Viewer",
    "Download",
    "Beides"
]

deliv = "Bereitstellung"
choice = "Ihre Auswahl"
goStatus = u"DIP anfordern"
go = "Los"

aipInfos = [u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Dies ist ein Platzhaltertext - yeah.</p></body></html>"
]

profileTitles = [u"Profil " + str(i) for i in range(4)]
profileRecom = [u"Empfohlen für...", u"Empfohlen für...", u"Empfohlen für...", u"Empfohlen für..."]
profileInfos = [
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Dies ist ein Platzhaltertext - yeah.</p></body></html>",
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Dies ist ein Platzhaltertext - yeah.</p></body></html>",
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Dies ist ein Platzhaltertext - yeah.</p></body></html>",
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Dies ist ein Platzhaltertext - yeah.</p></body></html>"
    ]

overviewTexts = [
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Signatur:</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Lorem Ipsum</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Titel:</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Lorem Ipsum</p>\n"
    "<p style=\" margin-top:0px; margin-bott"
                            "om:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Laufzeit:</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Lorem Ipsum</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Enth\u00e4lt:</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">Lorem Ipsum</p></body></html>",
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">DIP-Profil</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">0 (Rohdaten)</p></body></html>",
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Repr\u00e4sentationen</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">1 (Ursprung)</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">2 (Repr\u00e4sentation)</p></body></html>"
]

infoTexts = [
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:4px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Maintitle</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
    "<p style=\" margin-top:8px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Subtitle</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
    "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 1</li>\n"
    "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 2</li>\n"
    "<li style=\" margin-top:0p"
    "x; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 3</li></ol>\n"
    "<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 1</li>\n"
    "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 2</li>\n"
    "<li style=\" margin-top:0px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 3</li></ul>\n"
    "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px;\" cellspacing=\"2\" cellpadding=\"0\">\n"
    "<tr>\n"
    "<td>\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt"
    "; font-weight:600;\">Test</span></p></td>\n"
    "<td>\n"
    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:600;\">Test2</span></p></td></tr>\n"
    "<tr>\n"
    "<td></td>\n"
    "<td>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Test4</span></p></td></tr></table></body></html>",
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:4px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:16pt; font-weight:600;\">Maintitle</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:12pt;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</span></p>\n"
    "<p style=\" margin-top:8px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:14pt;\">Su"
    "btitle</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:12pt;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:12pt;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Source Sans Pro'; font-size:12pt;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</span></p>\n"
    "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-rig"
    "ht: 0px; -qt-list-indent: 1;\"><li style=\" font-family:'Source Sans Pro'; font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 1</li>\n"
    "<li style=\" font-family:'Source Sans Pro'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 2</li>\n"
    "<li style=\" font-family:'Source Sans Pro'; font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 3</li></ol></body></html>",
    u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:'Source Sans Pro'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
    "<p style=\" margin-top:4px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Maintitle</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
    "<p style=\" margin-top:8px; margin-bottom:2px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Subtitle</span></p>\n"
    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-"
    "indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
    "<p style=\" margin-top:0px; margin-bottom:5px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet Text Lorem Ipsum dolor sit amet</p>\n"
    "<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 1</li>\n"
    "<li style=\" margin-top:0px; margin-bottom:0px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 2</li>\n"
    "<li style=\" margin-top:0p"
"x; margin-bottom:12px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Element 3</li></ol></body></html>"
]


aipTitles = [u"AIP " + str(i) for i in range(4)]
aipFormats = [u"PDF", u"Format", u"txt", u"word"]
aipDescs = [u"Ursprung", u"Repräsentation"]