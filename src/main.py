import argparse
import shutil
from pathlib import Path

import pandas as pd
from pdfminer.high_level import extract_text

RECEIPTS_DIR = Path(__file__).resolve().parent.parent / "receipts"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "outputs"

CATEGORIES = {
    "physiotherapie": "Zuzahlungen für Physiotherapie",
    "rezept": "Rezeptgebühren",
    "apotheke": "Apothekeneinkäufe",
    "zahnarzt": "Zahnarztkosten",
    "heilpraktiker": "Heilpraktikerleistungen",
    "krankenhaus": "Krankenhauszuzahlungen",
    "hilfsmittel": "Medizinische Hilfsmittel",
}

def collect(file_path: str) -> None:
    """Speichert einen Beleg im Receipts-Ordner."""
    RECEIPTS_DIR.mkdir(exist_ok=True)
    src = Path(file_path)
    if not src.is_file():
        print("Datei nicht gefunden:", file_path)
        return
    dst = RECEIPTS_DIR / src.name
    shutil.copy(src, dst)
    print(f"Beleg {src.name} gesammelt.")

def analyze() -> None:
    """Analysiert alle gesammelten Belege und erstellt eine Excel-Datei."""
    if not RECEIPTS_DIR.exists():
        print("Keine Belege zum Analysieren gefunden.")
        return

    OUTPUT_DIR.mkdir(exist_ok=True)
    records = []
    for pdf in RECEIPTS_DIR.glob("*.pdf"):
        text = extract_text(pdf)
        category = "Sonstige"
        for keyword, name in CATEGORIES.items():
            if keyword.lower() in text.lower():
                category = name
                break
        records.append({
            "Datei": pdf.name,
            "Kategorie": category,
        })

    if not records:
        print("Keine PDF-Belege gefunden.")
        return

    df = pd.DataFrame(records)
    output_file = OUTPUT_DIR / "auswertung.xlsx"
    df.to_excel(output_file, index=False)
    print(f"Auswertung gespeichert unter {output_file}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Beleg Assistent Lohnsteuer")
    subparsers = parser.add_subparsers(dest="command")

    collect_parser = subparsers.add_parser("collect", help="Beleg sammeln")
    collect_parser.add_argument("file", help="Pfad zum Beleg (PDF)")

    subparsers.add_parser("start", help="Analyse starten")

    args = parser.parse_args()

    if args.command == "collect":
        collect(args.file)
    elif args.command == "start":
        analyze()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
