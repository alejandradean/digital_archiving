import csv

with open("test_list.csv") as csv_file:
    reader = csv.DictReader(csv_file)

    external_media = []
    archives_processing = []

    for row in reader:
        external_media.append(row['B'])
        archives_processing.append(row['D'])

    missing_files = [x for x in external_media if x not in archives_processing]
    print(missing_files)

