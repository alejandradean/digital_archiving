import csv
f = open('vol_1_test.csv')
csv_f = csv.reader(f)
data = []

for row in csv_f:
    data.append(row)
f.close()

def convert_row(row):
    return """<vitalRecord>
    <filename>%s</filename>
    <recordGroup>%s</recordGroup>
    <series>%s</series>
    <fileUnit>%s</fileUnit>
    <item>%s</item>
    <title>%s</title>
    <description>%s</description>
    <coverage>%s</coverage>
    <date>%s</date>
    <vitalsYear>%s</vitalsYear>
    <vitalsVolume>%s</vitalsVolume>
    <vitalsPage>%s</vitalsPage>
</vitalRecord>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])

new_xml_file = open('vol_1_test.xml', 'w')
new_xml_file.write('\n'.join([convert_row(row) for row in data[1:]]))

new_xml_file.close()
    
    
    
