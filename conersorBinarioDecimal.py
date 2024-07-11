#charles(m4dhenrry)
#python 3.7.1
while True:
  ins1="| Binary to decimal (type 'b') |"
  ins2="| Decimal to binary (type 'd') |"
  comand="| Invalid command |"
  print ("="*40)
  print (f"{ins1:=^40}\n{ins2:=^40}")
  contar=4
  while True:
      print ("="*contar)
      contar+=1
      if contar==7:
          print ("="*(contar),end="")
          alt=input ("> ")
          break
  print ("="*40)
  if alt =="b":
      sub1="| Type the binary number: |"
      print (f"{sub1:=^40}")
      contar=4
      while True:
          print ("="*contar)
          contar+=1
          if contar==7:
              print ("="*contar,end="")
              bina=input ("> ")
              break
      if bina.isnumeric()==True and set(bina)=={'1','0'} or set(bina)=={'1'} or set(bina)=={'0'}:
          bina=bina[::-1]
          decimal=[]
          exp=0
          for x in bina:
              num=int(x)*(2**exp)
              decimal.append(num)
              exp+=1
          sub2="| Decimal number: "
          sub3= str(sum(decimal))+" |"
          print ("="*40)
          print (f"{sub2+sub3:=^40}")        
          print ()
      else:
          print(f"{comand:=^40}")
          print()
  elif alt=="d":
      sub4="| Decimal number: |"
      print (f"{sub4:=^40}")
      contar=4
      while True:
          print ("="*contar)
          contar+=1
          if contar==7:
              print ("="*contar,end="")
              deci=input ("> ")
              break
      if deci.isnumeric()==True:
          deci=int(deci)
          binary=[]
          while deci!=1 and deci!=0:
            binary.append(deci%2)
            deci=deci//2    
          if deci!=0:
            binary.append(1)
            binary="".join(map(str, binary[::-1]))
          else:
            binary=str(deci)
          sub5="| binary number: "+binary+" |"
          print (f"{sub5:=^40}")
          print ()
      else:
          print(f"{comand:=^40}")
          print()
  else:
      print(f"{comand:=^40}")
      print()
print ()