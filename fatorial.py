def main ():

    """função que calcula fatorial"""


    num = int(input("Fatorial de: "))
    if num < 0:
        print("O número deve ser maior que 0.")
    elif num == 0:
        print ("0! = 1")
    else:
        print ("%i! =" %num, end = '')
        fat = 1
        for i in range (num, 0, -1):
            fat *= i
            if i == 1:
                print(" 1 =", fat)
            else:
                print(" %d ." %i, end = '')
        
main()
        
