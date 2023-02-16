
f=open('test.txt','r')
g=open('test1.txt','a+')
l=f.readlines()
for i in range(0,len(l),2):
    g.write(l[i])

print(g.readlines())



