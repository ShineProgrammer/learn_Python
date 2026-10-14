import random

number = int(input("Enter your number: "))
x = 1
y = 10

while 1:                   
    hads = random.randint(x , y)
    print('is it ' , hads , '?')
    offer = input()
    
    if offer == 'more':
        x = hads + 1
        continue
    elif offer == 'yes':
        print('wow, damn!')
        break
    elif offer == 'less':
        y = hads -1
        continue
    