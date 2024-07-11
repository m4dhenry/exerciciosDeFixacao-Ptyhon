from random import randint
import datetime


class Quarto:
    def __init__(self, número=0, leito, preço_dia=800, situação='livre', data_inicio, data_fim, diária=0):
        self._número = número
        self._leito = leito
        self._preço_dia = preço_dia
        self._situação = situação
        self._data_inicio = data_inicio
        self._data_fim = data_fim
        self._diária = diária

    def get
        

    def __cadastrar(self):
        self._numero = int(input('Número do quarto: '))
        self._leito = int(input('Número de leitos: '))
        print('')

    def __alugar(self):
        if not self._situação == 'livre':
            print('Quarto já alugado ou reservado! ')
            return
        self._data_inico = input("Data de inicio separado por '/'': ").split('/')
        self._data_inico = datetime.date(day=int(self._data_inico[0]), month=int(self._data_inico[1]), year=int(self._data_inico[2]))
        self.data_fim = input("Data de fim separado por '/'': ").split('/')
        self.data_fim = datetime.date(day=int(self.data_fim[0]), month=int(self.data_fim[1]), year=int(self.data_fim[2]))
        self._diária = self._data_inico-self.data_fim
        self._preço_dia = self._preço_dia*self._diária
        self._preço_dia = self.leio/100*20000+self._preço_dia
        self._situação = 'alugado'
        print(f'Quarto alugado com sucesso! Diária: {self._diária}Valor: {self._preço_dia}')

    def __resevar(self):
        if not self._situação == 'livre':
            print('Quarto já alugado ou reservado! ')
            return
        self._data_inico = input(
            "Data de inicio separado por '/'': ").split('/')
        self._data_inico = datetime.date(day=int(self._data_inico[0]), month=int(
            self._data_inico[1]), year=int(self._data_inico[2]))
        self.data_fim = input("Data de fim separado por '/'': ").split('/')
        self.data_fim = datetime.date(day=int(self.data_fim[0]), month=int(
            self.data_fim[1]), year=int(self.data_fim[2]))
        self._diária = self._data_inico-self.data_fim
        self._preço_dia = self._preço_dia*self._diária
        self._preço_dia = self.leio/100*20000+self._preço_dia
        self._situação = 'reservado'
        print(f'Quarto reservado com sucesso! Valor {self._preço_dia}')

    def __liberar(self):
        self._diária = 0
        self._data_inico = '00/00/0000'
        self.data_fim = '00/00/0000'
        self._situação = 'livre'
        self._preço_dia = 1200
