from random import randrange

rodando = True
while rodando:
    num = randrange(2, 100)
    print("Bem vindo ao jogo do chute!\n")
    print ("Tente adivinhar o número que estou pensando, entre 1 e 100:")
    chute = 0
    cont = 0
    while chute != num:
        chute = int(input("Seu chute: "))
        cont += 1
        if chute == num:
            break
        if chute > num:
            print ("Você deve chutar mais baixo!")
        else:
            print ("Você deve chutar mais alto!")
        
    print ("Parabéns, você acertou!!")
    print (f"Você chutou {cont} vezes.")
    rodando = bool(int(input("Você deseja jogar novamente? Digite: 1 - SIM / 0 - Não: ")))
    if not rodando:
        print("\nObrigado por jogar!")
    print("")