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

            if gender.lower() == "m":
                gender = "sameček"
            elif gender.lower() == "z":
                gender = "samička"

            print(f"{gender} morčete jménem: {name}\n- váží: {weight} g\n- datum narození: {date}")
            print(f"- cena se slevou 10 %: {(price * Decimal('0.9'))} Kč")

        except ValueError:
            print(f"Invalid date format for line: {line.strip()}")
        