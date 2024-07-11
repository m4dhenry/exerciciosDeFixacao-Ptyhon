class Setor:
    def __init__(self, nome='', sigla=''):
        self._sigla=sigla
        self._nome=nome

    def get_sigla(self):
        return self._sigla
    def set_sigla(self, valor):
        self._sigla= valor.strip()

    def get_nome(self):
        return self._nome
    def set_nome(self, valor):
        self._nome=valor.strip()

    def dadosSetor(self):
        print('Nome: ',self._nome,'(',self._sigla,')')

class Empregado:
    def __init__(self, codigo=0, salario=0, nome='', setor:Setor='', data_nascimento='', idade=0):
        self._codigo=codigo
        self._salario=salario
        self._nome=nome
        self._setor=setor
        self._data_nascimento=data_nascimento
        self._idade=idade
    
    def get_codigo(self):
        return self._codigo
    def set_codigo(self, valor):
        self._codigo= int(valor.strip().replace(' ',''))
     
    def get_salario(self):
        return self._salario
    def set_salario(self, valor):
        self._salario= valor
        
    def get_nome(self):
        return self._nome
    def set_nome(self, valor):
        self._nome= valor.strip()
        
    def get_setor(self):
        return self._setor
    def set_setor(self, nome, sigla):
        self._setor= Setor(nome, sigla)
        
    def get_data_nascimento(self):
        return self._data_nascimento
    def set_data_nascimento(self, valor):
        self._data_nascimento = valor.strip().replace(' ','')

    def get_idade(self):
        return self._idade
    def set_idade(self, valor):
        self._idade=valor                       

    def dadosEmpregado(self):
        print('Nome: ',self._nome)
        print('Data de nascimento: ',self._data_nascimento)
        print('Idade: ',self._idade,' anos')
        print('Código: ',self._codigo)
        print('Setor: ',(self._setor).get_nome(),'(',(self._setor).get_sigla(),')')
        print('Salário: ',self._salario)

class Gerente(Empregado):
    def __init__(self, codigo=0, salario=0, nome='', setor: Setor ='', data_nascimento='', idade=0, beneficios=0):
        super().__init__(codigo=0, salario=0, nome='', setor='', data_nascimento='', idade=0)
        self._beneficios=beneficios

    def get_beneficio(self):
        return self._beneficios
    def set_beneficio(self, valor):
        self._beneficios= int(valor.strip())

    def salarioGerente(self):
        self._salariofinal=self._salario+self._beneficios

    def dadosGerente(self):
        super().dadosEmpregado()
        print('Valor dos benefícios: ',self._beneficios)
        print('Sálario Final: ',self._salariofinal)


class Estagiario(Empregado):
    def __init__(self, codigo=0, salario=0, nome='', setor:Setor='', data_nascimento='', idade=0, qtdemeses=0):
        super().__init__(codigo=0, salario=0, nome='', setor='', data_nascimento='', idade=0)
        self._qtdemeses=qtdemeses

    def get_qtdemeses(self):
        return self._qtdemeses
    def set_qtdemeses(self, valor):
        self._qtdemeses = int(valor.strip())
    
    def dadosEstagiario(self):
        super().dadosEmpregado()
        print('Quantidade de meses: ',self._qtdemeses)