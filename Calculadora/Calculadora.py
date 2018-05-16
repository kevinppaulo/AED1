#inicializando variáveis globais
x =y = operacao = 0
#Loop que mantém a calculadora executando
while(True):
    print("#############################")
    print("Digite a operação a ser feita")
    operacao = int(input('''    1- Adição
    2-Subtração
    3- Multiplicação
    4- Divisão
    0- Sair\nSua opção: '''))
    
    if operacao == 1:
        x = int(input("Digite um numero: "))
        y = int(input("Digite um segundo numero: "))
        print("O resultado da soma é: ", x+y)
        #soma:
    elif operacao == 2:
        x = int(input("Digite um numero: "))
        y = int(input("Digite um segundo numero: "))
        print("O resultado da subtração é: ", x-y)
        #subtração
    elif operacao == 3:
        #multiplicação
        x = int(input("Digite um numero: "))
        y = int(input("Digite um segundo numero: "))
        if(x or y == 0):
            print("O resultado da multiplicação é 0")
            continue
        mult = x
        for i in range(1,y):
            mult+=x
        print("O resultado da multiplicação é:",mult)
        
    elif operacao == 4:
        #divisão
        x = int(input("Digite um numero: "))
        y = int(input("Digite um numero diferente de zero: "))
        if(y==0):
            while(y==0):
                y = int(input("Erro! Impossível dividir por zero! Tente outra vez: "))
        div = 0
        while(x-y >= 0):
            x-=y
            div+=1
        print("O resultado da divisão é:",div,"com resto",x)
        
    elif operacao == 0:
        #encerrar programa
        break;
    else:
        #Erro.
        print("Operação inválida.")
    