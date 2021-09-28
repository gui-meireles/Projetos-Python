alimentos = int(input("Quantos alimentos você consumiu hoje? "))
x = 1
soma = 0

while alimentos >= x:
    calorias = int(input("Quantas calorias teve o {}° alimento? ".format(x)))
    x = x + 1
    soma = soma + calorias
else:
    print("O total de calorias foi de: {} Kcal".format(soma))
    




