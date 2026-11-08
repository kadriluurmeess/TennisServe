"""Laadib TennisMyLife'i WTA 2018–2023 andmed kohalikku data/raw kausta."""

import csv
import io
from pathlib import Path
from urllib.request import urlopen


YEARS = range(2018, 2024)
DATA_DIR = Path(__file__).resolve().parent / "data" / "raw"
BASE_URL = "https://stats.tennismylife.org/data"
REQUIRED_COLUMNS = {
    "tourney_date", "surface", "winner_name", "loser_name",
    "w_svpt", "w_1stIn", "w_1stWon", "w_2ndWon",
    "l_svpt", "l_1stIn", "l_1stWon", "l_2ndWon",
}


def inspect_csv(content):
    """Kontrollib CSV struktuuri ning tagastab veerunimed ja ridade arvu."""
    reader = csv.reader(io.StringIO(content.decode("utf-8-sig"), newline=""))
    columns = next(reader, [])
    if not REQUIRED_COLUMNS.issubset(columns):
        raise ValueError("Fail ei sisalda oodatud WTA mänguandmete veerge.")
    row_count = 0
    for row in reader:
        if not row:
            continue
        if len(row) != len(columns):
            raise ValueError(f"CSV real {reader.line_num} on vale arv välju.")
        row_count += 1
    if row_count == 0:
        raise ValueError("CSV ei sisalda ühtegi mängu.")
    return columns, row_count


def download_data():
    """Laadib puuduvad aastafailid alla; olemasolevad failid säilitab."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    paths = []
    expected_columns = None
    total_rows = 0

    for year in YEARS:
        path = DATA_DIR / f"{year}_wta.csv"
        exists = path.exists()
        if exists:
            content = path.read_bytes()
        else:
            with urlopen(f"{BASE_URL}/{path.name}", timeout=60) as response:
                content = response.read()

        columns, row_count = inspect_csv(content)
        if expected_columns is None:
            expected_columns = columns
        elif columns != expected_columns:
            raise ValueError(f"Faili {path.name} veerud erinevad teistest aastatest.")

        if not exists:
            temporary = path.with_suffix(".csv.part")
            temporary.write_bytes(content)
            temporary.replace(path)

        status = "olemas" if exists else "alla laaditud"
        print(f"{path.name}: {row_count} rida, {len(columns)} veergu ({status})")
        total_rows += row_count
        paths.append(path)

    print(f"Kokku: {total_rows} rida ja {len(expected_columns)} veergu.")
    return paths


if __name__ == "__main__":
    download_data()
