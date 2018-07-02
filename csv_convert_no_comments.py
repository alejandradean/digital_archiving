import csv

f = open('mydata.csv')
csv_f = csv.reader(f)

all_rows = list(csv_f)

header_row = all_rows[0]
data_rows = all_rows[1:]

f.close()

def convert_row(row):
    return """<record>
    <field>%s</filename>
    <recordGroup>%s</recordGroup>
    <series>%s</series>
    <fileUnit>%s</fileUnit>
    <item>%s</item>
    <title>%s</title>
    <description>%s</description>
    <coverage>%s</coverage>
    <date>%s</date>
</record>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

new_xml_file = open('converted.xml', 'w')

for row in data_rows:
    xml_record = convert_row(row)
    new_xml_file.write(xml_record)
    new_xml_file.write('\n')

new_xml_file.close()