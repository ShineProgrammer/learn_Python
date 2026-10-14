import random

rNum = random.randint(1, 100)
while 1:
    number = int(input("ye adad bego pisar! : "))
    if number > rNum:
        print("bozorgtar gofti pisar!")
    elif number == rNum:
            print("afarin pisar!")
            break
    else:
        print("kochik tar gofti pisar!")