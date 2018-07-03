# INCOMPLETE SCRIPT
# pip install lxml
import os 
import csv
from lxml import etree

filepath = input('Enter filepath: ')

for root, dirs, files in os.walk(filepath):
    
    # navigate to each folder 4 levels down 
    for dir in dirs:
        if len(os.dirpath(dir)) > 14:
        os.chdir
        doc = etree.parse(operationalMetadata.xml)

        # <folder> dgs attribute
        folderElem = doc.find('folder')
         print(folderElem.get('dgs'))
         dgs = folderElem.get('dgs')

         # <volume-designation> text
         volDesElem = doc.find('volume-designation')
         print(volDesElem.text)
         title = volDesElem.text

         # <record-dates> text
         recordDatesElem = doc.find('record-dates')
         print(recordDatesElem.text)
         date = recordDatesElem.text

vitaltuple = (title, date, dgs)

mytuple = ('thing1', 'thing2', 'thing3')

with open('vital_records_dgs_index.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Title'] + ['Date'] + ['dgs Code'])
    writer.writerows([mytuple])
