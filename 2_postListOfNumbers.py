lst=[]
n=int(input('Enter the no of elements to be stored in list: '))

print('Enter the elemnts ')
for i in range(0,n):
    lst.append(int(input()))

print('The positive integers are : ')
for i in lst:
    if(i>0):
        print(i)