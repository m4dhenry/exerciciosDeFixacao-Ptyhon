#digite um número
#o programa dirá quantos números primos existem de 2 ao numero escolhido
x=range(2,int(input('numero: ')))
primos=[]
for i in x: 
  if i%2!=0!=i%3 and  i%5!=0!=i%7: 
    primos.append(i)
  elif 2==i or i==3 or i==5 or i==7:
    primos.append(i)
print(sorted(primos))
print(f'{len(primos)} numeros primos')