import os.path

errors = {
    "DrhError":
        "Unbekannter Fehler",
    "NoPathError":
        "Sie müssen einen Pfad für die AIP-Dateien angeben, bevor Sie sie laden können!",
    "PathError":
        "Die Datei/der Ordner existiert nicht oder der Pfad ist ein falscher Typ (d.h., er führt zu "
        "einem Ordner, obwohl er zu einer Datei führen sollte, oder er führt zu einer Datei, "
        "obwohl er zu einem Ordner führen sollte).",
    "PathExistsError":
        "Das Programm konnte eine(n) notwendige(n) Datei/Pfad nicht erstellen, "
        "da die Datei/der Pfad bereits existiert.",
    "FormatError":
        "Mindestens eine der eingereichten AIP-Dateien ist keine TAR-Datei.",
    "AIPError":
        "Mindestens eine der eingereichte AIP-Dateien konnte nicht gelesen werden, "
        "da sie kein valides AIP darstellt.",
    "IEError":
        "Die eingereichten AIPs und der ausgewählte Archivsoftware-Export "
        "repräsentieren nicht dieselbe Intellektuelle Einheit. Mindestens eine "
        "der Dateien repräsentiert eine andere Einheit als die anderen."
    ,
    "IEUncompleteError":
        "Es scheint, dass nicht alle AIPs für das gewünschte Archivale "
        "eingereicht worden sind. Mindestens ein Parent-AIP wird genannt, "
        "das nicht vorhanden ist."
}

impactedip = "Betroffenes Information Package"
impactedfile= "Pfad der Datei"
traceback_ = "Fehlermeldung"


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
        self.aiptable = [
            "Datei",
            "Format",
            "Dateigröße",
            "Erhaltungslevel"
        ]
        self.ieProps = [
            "Signatur",
            "Titel",
            "Art",
            "Laufzeit",
            "Enthält"
        ]

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

    def constructRepItb(self, date, files):
        ps = self._makep("<span style=\"font-weight: 600\">"+aipcreated+": </span>" + date, margin=(0, 10, 0, 20))
        ps += "<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:20px; " \
              "margin-right:0px;\" cellspacing=\"10\" cellpadding=\"0\"><tr>"
        for h in self.aiptable:
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

    def constructIeItb(self, infos=None):
        if not infos:
            ps = self._makep(noIeTitle, fontstyle="italic")
            return self._htmlwrap(ps)
        ps = ""
        for i in range(len(self.ieProps)):
            ps += self._makep(self.ieProps[i] + ":", fontstyle="italic")
            ps += self._makep(infos[i], margin=(0, 0, 0, 10))
        return self._htmlwrap(ps)

    def constructProfItb(self, no=None, title=None):
        ps = self._makep(profTbTitle + ":", fontweight=600)
        if no is not None:
            ps += self._makep(str(no) + " ("+title+")", margin=(0, 0, 0, 10))
        return self._htmlwrap(ps)

    def constructOvRepItb(self, nos=None, aip=False):
        ps = self._makep(repTbTitle + ":", fontweight=600)
        if nos:
            for i in range(len(nos)):
                if i == 0:
                    title = root
                else:
                    title = rep
                ps += self._makep(str(nos[i]) + " (" + title + ")", margin=(0, 0, 0, 10))
        elif aip:
            ps += self._makep(noRepTitle, margin=(0, 0, 0, 10))
        else:
            ps += self._makep(noIeTitle, margin=(0, 0, 0, 10))
        return self._htmlwrap(ps)

    def constructSuccessBrowser(self, details_):
        ps = ""
        for p in details_:
            ps += self._makep("- " + os.path.normpath(p))
        return self._htmlwrap(ps)

    def constructErrorBrowser(self, errs):
        ps = ""
        for e in errs:
            ename = e.__class__.__name__
            ps += self._makep(ename + ":", fontweight=600)
            if ename in errors:
                ps += self._makep(errors[ename])
                if e.getdetail():
                    ps += self._makep(impactedfile + ": " + e.getdetail(), margin=(0, 0, 10, 0))
            else:
                ps += self._makep(impactedip + ": " + e.getdetail())
                ps += self._makep(traceback_ + ": " + e.getdesc(), margin=(0, 0, 10, 0))
        return self._htmlwrap(ps)

    def wraptext(self, text):
        ps = self._makep(text)
        return self._htmlwrap(ps)

    def _makep(self, text, margin=(0, 0, 0, 0), textindent=0, qtblockindent=0, fontweight=400, fontsize=12,
               font="Source Sans Pro", fontstyle="normal"):
        return "<p style=\" margin-top:" + str(margin[0]) + "px; margin-bottom:" + str(margin[2]) + "px; margin-left:" + \
               str(margin[3]) + "px; margin-right:" + str(margin[1]) + "px; -qt-block-indent:" + str(
            qtblockindent) + "; " \
                             "text-indent:" + str(textindent) + "px; font-size:" + str(
            fontsize) + "pt; font-weight:" + str(fontweight) + "; font-family:"+font+"; font-style:"+fontstyle+"\">"\
            + text + "</p>"

    def _htmlwrap(self, middle, fontsize=12, font="Source Sans Pro"):
        return u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n" \
               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n" \
               "p, li { white-space: pre-wrap; }\n" \
               "</style></head><body style=\" font-family:'" + font + "'; font-size:" + str(fontsize) + \
               "pt; font-weight:400; font-style:normal;\">\n" + middle + "</body></html>"

