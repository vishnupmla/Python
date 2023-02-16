import csv
with open('file.csv') as newfile:
    obj = csv.reader(newfile)
    for i in obj:
        print(i)