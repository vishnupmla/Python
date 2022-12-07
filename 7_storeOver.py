lst=[]
n=int(input("Enter the size of list: "))
print('Enter the lsit elements: \n')
for i in range(n):
    x=int(input())
    if x>100:
        lst.append('Over')
    else:
        lst.append(x)

print(lst)    