noIeTitle = "Noch kein Archivale gewählt!"
noRepTitle = "Noch keine Repräsentation gewählt!"
profTbTitle = "Profil"
repTbTitle = "Repräsentationen"

aipcreated = "Erstellt"
AIP = "AIP"
root = "Ursprung"
rep = "Repräsentation"
typecollection = "Dateisammlung"
typeefile = "E-Akte"

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
    u"Archivsoftware-Export",
    u"Speichern unter"
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

profileTitles = [u"Profil " + str(i) for i in range(4)]
profileRecom = [u"Empfohlen für...", u"Empfohlen für...", u"Empfohlen für...", u"Empfohlen für..."]

msgDefault = "Etwas ist schiefgelaufen!"
msgDefaultInfo = "Keine Details verfügbar."
msgTitle = [
    [
        "AIPs erfolgreich geladen!",
        "DIP erfolgreich gespeichert!"
    ],
    [
        "Mögliche Probleme beim Laden",
        "Mögliche Probleme beim Laden oder Speichern",
        "Alles richtig?"
    ],
    [
        "TAR-Pakete konnten nicht geladen werden!",
        "DIP konnte nicht gespeichert werden!",
        "Fehlende Angaben!"
    ],
    [
        msgDefault,
        msgDefault,
        msgDefault
    ]
]
msgInfo = [
    [
        "",
        "Speicherort(e) siehe Details."
    ],
    [
        "Die AIP-Dateien konnten erfolgreich eingelesen werden, doch es wurde ein mögliches " \
        "Problem erkannt. Überprüfen " \
        "Sie ggf. anhand der Details, ob die gemeldeten Probleme relevant sind.",
        "Das DIP konnte erfolgreich gespeichert werden, doch bei der Erstellung " \
        "des DIP oder dem Einlesen der AIP-Dateien wurde ein mögliches Problem " \
        "erkannt. Überprüfen Sie ggf. anhand der Details, ob die " \
        "gemeldeten Probleme relevant sind. Falls ja, beheben Sie die Probleme und laden "
        "Sie die AIP-Dateien erneut.",
        "Sie haben einen neuen AIP-Pfad eingegeben, aber noch nicht geladen. "
        "Möglicherweise werden Ihnen noch die alten, unerwünschten AIPs angezeigt?<br>"
        '<br>Klicken Sie "Ok", wenn mit der DIP-Generierung trotzdem fortgefahren werden soll.<br>'
        "<br>Wenn Sie die eingegebenen Dateipfade zum Generieren der DIPs nutzen wollen, klicken "
        'Sie "Abbrechen" und bestätigen Sie zunächst die AIP-Eingabe.'
    ],
    [
        "Siehe die Details für mehr Infos.",
        "Siehe Details für mehr Infos.",
        "Mindestens eine notwendige Angabe fehlt! Bitte"
        "<ol><li>geben Sie AIP-Dateien oder einen Ordner mit AIP-Dateien ein (und bestätigen diese Auswahl)</li>"
        "<li>wählen Sie einen Speicherort für die fertigen DIP-Dateien</li></ol>"
    ],
    [
        msgDefaultInfo,
        msgDefaultInfo
    ]
]
msgWindow = [
    "Info",
    "Hinweis",
    "Fehler",
    "Fehler"
]
msgdet = "Details"
