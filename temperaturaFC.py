temp1=int(input("Digite a primeira temperatura: ")),input("Digite sua repectiva escala ('c' ou 'f'): ")
temp2=int(input("Digite a segunda temperatura: ")),input("Digite sua respectiva escala (: ")
if temp2[1]!=temp1[1]:
    if temp2[1].lower()=='f':
        tempf1=temp1[0]*1.8+32
        maior=tempf1,temp2[0]
        print (f"A temperatura {max(maior)} é maior que {min(maior)}")
    if temp2[1].lower()=='c':
        tempf1=(temp1[0]-32)/1.8
        maior=tempf1,temp2[0]
        print (f"A temperatura {max(maior)} é maior que {min(maior)}")
else:
    maior=temp2[0],temp1[0]
    print (f"A temperatura {max(maior)} é maior que {min(maior)}")