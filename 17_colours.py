lst1=[]
lst2=[]
lst3=[]
n=int(input('Enter the number of colours'))
print('Enter the colours in 1st list')
for i in range(n):
    lst1.append(input())
print('Enter the colours in 2nd list')
for i in range(n):
    lst2.append(input())

for i in lst1:
    if i not in lst2:
        lst3.append(i)

print(lst3)