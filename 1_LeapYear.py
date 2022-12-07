year=int(input('Enter the current year : '))
fut=int(input('Enter the future year : '))

print('Leap years are : \n')
for i in range(year,fut):
    if(i%4==0) and (i%100!=0) or (i%400==0):
        print(i)