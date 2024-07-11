import random
import numpy as np

def OrdBin(lista):
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
    return OrdBin(esquerda)+[pivot]+OrdBin(direita)
            
Lista=set(np.random.randint(1,100,(15)))

print ("Lista gerada automaticamente: ")
print(Lista)
print()
print("Lista Ordenada: ")
print(OrdBin(Lista))