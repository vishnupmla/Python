lst1=[12,7,4,9,13]
lst2=[12,25,8]
lst3=[]

#a
if len(lst1)==len(lst2):
    print("Two list are of same length")
else:
    print("List are not of same length")


#b
if sum(lst1)==sum(lst2):
    print('List sum are equal')
else:
    print('List sum is not equal')

#c
for i in lst1:
    if i in lst2:
        lst3.append(i)
    
print('Common element = ',lst3)



