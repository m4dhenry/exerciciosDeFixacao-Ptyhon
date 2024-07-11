import random
x=[1,2,3,4,5,6,7,8,9]
while x[0]+x[1]+x[2]!=15 or x[3]+x[4]+x[5]!=15 or x[6]+x[7]+x[8]!=15:
    random.shuffle(x)    
    while x[0]+x[3]+x[6]!=15 or x[1]+x[4]+x[7]!=15 or x[2]+x[5]+x[8]!=15:
        random.shuffle(x)
        while x[0]+x[4]+x[8]!=15 or x[2]+x[4]+x[6]!=15:
            random.shuffle(x)
print ('█'*40)
cubo='| CUBO MÁGICO |'
print (f'{cubo:-^46}')
print ('█'*40)
fail="""             
████████████████████████████████████████
████████████████▌▄▌▄▐▐▌█████████████████
████████████████▌▄▌▄▐▐▌▀████████████████
████████████████████████████████████████
               TENTE NOVAMENTE!"""
congrats=" PARABÉNS! "
finished="""\033[7m
           VOCÊ FINALIZOU O PUZZLE !
                 █ ▄▀█  █▀▄ █
                ▐▌           ▐▌
                █▌▀▄  ▄▄  ▄▀▐█
               ▐██  ▀▀  ▀▀  ██▌
              ▄████▄  ▐▌ ▄████▄\033[m"""
lin=['A','B','C','D','E','F','G','H','I']
lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '

print ('█'*40)
print (f'{lin1:█^42}')
print ('█'*40)
print (f'{lin2:█^42}')
print ('█'*40)
print (f'{lin3:█^42}')
print ('█'*40)
print ()
print ('█_ Atrás de cada letra tem um número de 1 a 9')
print ('█_ A soma das linhas,colunas e diagonais = 15')
print ('█_ Adivinhe qual número está em qual posição')
print ("█_ Digite 'Dica' para uma CHARADA")
print ()
ponto=0
j=[False]
while set(j)!={True}:
    position=input('Digite posição + número sugerido (ex:A8):').upper()
    if 1!=len(position)!=0:
        if position[0]=='A' and position[1].isnumeric()==True:
            if int(position[1])==x[0]:
                lin.pop(0)
                lin.insert(0,x[0])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=230
            else:
                print (fail)
                print ()
                ponto-=51
        elif position[0]=='B' and position[1].isnumeric()==True:
            if int(position[1])==x[1]:
                lin.pop(1)
                lin.insert(1,x[1])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=230
            else:
                print (fail)
                print ()
                ponto-=51
        elif position[0]=='C' and position[1].isnumeric()==True:
            if int(position[1])==x[2]:
                lin.pop(2)
                lin.insert(2,x[2])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=230
            else:
                print (fail)
                print ()
                ponto-=51
        elif position[0]=='D' and position[1].isnumeric()==True:
            if int(position[1])==x[3]:
                lin.pop(3)
                lin.insert(3,x[3])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=230
            else:
                print (fail)
                print ()
                ponto-=52
        elif position[0]=='E' and position[1].isnumeric()==True:
            if int(position[1])==x[4]:
                lin.pop(4)
                lin.insert(4,x[4])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=160
            else:
                print (fail)
                print ()
                ponto-=130
        elif position[0]=='F' and position[1].isnumeric()==True:
            if int(position[1])==x[5]:
                lin.pop(5)
                lin.insert(5,x[5])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=230
            else:
                print (fail)
                print ()
                ponto-=51
        elif position[0]=='G' and position[1].isnumeric()==True:
            if int(position[1])==x[6]:
                lin.pop(6)
                lin.insert(6,x[6])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=230
            else:
                print (fail)
                print ()
                ponto-=51
        elif position[0]=='H' and position[1].isnumeric()==True:
            if int(position[1])==x[7]:
                lin.pop(7)
                lin.insert(7,x[7])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=230
            else:
                print (fail)
                print ()
                ponto-=51
        elif position[0]=='I' and position[1].isnumeric()==True:
            if int(position[1])==x[8]:
                lin.pop(8)
                lin.insert(8,x[8])
                lin1=' '+str(lin[0])+' █ '+str(lin[1])+' █ '+str(lin[2])+' '
                lin2=' '+str(lin[3])+' █ '+str(lin[4])+' █ '+str(lin[5])+' '
                lin3=' '+str(lin[6])+' █ '+str(lin[7])+' █ '+str(lin[8])+' '
                print ('█'*40)
                print (f'{lin1:█^42}')
                print ('█'*40)
                print (f'{lin2:█^42}')
                print ('█'*40)
                print (f'{lin3:█^42}')
                print ('█'*40)
                print (f'{congrats:█^42}')
                print ('█'*40)
                print ()
                ponto+=230
            else:
                print (fail)
                print ()
                ponto-=51
        elif position=='DICA':
            print ()
            print ('O resto da divisão por 2 dos numeros X é 0')
            g=input ("Mais charadas? digite 'Dica' ou aperte enter: ").lower()
            if g=='dica':
                print ()
                print ('Os extremos são complementares de reverse(zed)')
                h=input ("Mais charadas? digite 'Dica' ou aperte enter: ").lower()
                if h=='dica':
                    print ()
                    print ('O resto da divisão por 2 dos numeros + é 1')
                    k=input ("Mais charadas? digite 'Dica' ou aperte enter: ").lower()
                    if k=='dica':
                        print ()
                        print ('É sempre o mesmo número no meio')
            print()
        else:
            print ()
            com='COMANDO INVÁLIDO'
            print (f'{com: ^44}')
            print ()
    j=map(lambda x:x.isnumeric(),map(str,lin))
print (finished)
if ponto==2000:
    print ('           Pontuação Máxima: ',ponto)
else:
    print ('           Pontuação: ',ponto)