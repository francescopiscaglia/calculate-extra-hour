from datetime import date


def get_previous_hours():
    """
    Reads and returns a list of previously stored hours from the 'ore_extra.txt' file.
    Returns:
        list: A list of strings, each representing a line (hour entry) from the file.
              Returns an empty list if the file does not exist or an error occurs during reading.
    Exceptions:
        Handles FileNotFoundError by returning an empty list.
        Handles other exceptions by printing an error message and returning an empty list.
    """
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
    """
    Appends today's overtime hours to the records, writes all non-zero records to 'ore_extra.txt', and calculates the total sum of overtime hours.
    Args:
        records (list): A list of strings, each representing a record in the format 'YYYY-MM-DD: hours'.
    Returns:
        int: The total sum of overtime hours from all records (excluding records with 0 hours).
        Exception: Returns the exception object if an error occurs during execution.
    Side Effects:
        - Prompts the user to input today's overtime hours.
        - Appends a new record for today to the records list.
        - Writes all non-zero hour records to 'ore_extra.txt'.
    """
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
