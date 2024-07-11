# -*- coding:utf-8 -*-
class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.lista = []
        
    def get_lista(self):
        if len(self.lista)==0:
            return self.lista
        listaaux = []
        for i in self.lista:
            listaaux.append(i.dado)
        listaaux = listaaux[:-1]
        listaaux.append(self.cauda)
        return listaaux             

    def inserir(self, novo_dado, posicao):
        posicao -= 1
        anterior=posicao-1
        if (posicao < 0) or (posicao > len(self.lista)):
            print('*** Posição Inválida ***')
            return
        if len(self.lista) == 0: #caso a lista seja vazia e so adicionar o novo nodo
            novo_nodo = Nodo(novo_dado)
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
            self.lista.append(novo_nodo)
            return
        if posicao == 0: # caso seja inserido no inicio
            novo_nodo = Nodo(novo_dado, self.cabeca)
            self.cabeca = novo_nodo
            self.lista.insert(0, novo_nodo)
        elif posicao == len(self.lista): #caso seja inserido no final
            novo_nodo = Nodo(novo_dado)
            self.lista.append(novo_nodo)
            self.lista[-2].proximo = novo_nodo
            self.cauda = novo_nodo
        else: #caso seja inserido no meio
            novo_nodo = Nodo(novo_dado, self.lista[posicao])
            self.lista[anterior].proximo = novo_nodo
            self.lista.insert(posicao, novo_nodo)

    def remover(self, posicao):  
        posicao -= 1
        anterior=posicao-1
        if (posicao < 0) or (posicao > len(self.lista)):
            print('*** Posição Inválida ***')
            return False
        # caso a lista tenha apenas um elemento e so remover o item
        if len(self.lista) == 1:
            self.lista.pop(0)
            return
        if posicao == 0: #retirando cabeca da lista e e tornando o item sucessor a cabeca da lista
            self.lista.pop(0)
            self.cabeca = self.lista[0]
        elif posicao+1 == len(self.lista): #removendo ultimo item da lista e tirando a referencia do anterior
            self.lista.pop(-1)
            self.lista[-1].proximo = None
            self.cauda = self.lista[-1]
        else: #removendo item do meio
            self.lista[posicao].proximo = None
            self.lista[anterior].proximo = None
            self.lista.pop(posicao)
            self.lista[anterior].proximo = self.lista[posicao]
    
    def busca(self, valor):
        corrente = self.cabeca
        posicao = 1
        while corrente.dado != valor:
            corrente = corrente.proximo
            posicao+=1
            if corrente == None:
                return str(valor)+' nao existe', None
        return corrente.dado,posicao

msg =' LISTAS ENCADEADAS '
print (f'{msg:=^50}')       
lista = ListaEncadeada()
print('Lista vazia: ',lista.get_lista())
lista.inserir(2,1)
lista.inserir(4,2)
lista.inserir(3,2)
lista.inserir(5,4)
print('Nova lista: ',lista.get_lista())
msg =' TESTE DE INSERCAO COM SUCESSO '
print (f'{msg:=^50}') 
print()
print('='*50)
busca1 = lista.busca(1)
busca2 = lista.busca(4)
busca3 = lista.busca(3)
busca4 = lista.busca(6)
print(f'Item {busca1[0]} na lista, posicao {busca1[1]}')
print(f'Item {busca2[0]} na lista, posicao {busca2[1]}')
print(f'Item {busca3[0]} na lista, posicao {busca3[1]}')
print(f'Item {busca4[0]} na lista, posicao {busca4[1]}')
msg =' TESTE DE BUSCA COM SUCESSO '
print (f'{msg:=^50}') 
print()
print('='*50)
lista.remover(4)
print(lista.get_lista())
lista.remover(2)
print(lista.get_lista())
lista.remover(1)
print(lista.get_lista())
lista.remover(1)
print(lista.get_lista())
msg =' TESTE DE REMORCAO POR POSICAO COM SUCESSO '
print (f'{msg:=^50}') 
print()
print('='*50)