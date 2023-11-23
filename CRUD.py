def converter(dicionario, tipo, entrada, acao):
    
    if tipo == "int":
        if acao == 1:
            dicionario[tipo].append(int(entrada))
        elif acao == 3:
            index = dicionario[tipo].index(int(entrada))
            dicionario[tipo]
            return            
        elif acao == 4:
            dicionario[tipo].remove(int(entrada))
    elif tipo == "float":
        if acao == 1:
            dicionario[tipo].append(float(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(float(entrada))
    elif tipo == "complex":
        if acao == 1:
            dicionario[tipo].append(complex(entrada))
        elif acao == 3:
            return            
       
        elif acao == 4:
            dicionario[tipo].remove(complex(entrada))
    elif tipo == "list":
        if acao == 1:
            dicionario[tipo].append(list(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(list(entrada))
    elif tipo == "tuple":
        if acao == 1:
            dicionario[tipo].append(tuple(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(tuple(entrada))
    elif tipo == "range":
        if acao == 1:
            dicionario[tipo].append(range(entrada))
        elif acao == 3:
            return           
        
        elif acao == 4:
            dicionario[tipo].remove(range(entrada))
    elif tipo == "str":
        if acao == 1:
            dicionario[tipo].append(str(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(str(entrada))
    elif tipo == "bytes":
        if acao == 1:
            dicionario[tipo].append(bytes(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(bytes(entrada))
    elif tipo == "bytearray":
        if acao == 1:
            dicionario[tipo].append(bytearray(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(bytearray(entrada))
    elif tipo == "memoryview":
        if acao == 1:
            dicionario[tipo].append(memoryview(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(memoryview(entrada))
    elif tipo == "set":
        if acao == 1:
            dicionario[tipo].append(set(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(set(entrada))
    elif tipo == "frozenset":
        if acao == 1:
            dicionario[tipo].append(frozenset(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(frozenset(entrada))
    elif tipo == "dict":
        if acao == 1:
            dicionario[tipo].append(dict(entrada))
        elif acao == 3:
            return            
        
        elif acao == 4:
            dicionario[tipo].remove(dict(entrada))

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
        converter(dicionario, tipo, entrada, a)
    elif a == 2:
        print(dicionario[tipo])
    elif a == 3:
        entrada = input("Digite o dado que deseja editar")
        converter(dicionario, tipo, entrada, a)
    elif a == 4:
        entrada = input("Qual dado deseja remover?\n")
        converter(dicionario, tipo, entrada, a)
    else:
        print("Açao invalida")
    print()
