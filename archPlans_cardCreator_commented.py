#!/usr/bin/env python3
# This is called a "shebang" line. It's used in unix-based OS environments like macOS to tell whatever shell you're using where the Python interpreter is (i.e. it specifies the absolute path to the interpreter). It allows you to then run your script in the shell with the simple command "python 3" instead of "path/to/python3". You don't need this line if you are using Windows.

import csv
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
# Imports the python modules needed to run this script. The user should refer to the ReportLab Toolkit documentation to pre-install the ReportLab package before running this script. ReportLab is a library that lets you create and format PDFs, among other things.

with open('whatever_your_file_is.csv', newline='', encoding='utf-8-sig') as csv_file:
# Opens your csv file and assigns it to variable csv_file. I included the encoding parameter with value "utf-8-sig" because the Byte Order Mark (BOM) character ("\ufeff") was being read at the beginning of my csv file. The csv module documentation indicates that setting the encoding parameter to utf-8-sig will remove this character when decoding the file.
    arch_plans_reader = csv.DictReader(csv_file, delimiter=',')
    # Uses the DictReader method to read the contents of csv_file as a dictionary (or, create key-value pairs between the column headers and cell values). This is helpful because our ultimate goal is to display our csv data in the pdf as "[Column header]: [cell value]" for each cell.
    dict_list = []
    # Each row in our csv file is the equivalent of one virtual index card. So we first need to separate out these rows and store them so that we can then further operate on them one at a time. Here, we are creating an empty list and assigning it to a variable called dict_list. We can then iterate through each row in our csv_file and add it individually to the list.
    for row in arch_plans_reader:
        dict_list.append(row)
        # Iterates through each row in the csv file and appends it to the dict_list.

for dictionary in dict_list: 
# Now that we have one big list in the dict_list variable of each virtual card dictionary, we are now going to iterate through each of those and combine sections of key-value pairs together in order to then display them together. We will then assign those sections into their own descriptive variables. I opted to do this because paragraphs are really difficult to format (imo) in ReportLab. Instead, I decided to do a bit of hard-coding to separate out sections into single-line paragraphs so that the final pdf looks nice.
    filename = dictionary['Filename']
    # Uses the dictionary index method to assign each filename to the filename variable. We will use this later on to name our pdfs.
    location_text = list(dictionary.items())[1:5]
    # Uses the list function to turn each virtual card dictionary back into a list so that we can index it and get only the sections (key-value pairs) we want. Python dictionaries are unordered, so that's why we turn it back into (an ordered) list. We are assigning the 2nd - 4th (Python indexes start at 0) dictionary key-value pairs (so in this case, the Case, Rack, Apart., No. keys with their accompanying values) to the location_text variable so that we can print it out as one line in the PDF later on.
    building_text = list(dictionary.items())[5:7]
    city_text1 = list(dictionary.items())[7:8]
    city_text2 = list(dictionary.items())[8:9]
    address_text = list(dictionary.items())[9:10]
    purpose_class_text = list(dictionary.items())[10:12]
    owner_text = list(dictionary.items())[12:13]
    architect_text = list(dictionary.items())[13:14]
    architect_address = list(dictionary.items())[14:15]
    date_text = list(dictionary.items())[15:17]
    inspector_text = list(dictionary.items())[17:18]
    notes_text = list(dictionary.items())[18:]

    pretty_dict1 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in location_text)
    # More variables! So now that we have our sections already separated out, we need to format it nicely. We convert it into a string of text using the join method on an empty space ("&nbsp;") to combine our key-value pairs together. We are using the string placeholder "{}" formatting method to populate a template that is the key (bolded, i.e. "<b>"), followed by a colon (":"), a space, and then the value (unbolded).
    pretty_dict2 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in building_text)
    pretty_dict3 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in city_text1)
    pretty_dict4 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in city_text2)
    pretty_dict5 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in address_text)
    pretty_dict6 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in purpose_class_text)
    pretty_dict7 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in owner_text)
    pretty_dict8 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in architect_text)
    pretty_dict9 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in architect_address)
    pretty_dict10 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in date_text)
    pretty_dict11 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in inspector_text)
    pretty_dict12 = "&nbsp;".join("<b>{}</b>: {} ".format(column_header, value) for column_header, value in notes_text)
    
    height = 2.99 * inch
    width = 5.09 * inch
    # Here we specify the dimensions of our card and assign each dimension to a variable.
    canvas = Canvas(filename, pagesize=(width, height))
    # Use ReportLab's Canvas method with the filename parameter set to our filename variable (which contains each filename from our csv file) and the dimension variable from above to create a pdf file.
    stylesheet = getSampleStyleSheet()
    normalStyle = stylesheet['Normal']
    # stylesheet info

    paragraph = Paragraph(f'<para>{pretty_dict1}<br/>{pretty_dict2}<br/>{pretty_dict3}<br/>{pretty_dict4}<br/>{pretty_dict5}<br/>{pretty_dict6}<br/>{pretty_dict7}<br/>{pretty_dict8}<br/>{pretty_dict9}<br/>{pretty_dict10}<br/>{pretty_dict11}<br/>{pretty_dict12}</para>', ParagraphStyle('my style', fontName='Courier'))
    padding_w = .25 * inch
    padding_h = .15 * inch
    w,h = paragraph.wrap(width - padding_w * 2, height - padding_h * 2)

    paragraph.drawOn(canvas, padding_w, height - h - padding_h)
    canvas.save()