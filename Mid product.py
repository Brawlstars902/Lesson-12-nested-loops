n=int(input('Please enter a 4 or mor digit number of which you would like to find the product of its middle digits.\n'))
t=n
l=0
while t>0:
    l=l+1
    t=int(t/10)
if l>=4:
    l=int(l/2)
    c=0
    while n>0:
        r=n%10
        if c==l:
            m=r
        elif c==(l-1):
            m2=r
        n=int(n/10)
        c=c+1
    p=m*m2
print('The product of '+str(m)+' times '+str(m2)+'(the middle numbers) is',p,'.')

