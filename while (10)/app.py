import time
a = 1

while True:
    print(a)
    a += 1
    time.sleep(1)
    if a == 100: 
        break

print('the while circle is broken')