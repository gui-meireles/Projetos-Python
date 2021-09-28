assinatura = int(input("Qual sua assinatura? 1-Basic / 2-Silver / 3-Gold / 4-Platinum " " "))
faturamento = float(input("Qual o seu faturamento anual? "))

if assinatura == 1:
    basic = faturamento * 0.3
    print("O valor a se pagar é de: {:.2f}".format(basic))
elif assinatura == 2:
    silver = faturamento * 0.2
    print("O valor a se pagar é de: {:.2f}".format(silver))
elif assinatura == 3:
    gold = faturamento * 0.1
    print("O valor a se pagar é de: {:.2f}".format(gold))
elif assinatura == 4:
    platinum = faturamento * 0.05
    print("O valor a se pagar é de: {:.2f}".format(platinum))
