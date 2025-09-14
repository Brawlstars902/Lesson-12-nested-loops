x=input('Please enter a string of letters.\n')
a=input('Please enter a character to find the recurrences of that character in the string.\n')
i=0
o=0
while (i<len(x)):
    if(x[i]==a):
        o=o+1
    i=i+1
print('The number of times',a,'is in ',x,'is',o,'.')
