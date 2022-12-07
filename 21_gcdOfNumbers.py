n1=int(input("Enter the first number \n"))
n2=int(input('Enter the second number \n'))

for i in range(1,min(n1,n2)):
    if(n1%i==0 and n2%i==0):
        gcd=i
print('The GCD of {} and {} = {}'.format(n1,n2,gcd))
    
