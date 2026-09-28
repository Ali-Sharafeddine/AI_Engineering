import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("data.json")


def load_data():
    if not DATA_FILE.exists():
        return {"books": [], "members": []}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ValueError("The data file contains invalid JSON.") from exc

    if not isinstance(data, dict):
        raise ValueError("The data structure is invalid.")

    data.setdefault("books", [])
    data.setdefault("members", [])
    return data


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        file.write("\n")
