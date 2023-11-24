def teste(tipo, dicionario):

    if tip == "bool" or not tip in dicionario:
        print("Tipo invalido: ", tip)
        return 0
    else:
        return 1

def converter(dicionario, tipo, entrada, acao):
    
    if acao == 1:
        dicionario[tipo].append(type(eval(entrada))(entrada))
    elif acao == 3:
        index = dicionario[tipo].index(type(eval(entrada))(entrada))
        dicionario[tipo][index] = type(eval(entrada))(input("Digite o novo dado\n"))
    elif acao == 4:
        dicionario[tipo].remove(type(eval(entrada))(entrada))
    
def acao():
    
    print("Qual açao deseja executar?\n")
    print("1 - Criar")
    print("2 - Ler")
    print("3 - Atualizar")
    print("4 - Remover")
    print("5 - Sair") 
    return input()

# usando um dicionario para salvar as info
dicionario = {"int":[], "float":[], "complex":[], "list":[], "tuple":[], "range":[], "str":[], "list":[], "tuple":[], "range":[], "set":[], "frozenset":[], "dict":[]}

print("Bem vindo")

while 1:
    a = int(acao())
    
    if a == 5:
        exit()
    
    print()

    if a == 1:
        entrada = input("Digite o dado que deseja adicionar\n")
        tip = str(type(eval(entrada))).split("'")[1]
        if not teste(tip, dicionario):
            continue
        converter(dicionario, tip, entrada, a)
    elif a == 2:
        for tipo in dicionario:
            print(f'{tipo}: {dicionario[tipo]}')
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
