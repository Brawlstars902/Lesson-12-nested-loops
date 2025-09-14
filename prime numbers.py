x=int(input('Please enter a number: '))
y=int(input('Please enter another number that is greater than your first number: '))
print('The prime numbers between',x,'and',y,'are:')
for number in range(x,y+1):
    if number> 1:
        for i in range(2,number):
            if number%i==0:
                break
        else:
            print(number)