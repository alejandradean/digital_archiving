# the csv module contains a library of code specifically written to handle data in .csvs
import csv

# the open() function, a built-in Python function, opens my .csv file, assigning it to variable "f"
# note: the path is relative, meaning the .csv is in the same directory as this script  
f = open('mydata.csv')

# csv.reader() was imported above and parses an opened file, assigning it to variable "csv_f"
csv_f = csv.reader(f)

# the parsed data from csv.reader() is converted into a list, and assigned to variable "all_rows"
all_rows = list(csv_f)

# the header row is separated out from the rest of the data; positionality in Python begins with 0
header_row = all_rows[0]
data_rows = all_rows[1:]

# closes .csv file
f.close()

# defines our custom function that converts a csv row to an XML record
# the function will be used to iterate over the items in the "data_rows" list and convert them into XML
# %s is a placeholder for the data in each column
# note: this script could be improved because the fields are currently "hard-coded"
# i.e. only a .csv file with the below columns will work with this script
# for simplicity I left it as is to demonstrate the basics of this function
# if you're looking for a challenge, this script can be modified to read any .csv file, no matter the colummns
# and that's what programming's all about!
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

# opens a new .xml file that we are writing to, indicated by 'w', and adds a root element
new_xml_file = open('converted.xml', 'w')
new_xml_file.write('<rootElement>')
new_xml_file.write('\n')

# we loop over each row, not including the header since "data_rows" was previously assigned as the rest of our data
for row in data_rows:
    
    # converts each row to XML using our custom function above
    xml_record = convert_row(row)
    
    # writes that converted XML to our new file
    new_xml_file.write(xml_record)
    
    # adds a new line between XML <record> tags
    new_xml_file.write('\n')

# writes the closing tag for the root element and closes our file
new_xml_file.write('</rootElement>')
new_xml_file.close()
