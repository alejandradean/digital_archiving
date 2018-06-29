import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('2013_export.xml')
root = tree.getroot()

for date in root.iter('Dates'):
  [month, day, year] = date.text.split('/')

  if len(month) == 1:
        month = '0' + month
            
  if len(day) == 1:
        day = '0' + day
  else:
    continue
  
  date.text = year + '-' + month + '-' + day

tree.write('2013_export.xml')
