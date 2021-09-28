segunda = int(input("Informe a quantidade de votos na segunda-feira: "))
terca = int(input("Informe a quantidade de votos na terça-feira: "))
quarta = int(input("Informe a quantidade de votos na quarta-feira: "))
quinta = int(input("Informe a quantidade de votos na quinta-feira: "))
sexta = int(input("Informe a quantidade de votos na sexta-feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Segunda-feira é o melhor dia")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Terça-feira é o melhor dia")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Quarta-feira é o melhor dia")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("Quinta-feira é o melhor dia")
else: 
    print("Sexta-feira é o melhor dia")
    

