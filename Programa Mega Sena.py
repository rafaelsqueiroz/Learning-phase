from random import randint
cont = lot = 0
print("Números escolhidos:")
while cont < 6:
    num = (randint(1,60))
    if num != lot:
        lot = num
        print (lot)
        cont += 1