# DIPGenerator
Module for generating profile specific Dissemination Information Packages (DIP) from Archival Information Packages (AIP) in a longterm digital archive.

The goal of the program is to provide a user interface, with which a user in an archive can be provided with information about possible DIP profiles and choosable representations of an archival file. They can then choose one profile (causing the metadata of the archival file to be filtered in a specified way) and one ore more representations.

The program also handles the request. It loads the requested representations and generates a DIP according to profile sepcific configurations. The DIP is then saved in the location the user chose.

This program serves as a prototype to demonstrate the concept of DIP profiles. It was developed in 2022 during an internship in the department [*DiPS.kommunal* of the LWL Archivamt für Westfalen](https://www.lwl-archivamt.de/de/elektronische-langzeitarchivierung/dipskommunal/). It has therefore been developed to fit the technichal environment and metadata schema of *DiPS.kommunal* and the GUI was designed according to the LWL corporate design. The concept behind the program can nevertheless be adapted to other longterm archives.

*DiPS.kommunal* is a software solution for digital preservation in communal archives in North Rhine Westphalia, Germany. It is operated by the Landschaftsverband Westfalen-Lippe ([LWL](https://lwl.org/)) and the [City of Cologne](https://www.stadt-koeln.de/artikel/62898/index.html) and it is part of the [DA-NRW](https://www.danrw.de/).



# Documentation (german)

- [Allgemeiner Aufbau](#allgemeiner-aufbau)
    - [`drh`](#drh)
    - [`rv`](#rv)
    - [`config`](#config)
    - [`svg`](#svg)
    - [`main.py`](#mainpy)
- [Konfigurationsmöglichkeiten](#konfigurationsmöglichkeiten)
    - [Anzahl, Name und Nummer von Profilen](#anzahl-name-und-nummer-von-profilen)
    - [Profil-abhängige Filterung von Metadaten](#profil-abhängige-filterung-von-metadaten)
    - [Infotexte zu Profilen](#infotexte-zu-profilen)
    - [Default-Auswahl](#default-auswahl)
    - [Profil-abhängige Einschränkung von Auswahlmöglichkeiten](#profil-abhängige-einschränkung-von-auswahlmöglichkeiten)
    - [Allgemeine Infotexte](#allgemeine-infotexte)
    - [GUI-Texte](#gui-texte)

- [Integration von Informationen aus einer Verzeichnungssoftware (VZE-Info)](#integration-von-informationen-aus-einer-verzeichnungssoftware-vze-info)
- [Erzeugung von ViewDIPs](#erzeugung-von-viewdips)
- [Nutzung des `drh` Moduls ohne das `rv` Modul](#nutzung-des-drh-moduls-ohne-das-rv-modul)
- [Dependencies](#dependencies)
- [Noch zu ergänzende Dateien](#noch-zu-ergänzende-dateien)


## Allgemeiner Aufbau

### `drh`
Das `drh` Modul (**D**IP **R**equest **H**andler) stellt Klassen und Funktionen bereit, die der Erzeugung von DIPs gemäß vorgegebener DIP-Profile dienen. Es bezieht dabei alle nötigen Informationen über und Konfigurationen für die DIP-Profile aus den Konfigurationsdateien im `config` Ordner.

### `rv`
Das `rv` Modul (**R**equest **V**iewer) stellt Klassen und Funktionen für eine graphische Benutzeroberfläche bereit. Die Klasse `RvMainWindow` enthält dabei die GUI-Elemente selbst, während die Klasse `RequestViewer` die Steuerung der GUI und die Kommunikation mit dem `drh.DIPRequestHandler` übernimmt.

### `config`
Der Ordner enthält alle Konfigurationsdateien, die für die Erzeugung von DIPs und ViewDIPs nötig sind. Dabei ist die interne Struktur des Ordners zweitrangig, da die Pfade zu allen Dateien in der jeweiligen Hauptkonfiguration für DIPs bzw. ViewDIPs festgehalten werden müssen und das Programm nur darüber auf die Dateien zugreift.
Diese Hauptkonfiguration (`profile_config.json`) muss in der `main.py` angegeben werden. Sie enthält allgemeine Informationen, auf die der `DIPRequestHandler` zugreift. Zusätzlich dazu können spezifischere Angaben für einzelne Profile nötig werden. Dies ist insbesondere bei der DIP-Config der Fall.

Die **DIP-Config** benötigt folgende zusätzliche Dateien:
- `DiPsArchiv.xsd`: XSD-Datei für DiPS-AIPs
- `info.json`: Info-Texte für die allgemeinen Info-Seiten der GUI
- Für jedes Profil mit der Nummer `x`:
    - `DIP-P[x].xsd`: XSD-Datei für DIPs dieses DIP-Profils
    - `p[x]_desc_de.json`: Infotexte über das Profil
    - `p[x]_xsl.xsl`: XSL-Datei zur Transformation von AIP-Metadaten in DIP-Metadaten dieses Profils

Auch hierbei gilt, dass die genaue Benennung der Dateien zweitrangig ist, so lange ihr Dateiname in der Hauptconfig richtig angegeben ist.

Die **ViewDIP-Config** benöigt ggf. ebenfalls weitere Dateien. Die ViewDIP-Config ist allerdings noch nicht ausgereift (siehe den Abschnitt zur Einbindung von [ViewDIPs](#erzeugung-von-viewdips)).

Zusätzlich zu den Config-Dateien, wird eine JSON-Datei mit **GUI-Texten** benötigt (hier `guitexts.json`).

### `svg`
Dieser Ordner enthält die Piktogramme, die von der GUI verwendet werden. Folgende SVGs müssen in dem Ordner vorhanden sein:
* `arrow_down.svg`: Nach unten zeigender Pfeil für Drop-Down-Details
* `arrow_up.svg`: Nach oben zeigender Pfeil für Drop-Down-Details
* `check.svg`: Häkchen für das Bestätigen der Dateiauswahl
* `directory.svg`: Ordnersymbol für die Auswahl eines Ordnerpfades
* `error.svg`: Fehler-Symbol für Fehlermeldungen
* `file_document.svg`: Dateisymbol für die Auswahl eines Dateipfades
* `info.svg`: Info-Symbol für das Navigieren zu Info-Seiten und für Infomeldungen
* `package.svg`: Ein Piktogramm, das DIPakete symbolisiert.
* `warning.svg`: Ein Warn-Symbol für Warnungen.

Für den Prototypen wurden Piktogramme des LWL Corporate Design verwendet, sowie zwei Open Source SVGs:
* https://www.iconshock.com/freeicons/check-circle-fill-24 (als `check.svg`)
* https://www.iconshock.com/freeicons/package-16 (als `package.svg`)

### `main.py`
Diese Datei startet das Programm, indem es einen `RequestViewer`, also die GUI, und einen `DIPRequestHandler` initialisiert. Das Script enthält auch die Pfadangaben, die zu den Konfig-Dateien führen, die alle weiteren Konfigurationen enthalten:
```python
confdir = "config/DIP/" # Pfad zum Ordner mit der DIP-Config
conf = "profile_conf.json" # Pfad zur Hauptconfig für DIPs (relativ zu confdir)
vconfdir = "config/VDIP/" # Pfad zum Ordner mit der ViewDIP-Config
vconf = "profile_conf.json" # Pfad zur Hauptconfig für ViewDIPs (relativ zu vconfdir)
texts = "config/guitexts.json" # Pfad zu den GUI-Texten
```

## Konfigurationsmöglichkeiten
Im Folgenden wird beschrieben, mit welchen Konfigurationsdateien welche Elemente des Programms, der GUI und der DIP-Generierung beeinflusst werden können.

### Anzahl, Name und Nummer von Profilen
Die Anzahl von Profilen ist nicht festgelegt. Um ein Profil anzulegen, genügt es, in der Hauptconfig (hier `profile_conf.json`) unter `profileConfigs` ein neues Objekt einzufügen. In diesem Objekt sind bereits die wichtigsten Eigenschaften eines Profils festgelegt. Das Objekt muss folgende Schlüssel enthalten:
- `DIPGeneration`: Angabe darüber, ob ein DIP generiert werden soll, oder das AIP unbearbeitet ausgeliefert werden soll (Boolean)
- `xsl`: Pfad zur Profil-spezifischen XSL-Datei (siehe [unten](#profil-abhängige-filterung-von-metadaten))
- `desc`:  Pfad zur Profil-spezifischen Infotext-Datei (siehe [unten](#infotexte-zu-profilen))
- `xsd`: Pfad zur Profil-spezifischen XSD-Datei (siehe [unten](#profil-abhängige-filterung-von-metadaten))
- `AIPChoice`: Angabe darüber, ob die User selbst AIPs auswählen dürfen (Boolen, vgl. [unten](#profil-abhängige-einschränkung-von-auswahlmöglichkeiten))
- `defaultAIP`: Default AIP-Auswahl (siehe [unten](#default-auswahl))
- `deliveryChoice`: Angabe darüber, ob die User selbst AIPs auswählen dürfen (Boolen, vgl. [unten](#profil-abhängige-einschränkung-von-auswahlmöglichkeiten))
- `defaultDelivery`: Default AIP-Auswahl (siehe [unten](#default-auswahl))
- `profileMetadata`: Metadaten für die Erzeugung der DIP-Metadaten (siehe [unten](#profil-abhängige-filterung-von-metadaten)). Ein Objekt mit folgenden Schlüsseln:
    - `profileNumber`: Menschenlesbares Kürzel oder Nummer des Profils
    - `profileDescription`: Kurzname des Profils
    - `profileVersion`: Version des Profils

Profile werden in der Reihenfolge angezeigt, in der sie in der Config-Datei stehen.

### Profil-abhängige Filterung von Metadaten
Bei der DIP-Generierung wird basierend auf den Metadaten der ausgewählten AIPs eine neue Metadatendatei für das resultierende DIP erzeugt. Dies geschieht in Abhängigkeit von dem gewählten DIP-Profil mittels der **XSLT-Datei** für das jeweilige Profil. Indem die XSLT-Datei geändert wird, kann also beeinflusst werden, welche Metadaten in das Profil aufgenommen werden, und welche nicht.

Jedem DIP wird eine **XSD-Datei** mitgegeben, die widerspiegelt, welche Metadaten in welchem Schema im DIP enthalten sind. Um genau zu dokumentieren, welche Metadaten aus dem ursprünglichen AIP *nicht* übernommen worden sind, werden die Schemadefinitionen dieser Daten in die XSD übernommen, aber ihr `maxOccurs`-Attribut wird auf `0` gesetzt.

In jeder XSD-Datei finden sich außerdem **allgemeine Angaben** über das benutzte Profil, über dessen Version (siehe [oben](#anzahl-name-und-nummer-von-profilen)), sowie über den benutzten Generierungs-Algorithmus und dessen Version (`generatorName`und `generatorVersion` in der `profile_conf.json`). Die Profilversion ändert sich, sobald etwas an der Profil-spezifischen XSL-Datei geändert wird. Die Version des Algorithmus ändert sich, sobald das Programm, das das DIP generiert, verändert wird. Wird ein gänzlich neues Programm genutzt, so muss ein anderer Name für den Algorithmus angegeben werden. Zu den allgemeinen DIP-Informationen gehört auch die Angabe der herausgebenden Institution und des Typs des AIPs (`issuedBy`und `type` in der `profile_conf.json`).

### Infotexte zu Profilen
Die Informationen zu jedem Profil sind in einer eigenen JSON-Datei festgehalten (hier `p[x]_desc_de.json`). Diese muss folgende Schlüssel enthalten:
- `no`: Die Kennnummer oder das Kürzel, das das Profil in menschenlesbaren Texten haben soll
- `shortName`: Die Kurzbezeichnung für das Profil
- `recommendation`: Eine kurze Empfehlung, für welche Nutzergruppen das Profil geeignet ist
- `repInfo`: Ein Infotext, der dem\*r Nutzer\*in angezeigt wird, wenn er\*sie dieses Profil gewählt hat und AIPs auswählen will (optional; falls leer, wird ein Default-Text gezeigt)
- `deliveryInfo`: Ein Infotext, der dem\*r Nutzer\*in angezeigt wird, wenn er\*sie dieses Profil gewählt hat und die Bereitstellungsart auswählen will (optional; falls leer, wird ein Default-Text gezeigt)
- fullDesc: Ein Objet mit folgenden Schlüsseln:
    - `desc`: Allgemeine Beschreibung des Profils als Fließtext
    - `suitability`: Angabe über die Eignung für bzw. Empfehlung für die Nutzung durch bestimmte Nutzergruppen
    - `ieLevel`: Angabe über die Metadaten, die auf IE-Ebene übernommen werden
    - `itemLevel`: Angabe über die Metadaten, die auf Item-Ebene übernommen werden
    - `archivalProcess`: Angabe über die Metadaten, die auf Ebene des (technischen) archivischen Prozesses übernommen werden
    - `representations`: Angabe über die Repräsentationen, die in diesem Profil wählbar sind
    - `other`: Zusätzliche Angaben außerhalb der bereits genannten Kategorien (optional)

Die Texte in `fullDesc` sollten in Form einer Liste von Strings vorliegen. Dabei wird jeder String als ein Paragraph interpretiert. Alle anderen Texte sollten einfache Strings sein (oder eine Zahl im Falle vom `no`).

### Default-Auswahl
Für den Fall, dass User keine eigene Auswahl tätigen, und um eine Standard-Auswahl zur Verfügung zu stellen, müssen Default-Einstellungen festgelegt werden. Diese betreffen
1. Das Default-Profil: Festgelegt mittels `standardProfile` in der `profile_conf.json` (Zahl, die den Index des Profils im Schlüssel `profileConfigs` angibt)
2. Die Default-AIP-Auswahl (profilabhängig): Festgelegt im jeweiligen `profileConfigs`-Objekt unter `defaultAIP`. Mögliche Werte:
    - "all": Alle AIPs
    - "latest": Nur das aktuellste AIP
    - "frame": Das Ursprungs- und das aktuellste AIP
3. Die Default-Bereitstellungsart (profilabhängig): Festgelegt im jeweiligen `profileConfigs`-Objekt unter `defaultDelivery`. Mögliche Werte:
    - "viewer": Nur ein ViewDIP wird erstellt. 
    - "download": Nur ein DIP wird erstellt.
    - "both": Sowohl ein DIP als auch ein ViewDIP wird erstellt.

### Profil-abhängige Einschränkung von Auswahlmöglichkeiten
Für manche Profile kann es sinnvoll sein, die Auswahlmöglichkeiten von AIPs oder Bereitstellungsarten einzuschränken. Ob eine Auswahl erlaubt ist (`true`) oder nicht (`false`) kann für jedes Profil unter `deliveryChoice` und `AIPChoice` angegeben werden.

Wenn eine Auswahl nicht erlaubt ist, so wird immer die Default-Auswahl getroffen. Es ist in diesem Falle ratsam, in der Infotext-Datei zu dem betreffenden Profil eine `repInfo` oder `deliveryInfo` zu hinterlegen, um dem User zu erklären, warum eine Auswahl nicht möglich ist (siehe dazu den Abschnitt zu [Profil-Infotexten](#infotexte-zu-profilen)).

### Allgemeine Infotexte
Um den Nutzer*innen eine informierte Entscheidung über die Wahl ihres DIP-Profils und ihrer AIPs sowie über die Benutzung des RequestViewers zu ermöglichen, sollen im RequestViewer Infoseiten angezeigt werden können. Die dort dargestellten Informationen müssen in einer entsprechenden JSON-Datei vorgehalten werden (hier `info.json`), deren Pfad in der `profile_conf.json` unter `info` vermerkt sein muss. Die Datei muss folgende Schlüssel enthalten:
- `representations`: Informationen darüber, was AIPs sind und was bei ihrer Auswahl zu beachten ist.
- `profiles`: Informationen darüber, was DIP-Profile sind und was bei Ihrer Auswahl zu beachten ist.
- `general`: Informationen über das Programm und seine Bedienung.

Jedem Schlüssel ist dabei ein Objekt mit folgendem Aufbau zugeordnet:
- `main`: Haupttitel der Infoseite
- `sections`: Einzelne Unterkapitel, jeweils wie folgt aufgebaut:
    - `sub`: Titel des Unterkapitels
    - `paragraphs`: Eine Liste von Strings, wobei jeder String genau einen Paragraphen repräsentiert.

### GUI-Texte
Die Texte der GUI stehen nicht im Code. Sie sind in einer eigenen Text-Datei hinterlegt (hier `guitexts.json`). Falls einzelne Label anders formuliert werden sollen, können sie hier geändert werden. Ebenfalls kann solchermaßen die gesamte GUI übersetzt werden. Die Anwendung unterstützt allerdings keine dynamische Internationalisierung, d.h. zur Runtime können keine anderen Sprachen ausgewählt werden. Die einmal geladene Datei mit den GUI-Texten gilt für die Dauer des Programms.

## Integration von Informationen aus einer Verzeichnungssoftware (VZE-Info)
Das dem Programm zugrundeliegende Konzept für DIP-Profile sieht vor, dass den DIPs grundlegende Informationen aus der archivischen Verzeichnung des angeforderten Archivales mitgegeben werden (Verzeichnungseinheit-Info = VZE-Info). Diese Informationen könnten z.B. durch einen manuellen Datenexport oder eine Schnittstelle zu der Verzeichnungssoftware abgefragt werden. Da jedoch nicht jede Archivsoftware einen Export auf Verzeichnungseinheitsebene anbietet und die Exportformate von Software zu Software unterschiedlich sind, wurde für den Prototypen darauf verzichtet, eine VZE-Integration zu realisieren.

Da sie im Konzept jedoch vorgesehen war, sind an entscheidenden Stellen im Programm bereits entsprechende Weichen gestellt worden. So kann manchen Methoden des `DIPRequestHandler`s z.B. eine VZE-Info übergeben werden und in der GUI kann ein FileSpinner für das AUswählen eines VZE-Exports. Teilweise müssen noch entsprechende Funktionen zur Verarbeitung eines solchen Exports implementiert werden. An den Stellen, wo die VZE bereits berücksichtigt wurde, wurde der entsprechende Code teils auskommentiert, um die Funktionsweise des aktuellen Prototypen nicht zu beeinträchtigen. Entsprechende Zeilen sind mit einem Inline-Comment markiert: `# VZE`

## Erzeugung von ViewDIPs
Das dem Programm zugrundeliegende Konzept für DIP-Profile sieht vor, dass eine Unterscheidung zwischen allgemeinen DIPs und anwendungsspezifischen DIPs vorgenommen wird. So soll bei jeder DIP-Anforderung ein allgemeines DIP generiert werden, welches auch zum Download oder Austausch von Informationen dient. Anwendungsspezifische DIPs wiederum sollen auf diesen allgemeinen DIPs aufbauen und sie für die Anzeige bzw. Bearbeitung in einem Programm vorbereiten.

Das ViewDIP, für das die Generierung im Prototypen bereits angelegt ist, ist so ein anwendungsspezifisches DIP. Es sollte dabei die Metadaten des DIPs an die Bedürfnisse des Viewers anpassen. Denkbar wäre zum Beispiel, dass der Viewer nur Schlüssel-Wert-Paare anzeigen, was ihn nutzbar für zahlreiche verschiedene Arten von Metadaten macht. Ein ViewDIP müsste dann die Daten aus dem DIP ebenfalls als Schlüssel-Wert-Paare enthalten.

Aus Zeitgründen, und da noch kein entsprechender Viewer für die generierten DIPs existiert, konnte die Generierung eines solchen ViewDIPs noch nicht vollständig umgesetzt werden. Aktuell haben die ViewDIPs denselben Aufbau wie die DIPs. Durch eine Überarbeitung der Klasse `ViewDIP` im Modul `drh.ip` kann eine solche Generierung implementiert werden. Insbesondere müsste hierfür auch eine Transformation der Daten mittels einer eigenen XSL-Datei und einer eigenen View-Config-Datei umgesetzt werden. 

## Nutzung des `drh` Moduls ohne das `rv` Modul
Das Programm bietet als Prototyp eine graphische Benutzeroberfläche an, die intern auf das `drh` Modul zugreift. Das `drh` Modul ist jedoch so konzipiert, dass es ohne das hier vorhandene `rv` Modul genutzt werden kann. Die öffentlichen Methoden des `DIPRequestHandler`s dienen dabei als Interface. So kann das Modul prinzipiell genutzt werden, um andere GUI-Applikationen vorzuschalten oder um ganz ohne GUI Daten über eine Programmierschnittstelle abzurufen. Entsprechende vorgelagerte Applikationen müssen lediglich den `DIPRequestHandler` importieren, initialisieren und von ihm Informationen abrufen.
Durch diese offene Konzeption soll die Nachnutzung des Programms vereinfacht werden.

## Dependencies
Das Programm ist in **Python** verfasst und benötigt darum einen Python Interpreter, um zu laufen.

Das Programm arbeitet mit folgenden **Paketen**, die nicht in der Python Standard-Library enthalten sind:
* [`saxonpy`](https://pypi.org/project/saxonpy/): Ein präkompiliertes Package für SaxonC, den Python XML Prozessor von Saxonica. GitHub Repository: [tennom/saxonpy](https://github.com/tennom/saxonpy)
* [`PySide6`](https://pypi.org/project/PySide6/): Das offizielle Python Modul für das GUI-Framework [Qt for Python](https://www.qt.io/qt-for-python).

Außerdem sind u.a. folgende Module aus der **Python-Standard-Library** für zentrale Funktionen des Programms verwendet worden:
* `tempfile` zum Verwalten temporärer Ordner für das Programm
* `tarfile` zum entpacken und packen von TAR-Dateien
* `json` zum Laden und Speichern von config-Dateien
* `lxml.etree` und `xml.etree` zum Parsen von XML 

## Noch zu ergänzende Dateien
Um mögliche Lizenz- oder Urheberrechtskonflikte zu vermeiden, wurden einige für das Funktionieren des Programms notwendige Dateien nicht dem öffentlichen Repository beigegeben. Diese sind:
* XSD-Dateien für die Mitgabe der Schemata in den fertigen DIPs. Hier müssten folgende Placeholder ersetzt werden, die jeweils als Dateinamen den Namen tragen müssen, der in der `profile_conf.json` für die XSD-Datei angegeben ist:
    * config/DIP/placeholder.xsd
    * config/DIP/profiles/p1/DIP-P1_placeholder.xsd
    * config/DIP/profiles/p2/DIP-P2_placeholder.xsd
    * config/DIP/profiles/p3/DIP-P3_placeholder.xsd
    * config/DIP/profiles/p4/DIP-P4_placeholder.xsd
* SVG-Dateien für die GUI, vgl. den Abschnitt zum Ordner `svg`
