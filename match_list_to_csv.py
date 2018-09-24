import csv

with open("test_list.csv") as csv_file:
    reader = csv.DictReader(csv_file)

    external_media = []
    archives_processing = []

    for row in reader:
        external_media.append(row['B'])
        # iterates thru values in column labeled B in csv and appends each to external_media list
        archives_processing.append(row['D'])
        # iterates thru values in column labeled D in csv and appends each to archives_processing list

    missing_files = [x for x in external_media if x not in archives_processing]
    # print(missing_files) will print values in shell
    
    with open('missing_files_list.csv', 'a', newline='') as output_csv:
        writer = csv.writer(output_csv, delimiter=',')
        for file in missing_files:
            writer.writerow([file])
