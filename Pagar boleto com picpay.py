# Teste de pagar boleto com picpay
# Vale a pena utilizar o saldo preexistente pra gerar boleto?

percent_cashback = int(input("Digite qual valor de porcentagem o Picpay irá dar de cashback: "))
boleto = int(input("Digite o valor do boleto a ser pago, em reais: "))
limite_boleto = int(input("Digite o valor limite do boleto para o qual o cashback de %i%% é válido: " %(percent_cashback)))
saldo = float(input("Digite o valor do seu saldo atual na conta Picpay: "))
taxa = float(input("Digite a taxa (em %), que será cobrada no cartão de crédito: "))
resp = input("Você deseja usar o saldo anterior para pagar o boleto? Responda ""y"" para sim e ""n"" para não: ")


    
if resp == 'y':# utiliza o saldo que já tinha na conta
    fat_cartao = (boleto - saldo)*(1 + taxa/100)
    if fat_cartao <= limite_boleto:
        cashback = percent_cashback/100 * fat_cartao
    else:
        cashback = percent_cashback/100 * limite_boleto
    ganho_liq = boleto + cashback - fat_cartao - saldo
    
elif resp == 'n': # não utiliza o saldo que já tinha na conta
    fat_cartao = boleto *(1 + taxa/100)
    if fat_cartao <= limite_boleto:
        cashback = percent_cashback/100 * fat_cartao
    else:
        cashback = percent_cashback/100 * limite_boleto
    ganho_liq = boleto + cashback - fat_cartao
    
else:
    print("Resposta inválida")

print ("\nTotal de cashback ganho: R$ %.2f" % cashback)
print ("Ganho líquido: R$ %.2f" % ganho_liq)

# como truncar a casa decimal?
# tem como transformar ponto em virgula?

