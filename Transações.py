transacao = int(input("Quantas transações você fez hoje? "))
x = 1
soma = 0

while transacao >= x:
    valor = int(input("Qual o valor da {}° transação? ".format(x)))
    x = x + 1
    soma = soma + valor
else:
    print("O total gasto foi de: {} reais".format(soma))
    
    media = soma / transacao
    print("A média por transação foi de {:.2f} reais".format((media)))