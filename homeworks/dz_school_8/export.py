import csv
from logg import logging

def save_csv(file_name):
    logging.info(f"Export in csv format: {file_name}.csv")

    with open(f'{file_name}.csv', 'w', encoding="utf-8", newline="") as file_w, \
            open('telephone_book.csv', encoding="utf-8") as file_r:
        all_data = csv.DictReader(file_r)
        fieldnames = ["id", "name", "surname", "phone", "description"]
        writer = csv.DictWriter(file_w, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)
        print(f"{file_name}.csv file saved\n")