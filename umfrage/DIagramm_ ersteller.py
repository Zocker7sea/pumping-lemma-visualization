import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==================================================
# Pfade
# ==================================================

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "diagrams"
OUTPUT_DIR.mkdir(exist_ok=True)

# ==================================================
# CSV laden
# ==================================================

csv_files = list(DATA_DIR.glob("*.csv"))
if not csv_files:
    raise FileNotFoundError("Keine CSV-Datei im data-Ordner gefunden.")

DATA_PATH = csv_files[0]
df = pd.read_csv(DATA_PATH, encoding="utf-16", sep="\t")

# nur abgeschlossene Interviews
df = df[df["FINISHED"] == 1]

# ==================================================
# Relevante Spalten
# ==================================================

RELEVANT_COLUMNS = [
    "CASE",
    "A102",
    "A103",
    "A106",
    "A201",
    "A202",
    "A203",
    "A204",
    "A205",
    "A208",
    "A301",
    "A302_01",
    "A303_01"
]

df = df[[c for c in RELEVANT_COLUMNS if c in df.columns]]

# ==================================================
# Gruppen
# ==================================================

groups = {
    "mixed": df,
    "informatik": df[df["A102"] == 1],
    "nicht_informatik": df[df["A102"] == 2]
}

# ==================================================
# Sprach-Mapping
# ==================================================

LANGUAGE_MAP = {
    1: "aⁿbⁿ",
    2: "gerade Anzahl von a",
    3: "(ab)*",
    4: "aⁿbⁿcⁿ",
    5: "Palindrome",
    6: "a*",
    7: "aⁿbᵐaⁿ",
    8: "aᵏ²",
    9: "aⁿbᵐ mit n > m"
}

# ==================================================
# Skalen
# ==================================================

LIKERT_LABELS = [
    "stimme gar nicht zu",
    "stimme eher nicht zu",
    "weder noch",
    "stimme eher zu",
    "stimme voll zu"
]

FAMILIARITY_LABELS = [
    "gar nicht vertraut",
    "eher nicht vertraut",
    "teilweise vertraut",
    "gut vertraut",
    "sehr gut vertraut"
]

# ==================================================
# A102 – TI besucht
# ==================================================

plt.figure()
df["A102"].value_counts().reindex([1, 2], fill_value=0).plot(kind="bar")
plt.title("Haben Sie bereits ein Modul zur Theoretischen Informatik besucht?")
plt.xlabel("Antwort")
plt.ylabel("Anzahl der Teilnehmenden")
plt.xticks([0, 1], ["Ja", "Nein"], rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "a102_ti_modul_belegt.png", dpi=300)
plt.close()

# ==================================================
# Dateinamen-Mapping für bessere Übersicht
# ==================================================

FILENAME_MAP = {
    "A103": "a103_vertrautheit_mit_lemma",
    "A106": "a106_startseite_verstaendlich",
    "A201": "a201_sprachauswahl_verstaendlich",
    "A202": "a202_zerlegung_verstaendlich",
    "A203": "a203_pumping_verstaendlich",
    "A204": "a204_rueckmeldung_sprachzugehoerigkeit",
    "A205": "a205_verstaendnis_gefoerdert",
    "A301": "a301_gesamtbenutzerfreundlichkeit"
}

LIKERT_QUESTIONS = {
    "A106": "Startseite verständlich",
    "A201": "Sprachauswahl verständlich",
    "A202": "Zerlegung verständlich",
    "A203": "Pumping verständlich",
    "A204": "Rückmeldung korrekt",
    "A205": "Verständnis gefördert",
    "A301": "Gesamtbenutzerfreundlichkeit"
}

# ==================================================
# Verarbeitung pro Gruppe
# ==================================================

for group_name, group_df in groups.items():

    group_dir = OUTPUT_DIR / group_name
    group_dir.mkdir(exist_ok=True)

    # Excel speichern
    group_df.to_excel(group_dir / "daten.xlsx", index=False)

    # ---------- A103 ----------
    fam = group_df["A103"].replace(-9, pd.NA)
    counts = fam.value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)

    plt.figure()
    counts.plot(kind="bar")
    plt.title("Wie vertraut sind Sie mit dem Pumping-Lemma?")
    plt.ylabel("Anzahl der Teilnehmenden")
    plt.xticks(range(5), FAMILIARITY_LABELS, rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(group_dir / f"{FILENAME_MAP['A103']}.png", dpi=300)
    plt.close()

    # ---------- Likert ----------
    for col, title in LIKERT_QUESTIONS.items():

        data = group_df[col].replace(-9, pd.NA)
        counts = data.value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)

        plt.figure()
        counts.plot(kind="bar")
        plt.title(title)
        plt.ylabel("Anzahl der Teilnehmenden")
        plt.xticks(range(5), LIKERT_LABELS, rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(group_dir / f"{FILENAME_MAP[col]}.png", dpi=300)
        plt.close()

    # ---------- Sprache ----------
    if "A208" in group_df.columns:
        mapped = group_df["A208"].map(LANGUAGE_MAP)

        plt.figure()
        mapped.value_counts().plot(kind="bar")
        plt.title("Welche Sprache wurde getestet?")
        plt.ylabel("Anzahl der Teilnehmenden")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.savefig(group_dir / "a208_gewaehlte_sprache.png", dpi=300)
        plt.close()

    # ---------- Freitext strukturiert ----------
    with open(group_dir / "freitext.txt", "w", encoding="utf-8") as f:

        for _, row in group_df.iterrows():

            if pd.isna(row.get("A302_01")) and pd.isna(row.get("A303_01")):
                continue

            f.write("\n" + "=" * 70 + "\n")
            f.write(f"CASE: {row['CASE']}\n")
            f.write("-" * 70 + "\n")

            if pd.notna(row.get("A302_01")):
                f.write("Frage A302:\n")
                f.write(str(row["A302_01"]).strip() + "\n")
                f.write("-" * 70 + "\n")

            if pd.notna(row.get("A303_01")):
                f.write("Frage A303:\n")
                f.write(str(row["A303_01"]).strip() + "\n")

            f.write("=" * 70 + "\n")

print("Alle Diagramme und strukturierten Freitexte wurden erstellt.")