import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from main import collect, analyze, RECEIPTS_DIR


def update_count(label_var: tk.StringVar) -> None:
    count = len(list(RECEIPTS_DIR.glob("*.pdf"))) if RECEIPTS_DIR.exists() else 0
    label_var.set(f"Gesammelte Belege: {count}")


def add_receipt(label_var: tk.StringVar) -> None:
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        collect(file_path)
        update_count(label_var)


def start_analysis() -> None:
    analyze()
    messagebox.showinfo("Fertig", "Analyse abgeschlossen.")


def main() -> None:
    root = tk.Tk()
    root.title("Beleg Assistent")

    label_var = tk.StringVar()
    label = tk.Label(root, textvariable=label_var)
    label.pack(pady=10)

    update_count(label_var)

    add_btn = tk.Button(root, text="Beleg hinzufügen", command=lambda: add_receipt(label_var))
    add_btn.pack(fill="x", padx=20, pady=5)

    start_btn = tk.Button(root, text="Analyse starten", command=start_analysis)
    start_btn.pack(fill="x", padx=20, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
