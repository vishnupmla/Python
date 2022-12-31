lst=['Maharashtra','Karnataka','Gujarat','Kerala','Madhya Pradesh']
lrg=lst[0]

for i in lst:
    
    if len(i)>len(lrg):
        lrg=i

print("The largest word in the list is '{}' and length is {}. ".format(lrg,len(lrg)))
    