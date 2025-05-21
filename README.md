Overtime Hours Tracker
======================

This is a simple Python script for tracking daily overtime hours and storing them in a plain text file (`ore_extra.txt`).

Overview
--------
The script performs the following actions:
- Reads previously recorded overtime hours from `ore_extra.txt`
- Prompts the user to input today’s overtime hours
- Appends the new entry to the list of records (only if the value is greater than zero)
- Rewrites the file with all valid entries
- Calculates and prints the total amount of overtime hours recorded

How It Works
------------
1. When executed, the script first attempts to read existing entries from the file `ore_extra.txt`.
2. It asks the user to input the number of overtime hours worked today.
3. It appends today's entry (formatted as `YYYY-MM-DD: hours`) to the list.
4. It writes all records back to the file, ignoring entries with 0 hours.
5. Finally, it prints the full list and the total sum of overtime hours.

File Format
-----------
The file `ore_extra.txt` contains one record per line, using the following format:

    YYYY-MM-DD: hours

Example:

    2025-05-20: 2
    2025-05-21: 1

Usage
-----
Run the script using Python 3:

    python overtime_tracker.py

You will be prompted to enter the number of hours worked today.

Error Handling
--------------
- If the file `ore_extra.txt` does not exist, the script will handle it gracefully and start a new one.
- Non-numeric or invalid input will raise an error message.
- Any other exception during file reading or writing will be printed to the console.

Requirements
------------
- Python 3.x

No external libraries are required.

Disclaimer
----------
This is a local tool meant for personal use only. All data is stored in plain text format and not backed up automatically.

License
-------
This project is released under the MIT License.
