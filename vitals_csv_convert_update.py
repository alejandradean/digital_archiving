import csv
import subprocess

print('Enter volume number (ex: 048): ')
vol_num = input()

csv_file = 'vol_' + str(vol_num) + '_1916_deaths.csv'
output_xml_file = 'vol_' + str(vol_num) + '_1916_deaths.xml'

f = open(csv_file)
csv_f = csv.reader(f)

all_rows = list(csv_f)

header_row = all_rows[0]
data_rows = all_rows[1:]

f.close()

def convert_row(row):
    return """<record>
    <filename>%s</filename>
    <recordGroup>%s</recordGroup>
    <series>%s</series>
    <fileUnit>%s</fileUnit>
    <item>%s</item>
    <title>%s</title>
    <description>%s</description>
    <coverage>%s</coverage>
    <date>%s</date>
</record>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

new_xml_file = open(output_xml_file, 'w')
new_xml_file.write('<vitalRecord>')
new_xml_file.write('\n')

for row in data_rows:
    xml_record = convert_row(row)
    new_xml_file.write(xml_record)
    new_xml_file.write('\n')

new_xml_file.write('</vitalRecord>')
new_xml_file.close()

print('Enter volume municipality range with _underscores_ (ex: holyoke_to_hudson): ')
municipalities = input()

saxon_source = '-s:C:\\Users\\adean\\Desktop\\' + str(output_xml_file)
saxon_output = '-o:A:\\HS6.07_1411\\Vital_records_ready_for_ingest\\Deaths\\1916\\vol_' + str(vol_num) + '_1916_deaths_' + str(municipalities) + '\\tiffs\\output.xml'

subprocess.run(['java', '-jar', 'C:\\Program Files (x86)\\saxon9he.jar', saxon_source, '-xsl:C:\\Users\\adean\\Desktop\\hs6_07_1411.xsl', saxon_output], shell=True)
