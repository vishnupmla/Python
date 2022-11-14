word='Kerala is gods own country, Kerala is  small state'

temp=list(set(word.split()))

for i in temp:
    print('Word \'{}\' occurs {} times in line of text'.format(i,word.count(i)))

