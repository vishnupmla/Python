import csv

with open('file.csv') as newfile:
    prjct = csv.reader(newfile)
    print(prjct)
    for i in prjct:
        print(i[1])