n=int(input('Enter the number '))
s=[]
for i in range(1,n+1):
    if n%i==0:
        s.append(i)
print('The factors of {} are: {}'.format(n,s))