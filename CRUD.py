import operator
def Ler(dicionario):
    max_key = max(dicionario.items(), key=operator.itemgetter(1))[0]

    for i in range(0, 2):
        print(" ---------------", end="")
    for i in range(0, dicionario[max_key][0]):
        print(" ---------------", end="")
    print()
    print("| Tipo    \t| N. Itens    \t|", end="")
    if dicionario[max_key][0] != 0:
        print(" Dado    \t|")
    else:
        print()
    for i in range(0, 2):
        print(" ---------------", end="")
    for i in range(0, dicionario[max_key][0]):
        print(" ---------------", end="")
    print()
    for tipo in dicionario:
        print('|', tipo[:7], '    \t| ', end="")
        for dado in dicionario[tipo]:
            print(str(dado)[:6]+'..', '    \t| ', end="")
        print()
        for i in range(0, 2):
            print(" ---------------", end="")
        for i in range(0, dicionario[max_key][0]):
            print(" ---------------", end="")
        print()
        
def teste(tipo, dicionario):

    if tipo == "bool" or not tipo in dicionario:
        print("Tipo invalido: ", tip)
        return 0
    else:
        return 1

def converter(dicionario, tipo, entrada, acao):
    
    if acao == 1:
        try:
            dicionario[tipo].append(type(eval(entrada))(entrada))
            dicionario[tipo][0] += 1
        except:
            print("\nSintax invalida")
            return
    elif acao == 3:
        try:
            index = dicionario[tipo].index(type(eval(entrada))(entrada))
        except:
            print("\nSintax invalida")
            return
        dicionario[tipo][index] = type(eval(entrada))(input("Digite o novo dado\n"))
    elif acao == 4:
        try:
            dicionario[tipo].remove(type(eval(entrada))(entrada))
            dicionario[tipo][0] -= 1
        except:
            print("\nSintax invalida")
            return
    
def acao():
    
    print("Qual açao deseja executar?\n")
    print("1 - Criar")
    print("2 - Ler")
    print("3 - Atualizar")
    print("4 - Remover")
    print("5 - Sair") 
    return input()

def main():
    # usando um dicionario para salvar as info
    dicionario = {"int":[0,], "float":[0,], "complex":[0,], "list":[0,], "tuple":[0,], "range":[0,], "str":[0,], "list":[0,], "set":[0,], "frozenset":[0,], "dict":[0,]}

    print("Bem vindo")

    while 1:
        try:
            a = int(acao())
        except:
            print("\nAçao invalida!\n")
            continue

        if a == 5:
            exit()
    
        print()

        if a == 1:
            entrada = input("Digite o dado que deseja adicionar\n")
            try:
                tip = str(type(eval(entrada))).split("'")[1]
            except:
                print("Sintax invalida")
                continue
            if not teste(tip, dicionario):
                continue
            converter(dicionario, tip, entrada, a)
        elif a == 2:
            Ler(dicionario)
        elif a == 3:
            entrada = input("Digite o dado que deseja editar\n")
            tip = str(type(eval(entrada))).split("'")[1]
            if not teste(tip, dicionario):
                continue
            converter(dicionario, tip, entrada, a)
        elif a == 4:
            entrada = input("Qual dado deseja remover?\n")
            tip = str(type(eval(entrada))).split("'")[1]
            if not teste(tip, dicionario):
                continue
            converter(dicionario, tip, entrada, a)
        else:
            print("Açao invalida")
        print()

if __name__ == '__main__':
    main()

