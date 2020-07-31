# digital_archiving
Total beginner here. Sharing some basic Python 3 scripts I've used to manage electronic records and large amounts of data. A lot of what I've written could be improved upon, so please feel free to suggest changes if you see places where code could be simplified or made better. I'm learning as I go and could use feedback!

**csv_convert.py**: converts a .csv file into an .xml file letting you map the data to custom XML tags (commented version)
**csv_convert_no_comments.py**: same as above, sans comments

**hs6_07_1411.xsl**: XSLT document that transforms a single XML file into individual Dublin Core-based XML files (using a custom prefix) and names each file according to whatever value is in the `<filename>` element plus ".metadata" ; I use it to create individual .metadata files for ingest alongside records into Preservica

**archPlans_cardCreator_commented.py**: uses the ReportLab library to create 'virtual index cards' (as pdfs) for each row in a csv file


~~ Catch me at alejandradean.com.
