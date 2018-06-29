import os
import csv

filepath = r'C:\Users\adean\Desktop\ongoing'

for root, dirs, files in os.walk(filepath):
    print(root)
    print(dirs)
    print(files)
