def converter(dicionario, tipo, entrada):
    
    if tipo == "int":
        dicionario[tipo].append(int(entrada))
    elif tipo == "float":
        dicionario[tipo].append(float(entrada))
    elif tipo == "complex":
        dicionario[tipo].append(complex(entrada))
    elif tipo == "list":
        dicionario[tipo].append(list(entrada))
    elif tipo == "tuple":
        dicionario[tipo].append(tuple(entrada))
    elif tipo == "range":
        dicionario[tipo].append(range(entrada))
    elif tipo == "str":
        dicionario[tipo].append(str(entrada))
    elif tipo == "bytes":
        dicionario[tipo].append(bytes(entrada))
    elif tipo == "bytearray":
        dicionario[tipo].append(bytearray(entrada))
    elif tipo == "memoryview":
        dicionario[tipo].append(memoryview(entrada))
    elif tipo == "set":
        dicionario[tipo].append(set(entrada))
    elif tipo == "frozenset":
        dicionario[tipo].append(frozenset(entrada))
    elif tipo == "dict":
        dicionario[tipo].append(dict(entrada))

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
    tipo = input("Digite o tipo de dado que deseja manipular\n")
    if tipo == "bool" or not tipo in dicionario:
        print("Tipo invalido")
        continue

    if a == 1:
        entrada = input("Digite seu dado\n")
        converter(dicionario, tipo, entrada)

    elif a == 2:
        print("Nao implementada")
    elif a == 3:
        print("Nao implementada")
    elif a == 4:
        dado = input("Qual dado deseja remover?\n")
        dicionario[tipo].remove(dado)
    else:
        print("Açao invalida")
    print() 

    print(dicionario)
