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
# Relevante Spalten (alles, was du später brauchst)
# ==================================================

RELEVANT_COLUMNS = [
    "CASE",
    "A102",  # TI besucht
    "A103",  # Vertrautheit
    "A106",  # Startseite
    "A201",  # Sprachauswahl
    "A202",  # Zerlegung
    "A203",  # Pumpen
    "A204",  # Rückmeldung
    "A205",  # Verständnis
    "A208",  # Sprache
    "A301",  # Gesamtbewertung
    "A302_01",  # Freitext
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
# A102 – TI besucht (nur Diagramm)
# ==================================================

plt.figure()
df["A102"].value_counts().reindex([1, 2], fill_value=0).plot(kind="bar")
plt.title("Haben Sie bereits ein Modul zur Theoretischen Informatik besucht?")
plt.xlabel("Antwort")
plt.ylabel("Anzahl der Teilnehmenden")
plt.xticks([0, 1], ["Ja", "Nein"], rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "A102_ti_besucht.png", dpi=300)
plt.close()

# ==================================================
# Diagramme + CSV pro Gruppe
# ==================================================

LIKERT_QUESTIONS = {
    "A106": "Startseite verständlich",
    "A201": "Sprachauswahl verständlich",
    "A202": "Zerlegung verständlich",
    "A203": "Pumping verständlich",
    "A204": "Rückmeldung korrekt",
    "A205": "Verständnis gefördert",
    "A301": "Gesamtbenutzerfreundlichkeit"
}

for group_name, group_df in groups.items():

    group_dir = OUTPUT_DIR / group_name
    group_dir.mkdir(exist_ok=True)

    # ---------- Gesamt-CSV ----------
    group_df.to_excel(group_dir / "daten.xlsx", index=False)

    # ---------- A103 Vertrautheit ----------
    fam = group_df["A103"].replace(-9, pd.NA)
    counts = fam.value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)

    plt.figure()
    counts.plot(kind="bar")
    plt.title("Wie vertraut sind Sie mit dem Pumping-Lemma?")
    plt.ylabel("Anzahl der Teilnehmenden")
    plt.xticks(range(5), FAMILIARITY_LABELS, rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(group_dir / "A103_vertrautheit.png", dpi=300)
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
        plt.savefig(group_dir / f"{col}.png", dpi=300)
        plt.close()

    # ---------- Sprache ----------
    if "A208" in group_df.columns:
        mapped = group_df["A208"].map(LANGUAGE_MAP)

        plt.figure()
        mapped.value_counts().plot(kind="bar")
        plt.title("Welche Sprache wurde in der Anwendung getestet?")
        plt.ylabel("Anzahl der Teilnehmenden")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.savefig(group_dir / "A208_sprache.png", dpi=300)
        plt.close()

    # ---------- Freitext ----------
    texts = []
    for col in ["A302_01", "A303_01"]:
        if col in group_df.columns:
            texts.extend(group_df[col].dropna().astype(str).tolist())

    with open(group_dir / "freitext.txt", "w", encoding="utf-8") as f:
        for t in texts:
            f.write(t.strip() + "\n\n")

print("Alle Diagramme wurden erstellt.")
