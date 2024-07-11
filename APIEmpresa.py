import funcionarios
from datetime import date
import os

def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age 

setores=[]
gerentes=[]
empregados=[]
estagiarios=[]

while True:
    menu=' MENU PRINCIPAL '
    print('='*50)
    print(f'{menu:=^50}')
    print('1. Cadastrar Funcionário')
    print('2. Aumentar salario')
    print('3. Listar setores')
    print('4. Listar funcionários')
    print('6. Finalizar')
    print('='*50)
    print('Digite o número da opção desejada: ')
    opcao=input('')
    os.system('clear') or None

    if opcao=='1':
        aux=0
        while aux!=1:
            cadastro=' CADASTRAR FUNCIONÁRIO '
            print('='*50)
            print(f'{cadastro:=^50}')
            print('1. Empregado')
            print('2. Gerente')
            print('3. Estagiário')
            print('4. Voltar ao menu principal')
            print('='*50)
            print('Digite o número da opção desejada: ')
            opco=input()
            print()
            if opco=='1':
                funcionario=funcionarios.Empregado()
                funcionario.set_nome(input('Nome completo: '))
                funcionario.set_data_nascimento(input('Data de nascimento (DD/MM/AAAA): '))
                if '/' in funcionario.get_data_nascimento():
                    age=funcionario.get_data_nascimento().split('/')
                else:
                    os.system('clear') or None
                    print('*** DATA INFORMADA INVÁLIDA ***')
                    continue
                funcionario.set_codigo(input('Codigo Empregado: '))
                funcionario.set_setor(input('Setor: '), input('Sigla do Setor: '))
                funcionario.set_salario(int(input('Salário: ').strip().replace(' ','')))
                funcionario.set_idade(calculateAge(date(int(age[2]), int(age[1]), int(age[0]))))
                empregados.append(funcionario)
                setores.append(funcionario.get_setor())
                os.system('clear') or None
                print('*** CADASTRO REALIZADO COM SUCESSO ***')
                continue
            elif opco=='2':
                funcionario=funcionarios.Gerente()
                funcionario.set_nome(input('Nome completo: '))
                funcionario.set_data_nascimento(input('Data de nascimento (DD/MM/AAAA): '))
                if '/' in funcionario.get_data_nascimento():
                    age=funcionario.get_data_nascimento().split('/')
                else:
                    os.system('clear') or None
                    print('*** DATA INFORMADA INVÁLIDA ***')
                    continue
                funcionario.set_codigo(input('Codigo Empregado: '))
                funcionario.set_setor(input('Setor: '), input('Sigla do Setor: '))
                funcionario.set_salario(int(input('Salário: ').strip().replace(' ','')))
                age=funcionario.get_data_nascimento().split('/')
                funcionario.set_idade(calculateAge(date(int(age[2]), int(age[1]), int(age[0]))))
                funcionario.set_beneficio(input('Valor do Benefíco: '))
                funcionario.salarioGerente()
                gerentes.append(funcionario)
                setores.append(funcionario.get_setor())
                os.system('clear') or None
                print('*** CADASTRO REALIZADO COM SUCESSO ***')
                empregados.append(funcionario)
                continue
            elif opco=='3':
                funcionario=funcionarios.Estagiario()
                funcionario.set_nome(input('Nome completo: '))
                funcionario.set_data_nascimento(input('Data de nascimento (DD/MM/AAAA): '))
                if '/' in funcionario.get_data_nascimento():
                    age=funcionario.get_data_nascimento().split('/')
                else:
                    os.system('clear') or None
                    print('*** DATA INFORMADA INVÁLIDA ***')
                    continue
                funcionario.set_codigo(input('Codigo Empregado: '))
                funcionario.set_setor(input('Setor: '), input('Sigla do Setor: '))
                funcionario.set_salario(int(input('Salário: ').strip().replace(' ','')))
                age=funcionario.get_data_nascimento().split('/') 
                funcionario.set_idade(calculateAge(date(int(age[2]), int(age[1]), int(age[0]))))
                funcionario.set_qtdemeses(input('Quantidade de meses do estágio: '))
                estagiarios.append(funcionario)
                setores.append(funcionario.get_setor())
                os.system('clear') or None
                print('*** CADASTRO REALIZADO COM SUCESSO ***')
                empregados.append(funcionario)
                continue
            elif opco=='4':
                aux=1
                os.system('clear') or None
                continue
            else:
                os.system('clear') or None
                print('*** OPÇÃO INVÁLIDA TENTE NOVAMENTE ***')
    elif opcao=='3':
        listar_s=' LISTAR SETORES '
        print('='*50)
        print(f'{listar_s:=^50}')
        print()
        if len(setores)!=0:
            for i in setores:
                i.dadosSetor()
                print()
            print('FIM da lista, click ENTER para voltar ao menu inicial')
            input()
            os.system('clear') or None
        else:
            os.system('clear') or None
            print('           *** NENHUM SETOR CADASTRADO ***')
            print('*** Para cadastrar um setor é preciso cadastrar um funcionário ***')

    elif opcao=='4':
        if (empregados)!=0:
            aux=0
            while aux!=1:
                listagem=' LISTAR FUNCIONÁRIOS '
                print('='*50)
                print(f'{listagem:=^50}')
                print('1. Todos Empregados')
                print('2. Gerentes')
                print('3. Estagiários')
                print('4. Voltar ao menu principal')
                print('='*50)
                print('Digite o número da opção desejada: ')
                opc=input()
                print()
                if opc=='1':
                    for i in empregados:
                        i.dadosEmpregado()
                        print()
                    print('FIM da lista, click ENTER para voltar ao menu inicial')
                    input()
                    os.system('clear') or None
                elif opc=='2':
                    if len(gerentes)==0:
                        os.system('clear') or None
                        print('*** NENHUM GERENTE CADASTRADO ***')
                        continue
                    for i in gerentes:
                        i.dadosGerente()
                        print()
                    print('FIM da lista, click ENTER para voltar ao menu inicial')
                    input()
                    os.system('clear') or None
                elif opc=='3':
                    if len(estagiarios)==0:
                        os.system('clear') or None
                        print('*** NENHUM ESTAGIÁRIO CADASTRADO ***')
                        continue
                    for i in estagiarios:
                        i.dadosEstagiario()
                        print()
                    print('FIM da lista, click ENTER para voltar ao menu inicial')
                    input()
                    os.system('clear') or None
                elif opc=='4':
                    aux=1
                    os.system('clear') or None
                    continue
                else:
                    os.system('clear') or None
                    print('*** OPÇÂO INVÁLIDA ***')
                    continue
                aux=1
                print()
        else:
            os.system('clear') or None
            print('*** NENHUM FUNCIONÁRIO CADASTRADO ***')

    elif opcao=='2':
        if len(empregados)!=0:
            percent=' AUMENTO DE SALÁRIO '
            print('='*50)
            print(f'{percent:^50}')
            percentual=input('-> Percentual de aumento (apenas números): ').strip().replace(' ','')
            print()
            if (percentual.isnumeric() or not percentual.isalnum()) or (0>percentual):
                for i in empregados:
                    print('Funcionario: ', i.get_nome(),'  Código: ',i.get_codigo())
                    print('Salario antigo: ',i.get_salario())
                    i.set_salario(i.get_salario()+(i.get_salario()*float(percentual)/100))
                    print('Novo salario', i.get_salario())
                    print()
                for i in gerentes:
                    print('Funcionario: ', i.get_nome(),'  Código: ',i.get_codigo())
                    print('Salario antigo: ',i.get_salario())
                    i.set_salario(i.get_salario()+(i.get_salario()*float(percentual)/100))
                    print('Novo salario', i.get_salario())
                    print()
                for i in estagiarios:
                    print('Funcionario: ', i.get_nome(),'  Código: ',i.get_codigo())
                    print('Salario antigo: ',i.get_salario())
                    i.set_salario(i.get_salario()+(i.get_salario()*float(percentual)/100))
                    print('Novo salario', i.get_salario())
                    print()
            else:
                os.system('clear') or None
                print('*** VALOR INVÁLIDO ***')
            print('Aumento aplicado com sucesso! ')
            print()
            print('-> Click ENTER para voltar ao menu inicial')
            input()
            os.system('clear') or None
        else:
            os.system('clear') or None
            print('*** NENHUM FUNCIONÁRIO CADASTRADO ***')

    elif opcao=='6':
        print()
        print('PROGRAMA FINALIZADO! ')
        break

    else:
        os.system('clear') or None
        print('*** OPÇÂO INVÁLIDA ***')