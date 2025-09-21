x=int(input('Please enter a number of which you would like to convert to binary.\n'))
i=x
if i==0:
    print('The binary number of',i,'is 0')
s=str('')
f=str('')
sum=str('')
while i>0:
    r=i%2
    b=str(r)+sum
    i=i//2
    f=b+f
    if i<1:
        print('The binary of the decimal',x,'is',f,'.')