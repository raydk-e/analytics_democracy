#!/usr/bin/env python3
import csv

source_file = 'personal_finance.csv'
destination_file = 'finance_report.csv'

try:
    with open(source_file, "r", newline='') as input_file,\
         open(destination_file, "w", newline='') as output_file:
        
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        for r in reader:
            writer.writerows(r)
    print(f"file copied from {source_file} to {destination_file}")

except FileNotFoundError:
    print(f"the {source_file} is not available")
except Exception as e:
    print(f"An error occurred: {e}")



