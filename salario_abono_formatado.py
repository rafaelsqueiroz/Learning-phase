"""
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em
reconhecimento ao bom resultado alcançado durante o ano que passou.
Para isto contratou você para desenvolver a aplicação que servirá como uma
projeção de quanto será gasto com o pagamento deste abono.

o	Após reuniões envolvendo a diretoria executiva, a diretoria financeira e
    os representantes do sindicato laboral, chegou-se a seguinte forma de
    cálculo:

o	a.Cada funcionário receberá o equivalente a 20% do seu salário bruto
        de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles
        funcionários cujo salário for muito baixo, recebem este valor mínimo;
        Neste momento, não se deve ter nenhuma preocupação com colaboradores
        com tempo menor de casa, descontos, impostos ou outras particularidades.
        Seu programa deverá permitir a digitação do salário de um número
        indefinido (desconhecido) de salários. Um valor de salário igual a 0
        (zero) encerra a digitação. Após a entrada de todos os dados o programa
        deverá calcular o valor do abono concedido a cada colaborador, de acordo
        com a regra definida acima. Ao final, o programa deverá apresentar:
        
o	O salário de cada funcionário, juntamente com o valor do abono;
o	O número total de funcionário processados;
o	O valor total a ser gasto com o pagamento do abono;
o	O número de funcionário que receberá o valor mínimo de 100 reais;
o	O maior valor pago como abono; A tela abaixo é um exemplo de execução do
        programa, apenas para fins ilustrativos. Os valores podem mudar a cada
        execução do programa.

Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""

def main ():
        """Programa de Projeção de Gastos com Abono"""

        print ("\nPrograma de Projeção de Gastos com Abono")
        print ("="*40)
        lista = []
        salario = 1
        while True:
                salario = float(input("Salário: "))
                if salario == 0:
                        break
                abono = 0.2*salario
                if abono < 100:
                        abono = 100
                lista.append([salario, abono]) #salario é o elemento [0] e abono é o elemento [1]

        print("\nSalário     - Abono     ")

        saida = []

        for i in range(len(lista)): 

                #cifrão
                saida.append("R$ ")

                #salário
                x = "%.2f" %(lista[i][0])
                Formata1 (i,x,8,saida)
                saida[i] += " - R$ "

                #abono
                x = "%.2f" %(lista[i][1])
                Formata1 (i,x,7,saida)

                print(saida[i])

def Formata1 (i,entr,lmt,output):
        if len (entr) <= lmt:
                output[i] += (lmt-len(entr))*" "+ entr
        else:
                output[i] += entr

main()