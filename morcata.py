from decimal import Decimal
from datetime import datetime


with open("data/morcata.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

    for line in lines:
        parts = line.strip().split(";")
        name = parts[0].strip()
        weight = int(parts[1].strip())
        date_str = parts[2].strip()
        price = Decimal(parts[3].strip())
        gender = parts[4].strip()
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            print(f"Jméno: {name}, Hmotnost: {weight}, Cena: {price}, Datum narození: {date}, Pohlaví: {gender}")
        except ValueError:
            print(f"Invalid date format for line: {line.strip()}")
        