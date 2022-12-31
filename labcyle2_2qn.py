#fibanocci series

n=int(input('Enter the number '))
n1=0
n3=0
n2=1
print('The fibanocci series with {} terms are: '.format(n))
for i in range(n):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    