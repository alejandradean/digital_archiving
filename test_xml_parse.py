import os
import csv
import xml.etree.ElementTree as ET

for root, dirs, files in os.walk('test_parse'):
    for filename in files:
        if filename == 'operationalMetadata.xml':

            filepath = os.path.join(root, filename)
            tree = ET.parse(filepath)
            root = tree.getroot()

            for folder in root.findall('folder'):

                dgs = folder.get('dgs')
                title = folder.find('volume-designation').text
                date = folder.find('record-dates').text

            vitaltuple = (title, date, dgs)
            
            with open(r'C:\Users\adean\Desktop\vital_records_dgs_index.csv', 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerows([vitaltuple])
