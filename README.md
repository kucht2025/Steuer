# Beleg Assistent Lohnsteuer

Dieses Projekt implementiert einen einfachen Assistenten, der Belege im Zusammenhang mit Gesundheitsausgaben sammelt und auswertet. Nach dem Sammeln lassen sich die Belege analysieren und in eine Excel-Datei exportieren. So lassen sich zum Beispiel Zuzahlungen oder Apothekenrechnungen bequem für die Steuererklärung aufbereiten.

## Funktionen
- **Sammelmodus**: Belege werden gesammelt und in einem Ordner gespeichert.
- **Analysemodus**: Nach dem Befehl `start` werden alle Belege kategorisiert und in einer Excel-Tabelle zusammengefasst.
- **Einfache Kategorisierung**: Erste Heuristiken ordnen Ausgaben Kategorien wie "Apotheke" oder "Krankenhaus" zu.

## Einrichtung
1. Python 3.10 oder neuer installieren.
2. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

## Nutzung
Belege können mit dem Befehl `collect` hinzugefügt werden. Die Analyse startet mit `start`.
```bash
# Beleg sammeln
python src/main.py collect /pfad/zum/beleg.pdf

# Analyse starten
python src/main.py start
```
Die Ergebnisse liegen anschließend im Ordner `outputs/`.

### Grafische Benutzeroberfläche
Alternativ kann eine einfache grafische Oberfläche gestartet werden:
```bash
python src/gui.py
```
Über die Buttons lassen sich PDF-Belege auswählen und die Analyse starten.

## Projektstruktur
- `src/` – Quellcode der Anwendung
- `receipts/` – abgelegte Belege
- `outputs/` – erzeugte Excel-Dateien

## Beitrag leisten
Anregungen und Pull Requests sind willkommen. Details stehen in [CONTRIBUTING.md](CONTRIBUTING.md).

## Lizenz
Dieses Projekt steht unter der [MIT-Lizenz](LICENSE).
