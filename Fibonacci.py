proximo = 0
anterior = 0
i = int(input("Coloque aqui o seu número: "))

while(proximo < i):
    proximo = proximo + anterior
    anterior = proximo - anterior

    if(proximo == 0):
        proximo = proximo + 1

if(proximo == i):
    print("Ação bem sucedida!")
else:
    print("A ação falhou...")
