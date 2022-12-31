a=input("Enter a string ")
a=a.replace(" ","")

cnt=dict()

for i in a:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1
print("The count of each charecters in the string are: \n",cnt)