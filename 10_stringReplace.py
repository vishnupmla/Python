s=input('Enter a string : ')
a=s[0]
f=a
n=len(s)
for i in range(1,n):
    if s[i]==a:
        f=f+'$'
    else:
        f=f+s[i]


print(f)