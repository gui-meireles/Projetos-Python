peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura**2

print("Seu IMC é: {:.2f}".format(imc))

if imc < 16:
    print("Sua categoria é Baixo peso Grau III")
elif imc < 16.99:
    print("Sua categoria é Baixo peso Grau II")
elif imc < 18.49:
    print("Sua categoria é Baixo peso Grau I")
elif imc < 24.99:
    print("Sua categoria é Peso Ideal")
elif imc < 29.99:
    print("Sua categoria é Sobrepeso")
elif imc < 34.99:
    print("Sua categoria é Obesidade Grau I")
elif imc < 39.99:
    print("Sua categoria é Obesidade Grau II")
else:
    print("Sua categoria é Obesidade Grau III")
