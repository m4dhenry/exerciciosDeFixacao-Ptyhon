class Cliente:
    def __init__(nome = '', dtCadastro = ''):
        self._nome = nome
        self._dtCadastro = dtCadastro
    
    def get_nome(self):
        return self._nome
    def set_nome(self, value)
        self._nome = value
    
    def get_dtCadastro(self):
        return self.__dtCadastro
    def set_dtCadastro(self,value):
        self._dtCadastro = value

    @abstractclassmethod
    def getIdentificação(self):
        pass

class PessoaFisica(Cliente):
    def __init__(nome = '', dtCadastro = '', idade = 0, cpf = ''):
        super().__init__(nome = '', dtCadastro = '')
        self._idade = idade
        self._cpf = cpf
    
    def get_idade(self):
        return self._idade
    def set_idade(self, value):
        if value.isnumeric() and not value.isalpha():
            self._idade = int(value)
        else:
            print ('Valor Inválido')
    
    def get_cpf(self):
        return self._cpf
    def set_cpf(self, value):
        if value.isnumeric() and not value.isalpha() and len(value)==11:
            self._cpf = value
        else:
            print ('CPF Inválido')

    def getIdentificacao(self):
        print ('CPF: ',self.get_cpf())

class PessoaJurídica(Cliente):
    def __init__(nome = '', dtCadastro = '', cnpj = ''):
        super().__init__(nome = '', dtCadastro = '')
        self._cnpj = cnpj
    
    def get_cnpj(self):
        return self._cnpj
    def set_cnpj(self,value):
        if value.isnumeric() and not value.isalpha() and len(value)==14:
            self._cnpj = value
        else:
            print ('CNPJ Inválido')

    def getIdentificacao(self):
        print ('CNPJ: ',self.get_cnpj())