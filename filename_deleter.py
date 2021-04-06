#!/usr/bin/env python3

# script to delete files based on a list created from the first column of a csv file that has a column header of "filenames" ; this python script needs to be saved in the same directory as the csv file and this current working directory needs to have a folder named "Images" that contains the [image] files to be deleted. 

import csv
import os

input_csv = input("Enter your csv filename: ")

with open(input_csv, newline='', encoding='utf-8-sig') as csv_file:
# included the encoding parameter with value "utf-8-sig" because the Byte Order Mark (BOM) character ("\ufeff") was being read at the beginning of the csv file. The csv module documentation indicates that setting the encoding parameter to utf-8-sig will remove this character when decoding the file.
    reader = csv.DictReader(csv_file, delimiter=',')
    list_of_filenames = []
    for row in reader:
        list_of_filenames.append(row['filenames'])

root_path = os.path.abspath(os.getcwd()) + '/Images'
# uses os.getcwd() method to return current working directory
# appends 'Images' folder to path, which is then normalized through os.path.abspath as a string and is assigned to the root_path variable

for root, dirs, files in os.walk('Images'):
    for filename in list_of_filenames:
        file_path = os.path.join(root_path, filename)
        os.remove(file_path)

print("Files deleted:")
for filename in list_of_filenames:
    print(filename)