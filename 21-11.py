lst=[]
n=int(input("Enter the range"))

for i in range(n):
    x=int(input('Enter the list element'))
    if x>100:
        lst.append('over')
    else:
        lst.append(x)

print(lst)