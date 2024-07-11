total=int(input("Total: "))
num_=[]
print ()
print("#Digite no maximo 5 numeros e 'none' para parar")
n=[]
while n!="none" and len(num_)<5:
    n=input("-> Numero: ")
    if n=="none":
        num_.pop(-1)
    else:
        num_.append(n)
num_= map(int,num_)
num_=sorted(num_)
print()

#Minimo multiplo comum
fat1=[]
fat2=[]
fat3=[]
fat4=[]
fat5=[]
z=0
for x in num_:
    p=0
    if z==0:
        while len(fat1)<=1000:
            p=p+x
            fat1.append(p)
    if z==1:
        while len(fat2)<=1000:
            p=p+x
            fat2.append(p)
    if z==2:
        while len(fat3)<=1000:
            p=p+x
            fat3.append(p)
    if z==3:
        while len(fat4)<=1000:
            p=p+x
            fat4.append(p)
    if z==4:
        while len(fat5)<=1000:
            p=p+x
            fat5.append(p)  
    z+=1
fat1=set(fat1)
fat2=set(fat2)
fat3=set(fat3)
fat4=set(fat4)
fat5=set(fat5)
inter=[]
if len(fat2):
    inter=fat1 & fat2
if len(fat3)!=0:
    inter=fat1 & fat2 & fat3
if len(fat4)!=0:
    inter=fat1 & fat2 & fat3 & fat4
if len(fat5)!=0:
    inter=fat1 & fat2 & fat3 & fat4 & fat5
inter=sorted(inter)
mmc=inter[0]
print(f'MMC= {mmc}')
#constante de proporcao "k"   
k=total*mmc/sum(map(lambda x:mmc/x, num_))
print ()
print(f'#Constante de proporcao k = {k}')
u=0
while u<len(num_):
    print(f'-> Inversamente Proporcional a {num_[u]}= {k/int(num_[u])} ')
    u=u+1