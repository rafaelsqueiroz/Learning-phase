from random import randint


cont = 0
lot = 0
lista = []
print("Números escolhidos: ", end = '')
while cont < 6:
    num = (randint(1,60))
    if num != lot:
        lot = num
        lista.append(lot)
        cont += 1
lista.sort()
print(lista)
