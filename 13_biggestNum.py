a1=int(input("Enter 1st num: "))
a2=int(input('Enter 2nd num: '))
a3=int(input('Enter 3rd num: '))

if a1>a2:
    if a1>a3:
        print('{} is greater than {} and {}'.format(a1,a2,a3))
    else:
        print('{} is greater than {} and {}'.format(a3,a1,a2))
elif a2>a3:
    print('{} is greater than {} and {}'.format(a2,a3,a1))

else:
    print('{} is greater than {} and {}'.format(a3,a2,a1))