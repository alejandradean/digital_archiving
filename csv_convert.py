# the csv module contains a library of code specifically written to handle data in .csvs
import csv

# the open() function, a built-in Python function, opens my .csv file, assigning it to variable "f"
# note: the path is relative, meaning the .csv is in the same directory as this script  
f = open('mydata.csv')

# csv.reader() was imported above and parses an opened file, assigning it to variable "csv_f"
csv_f = csv.reader(f)

# the parsed data from csv.reader() is converted into a list, and assigned to variable "all_rows"
# we do this because csv.reader() returns something called a generator
# generators have to be used in certain ways, so it's much easier to turn this into a list
all_rows = list(csv_f)

# the header row is separated out from the rest of the data; positionality in Python begins with 0
header_row = all_rows[0]
data_rows = all_rows[1:]

# closes .csv file
f.close()

# defines our custom function that converts the iterated data in our new list into XML
# %s is a placeholder for the data in each column
# this script could be improved by not hard-coding the fields; for example, if I use this on a .csv with different fields it would not work
# for simplicity I left it as is to demonstrate the basics of this function
# if you're looking for a challenge try to convert this to something that could work with any .csv file
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

# opens a new .xml file that we are writing to, indicated by 'w'
new_xml_file = open('converted.xml', 'w')

# we loop over each row, not including the header
for row in data_rows:
    
    # convert each row to XML using our function above
    xml_record = convert_row(row)
    
    # write that converted XML to our new file
    new_xml_file.write(xml_record)
    
    # add a new line between records
    new_xml_file.write('\n')

# close our file
new_xml_file.close()
    
    
    
