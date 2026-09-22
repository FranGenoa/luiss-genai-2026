"""Build the classroom CSV for Esercizio 3 from the public Wine Enthusiast dataset.

Source: TidyTuesday 2019-05-28 mirror of the Kaggle "Wine Reviews" dataset
https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2019/2019-05-28/winemag-data-130k-v2.csv

Run once to regenerate data/vini_italiani_recensioni.csv
"""
import os
import re

import pandas as pd

SRC = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2019/2019-05-28/winemag-data-130k-v2.csv"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vini_italiani_recensioni.csv")
TARGET_ROWS = 1500
SEED = 2026

PROVINCE_IT = {
    "Tuscany": "Toscana",
    "Piedmont": "Piemonte",
    "Veneto": "Veneto",
    "Northeastern Italy": "Italia nord-orientale",
    "Sicily & Sardinia": "Sicilia e Sardegna",
    "Southern Italy": "Italia meridionale",
    "Central Italy": "Italia centrale",
    "Lombardy": "Lombardia",
    "Italy Other": "Altre zone d'Italia",
    "Northwestern Italy": "Italia nord-occidentale",
}


def vintage(title):
    years = re.findall(r"(19[5-9]\d|20[0-2]\d)", str(title))
    return int(years[0]) if years else pd.NA


def score_band(p):
    if p >= 95:
        return "95-100 Eccezionale"
    if p >= 90:
        return "90-94 Ottimo"
    if p >= 87:
        return "87-89 Molto buono"
    return "80-86 Buono"


def price_band(p):
    if p < 15:
        return "1. Sotto 15"
    if p < 25:
        return "2. Da 15 a 24"
    if p < 40:
        return "3. Da 25 a 39"
    if p < 75:
        return "4. Da 40 a 74"
    return "5. 75 e oltre"


def main():
    raw = pd.read_csv(SRC)
    df = raw[raw["country"] == "Italy"].copy()
    df = df.dropna(subset=["price", "points", "province", "variety", "winery"])
    df = df.drop_duplicates(subset=["title", "winery", "price"])

    df["anno"] = df["title"].map(vintage)
    df = df.dropna(subset=["anno"])
    df = df[(df["anno"] >= 2000) & (df["anno"] <= 2017)]

    # Stratified sample by province so every macro-area stays represented.
    frac = TARGET_ROWS / len(df)
    parts = []
    for prov, grp in df.groupby("province"):
        n = max(12, round(len(grp) * frac))
        n = min(n, len(grp))
        parts.append(grp.sample(n=n, random_state=SEED))
    sample = pd.concat(parts)
    if len(sample) > TARGET_ROWS:
        sample = sample.sample(n=TARGET_ROWS, random_state=SEED)

    out = pd.DataFrame({
        "id_recensione": range(1, len(sample) + 1),
        "nome_vino": sample["title"].str.strip().values,
        "cantina": sample["winery"].str.strip().values,
        "regione": sample["province"].map(PROVINCE_IT).fillna(sample["province"]).values,
        "denominazione": sample["region_1"].fillna("Non indicata").str.strip().values,
        "vitigno": sample["variety"].str.strip().values,
        "annata": sample["anno"].astype(int).values,
        "punteggio": sample["points"].astype(int).values,
        "fascia_punteggio": sample["points"].map(score_band).values,
        "prezzo_usd": sample["price"].astype(float).values,
        "fascia_prezzo_usd": sample["price"].map(price_band).values,
        "recensore": sample["taster_name"].fillna("Non indicato").str.strip().values,
        "nota_degustazione": sample["description"].str.replace(r"\s+", " ", regex=True).str.strip().str.slice(0, 260).values,
    })

    out["punti_per_dollaro"] = (out["punteggio"] / out["prezzo_usd"]).round(2)
    out = out.sort_values(["regione", "cantina", "annata"]).reset_index(drop=True)
    out["id_recensione"] = range(1, len(out) + 1)

    # Normalise typographic characters so the file opens cleanly in Excel everywhere.
    for col in out.select_dtypes(include="object").columns:
        out[col] = (out[col]
                    .str.replace("\u2019", "'", regex=False)
                    .str.replace("\u2018", "'", regex=False)
                    .str.replace("\u201c", '"', regex=False)
                    .str.replace("\u201d", '"', regex=False)
                    .str.replace("\u2013", "-", regex=False)
                    .str.replace("\u2014", "-", regex=False))

    # utf-8-sig: Excel on Windows needs the BOM to render accented characters.
    out.to_csv(OUT, index=False, encoding="utf-8-sig")

    print(f"Rows: {len(out)}  Size: {os.path.getsize(OUT)/1024:.0f} KB")
    print(out["regione"].value_counts())


if __name__ == "__main__":
    main()
