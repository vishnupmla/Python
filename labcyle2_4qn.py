# Generate a list of four digit numbers in a given range with all their digits even and the 
#  number is a perfect square.


n1=int(input('Enter the starting index(4 digit) : '))
n2=int(input('Enter the ending index(4 digit) : '))
nums=[]

for i in range(n1,n2):
    s=str(i)
    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
        q=pow(i,.5)
        if q==int(q):
            nums.append(q*q)
if len(nums)==0:
    print('No Element')
else:
    print('Numbers with all digit even and perfect squares are - ',nums)   
    
    
        

            
            
