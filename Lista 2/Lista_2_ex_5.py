lista1 = []
lista2 = []
lista_composta = []

for i in range(0,5):
    try:
        lista1.append(int(input("Digite um número: ")))
    except:
        print("Você deve inserir apenas números")
        continue

for i in range(0,5):
    try:
        lista2.append(int(input("Digite um número: ")))
    except:
        print("Você deve inserir apenas números")
        continue

for i in range(0,5):
    lista_composta.append(lista1[i])

for i in range(0,5):
    lista_composta.append(lista2[i])

#remover duplicados
memoria = []
for i in range(0,10):
    memoria.append(lista_composta[i])
    if(lista_composta[i] in memoria):
        del lista_composta[i]

lista1.sort()
lista2.sort()
lista_composta.sort()

print(lista1)
print(lista2)
print(lista_composta)