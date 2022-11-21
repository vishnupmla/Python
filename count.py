s=input("enter the  text")
cnt=dict()
x=s.split()
for i in x:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
print(cnt)