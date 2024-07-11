#---------------------------------------------------------------------------------
#   Atividade está valendo 8,0 pontos de 10,0 pontos da Avaliação da Unidade 1
#---------------------------------------------------------------------------------
#Professora: Clenia Melo Araujo                                   Data: 19/10/2022
#Aluno: Charles Henrique Oleiva de Jesus

#Implemente algoritmo para listas lineares sequenciais de forma que contemple as seguintes situações:

#A função abaixo realizará uma pesquisa de modo binária e retornanará VERDADEIRO OU FALSO
#caso o valor exista ou não na lista.

def BuscaBinaria(item,lista):
    meio=len(lista)//2
    while item!=lista[meio]:
        if meio==0:
            return False
        if item > lista[meio]:
            lista=lista[meio+1:]
            meio=len(lista)//2
        else:
            lista=lista[:meio]
            meio=len(lista)//2
    return True

#A função realizará uma pesquisa de modo sequencial e retornanará VERDADEIRO OU FALSO
#caso o valor exista ou não na lista.

def BuscaSequencial(item,lista):
    for i in lista:
        if i==item:
            return True
    return False

#Função para ordenação binária

def OrdenacaoBinaria(lista):
    if len(lista)<=1:
        return lista
    else:
        pivot=lista.pop()
        
    direita = []
    esquerda = []
    
    for i in lista:
        if i > pivot:
            direita.append(i)
        else:
            esquerda.append(i)
    return OrdenacaoBinaria(esquerda)+[pivot]+OrdenacaoBinaria(direita)

#CABEÇALHO
p="| PROVA DE ESTRUTURA DE DADOS |"
v="| 1° BIMESTRE |"
print (f'{p:=^50}')
print (f'{v:-^50}')
print ()
print ()

#Remoção em Listas Lineares Sequenciais 
t="| Remoção em Listas Lineares Sequenciais |"
print(f'{t:=^50}')

#1 Listas não ordenadas
a='| Listas não Ordenadas |'
print (f'{a:-^50}')
print()

lista=[7,3,15,21,14,40,2]
print(lista)
while True:
    numero=int(input("Número que deseja excluir: "))
    if BuscaSequencial(numero,lista):
        lista.remove(numero)
        print("Nova lista: ",lista)
        break
    else:
        print()
        print(f"O número '{numero}' não existe na lista")
        print("Por favor insira um valor válido ")
print()

#2 Listas ordenadas
a='| Listas Ordenadas |'
print (f'{a:-^50}')
print()

lista=[2,3,7,14,15,21,40]
print(lista)
while True:
    numero=int(input("Número que deseja excluir: "))
    if BuscaBinaria(numero,lista):
        lista.remove(numero)
        print("Nova lista: ",lista)
        break
    else:
        print()
        print(f"O número '{numero}' não existe na lista: ")
        print("Por favor insira um valor válido ")
print()

# Inserção em Listas Lineares Sequenciais 
t="| Inserção em Listas Lineares Sequenciais |"
print(f'{t:=^50}')

#1 Listas não ordenadas
a='| Listas não Ordenadas |'
print (f'{a:-^50}')
print()

lista=[7, 3, 15, 21, 14, 40, 2]
print(lista)
while True:
    numero=int(input("Número que deseja inserir: "))
    if not BuscaSequencial(numero,lista):
        lista.append(numero)
        print("Nova lista: ",lista)
        break
    else:
        print()
        print(f"O número '{numero}' já existe na lista ")
        print("Por favor insira um valor que não está nela ")
print()

#2 Listas ordenadas
a='| Listas Ordenadas |'
print (f'{a:-^50}')
print()

lista=[2, 3, 7, 14, 15, 21, 40]
print(lista)
while True:
    numero=int(input("Número que deseja inserir: "))
    if not BuscaSequencial(numero,lista):
        lista.append(numero)
        lista=OrdenacaoBinaria(lista)
        print("Nova lista: ",lista)
        break
    else:
        print()
        print(f"O número '{numero}' já existe na lista ")
        print("Por favor insira um valor que não está nela ")
print()