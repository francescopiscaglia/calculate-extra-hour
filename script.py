from datetime import date


def get_previous_hours():
    hours = []
    try:
        with open("ore_extra.txt", "r") as file:
            for line in file:
                clean_line = line.strip()
                if clean_line:
                    hours.append(clean_line)

        return hours
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Errore durante la lettura: {e}")
        return []


def write_all_records_and_calc_sum(records: list):
    sum = 0
    try:
        today_hours = int(
            input("Inserisci quante ore hai fatto oggi di straordinario: ")
        )

        today_date = date.today()
        new_record = f"{today_date}: {today_hours}"
        records.append(new_record)

        with open("ore_extra.txt", "w") as file:
            for line in records:
                hour = int(line.split(": ")[1])
                if hour != 0:
                    file.write(line + "\n")
                    sum += hour

        return sum

    except Exception as e:
        return e


previous_hours = get_previous_hours()
print("Ore precedenti:", previous_hours)
total_hours = write_all_records_and_calc_sum(previous_hours)
print("Totale ore straordinario:", total_hours)
