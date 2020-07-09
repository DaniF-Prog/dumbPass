import random
ln = int(input('enter length: '))
for it in range(0, ln): 
    rc = random.randint(33, 126)
    print(chr(rc), end = "")
