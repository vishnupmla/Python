s1=input('enter the first string: ')
s2=input('Enter the second string: ')
s=s2[0]+s1[1::]+' '+s1[0]+s2[1::]
print('new string = ',s)
