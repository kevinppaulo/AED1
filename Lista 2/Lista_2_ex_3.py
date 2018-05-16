lista = []
positivos = []
negativos = []
for i in range(0,10):
    try:
        lista.append(int(input("Digite um numero: ")))
    except:
        print("você não deve digitar letras ou simbolos")

for item in range(0,10):
    if lista[item] > 0:
        positivos.append(lista[item])
    elif lista[item] < 0:
        negativos.append(lista[item])
print(lista)
print(positivos)
print(negativos)