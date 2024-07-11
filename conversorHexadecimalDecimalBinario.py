def decb(binary):
    binary= binary[::-1]
    bin=[f for f in binary]
    if set(bin)=={'1','0'} or set(bin)=={'1'} or set(bin)=={'0'}:
        decimal=0
        c=0
        for x in binary:
            decimal=decimal+(2**c)*int(x)
            c+=1
        return decimal
    return 'Não binário'
        

def hexb(binary):
    bin=[f for f in binary]
    if set(bin)=={'1','0'} or set(bin)=={'1'} or set(bin)=={'0'}:
        binary_list=[]
        while len(binary)!=0:
            binary_list.append(binary[-4:])
            c=len(binary[-4:])
            while c>0:
                binary=binary[:-1]
                c-=1
        hexadecimal=' '
        decimal_list=[]
        for y in binary_list:
            decimal=0
            c=0
            for x in y[::-1]:
                decimal=decimal+(2**c)*int(x)
                c+=1
            decimal_list.append(decimal)
        for g in decimal_list:
            hexadecimal=hexadecimal+hex(g)[2:]
        return hexadecimal[1:].upper()
    return 'Não binário'

def bind(decimal):
    if decimal.isnumeric()==True:
        binary=bin(int(decimal))[2:]
        return binary
    return 'Não decimal'

def hexd(decimal):
    if decimal.isnumeric()==True:
        hexadecimal=hex(int(decimal))[2:].upper()
        return hexadecimal 
    return 'Não decimal'

def binh(hexa):
    hexa=hexa[::-1].upper()
    if 'A' in hexa or 'B' in hexa or 'C' in hexa or 'D' in hexa or 'E' in hexa or 'F' in hexa or hexa.isnumeric()==True:
        decimal=0
        c=0
        for x in hexa:
            if x=='A':
                decimal+=10*(16**c)
            elif x=='B':
                decimal+=11*(16**c)
            elif x=='C':
                decimal+=12*(16**c)
            elif x=='D':
                decimal+=13*(16**c)
            elif x=='E':
                decimal+=14*(16**c)
            elif x=='F':
                decimal+=15*(16**c)
            elif x.isnumeric()==True:
                decimal+=int(x)*(16**c)
            else:
                return 'Não hexadecimal'
            c+=1
        binary=bin(int(decimal))[2:]
        return binary
    return 'Não hexadecimal'

def dech(hexa):
    hexa=hexa[::-1].upper()
    if 'A' in hexa or 'B' in hexa or 'C' in hexa or 'D' in hexa or 'E' in hexa or 'F' in hexa or hexa.isnumeric()==True:
        decimal=0
        c=0
        for x in hexa:
            if x=='A':
                decimal+=10*(16**c)
            elif x=='B':
                decimal+=11*(16**c)
            elif x=='C':
                decimal+=12*(16**c)
            elif x=='D':
                decimal+=13*(16**c)
            elif x=='E':
                decimal+=14*(16**c)
            elif x=='F':
                decimal+=15*(16**c)
            elif x.isnumeric()==True:
                decimal+=int(x)*(16**c)
            else:
                return 'Não hexadecimal'
            c+=1
        return decimal
    return 'Não hexadecimal'

while True:
    print ('•'*44)
    que='( Digite um número: )'
    tipo='( Decimal ou Binário ou Hexadecimal )'
    print (f'{que:•^44}')
    print (f'{tipo:•^44}')
    print ('•'*44)
    print ()
    print ('•'*7,end='')
    num=input('| ')
    print ()
    print (f'|Binário({num})-> decimal:     ',decb(num))
    print (f'|Binário({num})-> hexadecimal: ',hexb(num))
    print (f'|Decimal({num})-> binário:.    ',bind(num))
    print (f'|Decimal({num})-> hexadecimal: ',hexd(num))
    print (f'|Hexadecimal({num})-> binário: ',binh(num))
    print (f'|Hexadecimal({num})-> decimal: ',dech(num))
    print ()