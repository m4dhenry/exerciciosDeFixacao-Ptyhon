# -*- coding:utf-8 -*-
class Nodo:
    def __init__(self, dado=0, anterior_nodo=None):
        self.dado = dado
        self.proximo = anterior_nodo

    def __repr__(self):
        return '%s -> %s' % (self.proximo, self.dado)

class Pilha:
    def __init__(self):
        self.topo = None

    def Empilhar(self, valor):
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = self.topo
        self.topo = novo_nodo
    
    def Desempilhar(self):
        if (self.Vazia()):
            print("Pilha vazia.")
            return
        self.topo = self.topo.proximo
            
    def Vazia(self):
        if(self.topo==None):
            return True
        return False
        
    def Esvaziar(self):
        self.topo = None
        
class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
    def vazia(self):
        if(self.cabeca == None):
            return True
        return False
    
    def Emfilerar(self, valor):
        novo_nodo = Nodo(valor)
        if (self.Vazia()):
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
            return
        self.cauda.proximo = novo_nodo
        self.cauda = novo_nodo
            
    def Desemfilerar(self):
        if (self.Vazia()):
            print('Fila vazia')
            return
        self.cabeca = self.cabeca.proximo
    
    def Esvaziar(self):
        self.cabeca = None
        self.cauda = None

pilha = Pilha()
pilha.Empilhar(3)
pilha.Empilhar(4)
pilha.Empilhar(5)
pilha.Empilhar(6)
pilha.Desempilhar()
