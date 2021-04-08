import os

directory_path = input("Enter directory path: ")

# the below will create a file 'filenames.txt' in the same directory the script is saved in. Enter the full path in addition to the .txt filename to create the file elsewhere.
with open('filenames.txt', 'a') as file:
    for root, dirs, files in os.walk(directory_path):
        file.write('-- Directory: {} --'.format(root))
        file.write('\n\n')
        for filename in files:
            file.write('{}'.format(filename))
            file.write('\n')
        file.write('\n')

file.close()

# the below code prints the output in the shell and uses old syntax
# for root, dirs, files in os.walk(directory_path):
    # print('Directory: %s' % root)
    # for filename in files:
        # print('\t%s' % filename)
