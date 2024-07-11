total=float(input("Total: "))
num_=[]
print ()
print("#Digite no máximo 5 números ou 'none' para parar")
n=[]
while n!="none" and len(num_)<5:
    n=input("-> Numero: ")
    if n=="none":
        num_.pop(-1)
    else:
        num_.append(n)
k=total/sum(map(int,num_))
print ()
print(f'#constante de proporcao k = {k}')
its=[]
u_=0
while len(its)<len(num_):
    print(f'Proporcional a {num_[u_]}= {int(num_[u_])*k} ')
    its.append(u_)
    u_=u_+1