import os
import csv

filepath = r'C:\Users\adean\Desktop\ongoing'

for root, dirs, files in os.walk(filepath):
    print(root)
    print(dirs)
    print(files)

with open('filenames_list.csv', 'w', newline='') as csvfile:
    new_csv_writer = csv.writer(csvfile, delimiter=',')
    for file in files:
        new_csv_writer.writerow([file])
