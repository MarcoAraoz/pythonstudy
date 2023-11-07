import csv

with open(".csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0