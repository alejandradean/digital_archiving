# INCOMPLETE SCRIPT
import os 
import csv
import xml.etree.ElementTree as ET

filepath = input('Enter filepath: ')

for root, dirs, files in os.walk(filepath):
    
    # navigate to each folder 4 levels down 
    for dir in dirs:
        if len(os.dirname(dir)) > 14:
        os.chdir
        tree = ET.parse('operationalMetadata.xml')
        root = tree.getroot()

        for folder in root.findall('folder'):
            dgs = folder.get('dgs')
            title = folder.find('volume-designation').text
            date = folder.find('record-dates').text
            print(dgs, title, date)

        vitaltuple = (title, date, dgs)

        with open('vital_records_dgs_index.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Title'] + ['Date'] + ['dgs Code'])
            writer.writerows([vitaltuple])
   else:
        
