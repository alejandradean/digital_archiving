# digital_archiving
Total beginner here. Sharing some basic Python 3 scripts I've used to manage electronic records and large amounts of data. A lot of what I've written could be improved upon, so please feel free to suggest changes if you see places where code could be simplified or made better. I'm learning as I go and could use feedback!

**csv_convert.py**: converts a .csv file into an .xml file letting you map the data to custom XML tags (commented version)
**csv_convert_no_comments.py**: same as above, sans comments

**date_change_xml.py**: parses an XML file and formats dates to YYYY-MM-DD (will throw errors if the dates are just months and years or just years, working on a fix)

**hs6_07_1411.xsl**: XSLT document that transforms a single XML file into individual Dublin Core-based XML files (using a custom prefix) and names each file according to whatever value is in the <filename> element plus ".metadata" ; I use it to create individual .metadata files for ingest alongside records into Preservica

**xml_parse.py**: walks through a directory and all subdirectories, opens and parses any file named "operationalMetadata.xml", and writes the values of three specified XML tags to a .csv file (values are appended, so .csv is not overwritten each time an XML file is parsed)

~~
Catch me at alejandradean.com.
