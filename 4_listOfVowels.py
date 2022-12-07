word=input('Enter the word : ')
lst=[]
vowels='AEIOUaeiou'
for i in word:
    if i in vowels:
        lst.append(i)
print('Vowels are :',lst)