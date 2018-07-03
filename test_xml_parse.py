# pip install lxml

from lxml import etree
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

import csv

mytuple = ('thing1', 'thing2', 'thing3')

with open('vital_records_dgs_index.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Title'] + ['Date'] + ['dgs Code'])
    writer.writerows([mytuple])

