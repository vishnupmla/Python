lst=['sam','Kannan','Punnose','Tancy']
count=0
for i in lst:
    for j in i:
        if j=='a':
            count+=1

print('The occurance of -a- is: ',count)