import time
import random as rd

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.conta = [] 
        
    def realizar_transacao(self, conta, transacao):
        transacao.adicionar(conta)
    
    def adicionar_conta(self, conta):
        self.conta.append(conta)


class Pessoa_fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
        
class Pessoa_juridica(Cliente):
    def __init__(self, nome_empresa, cnpj, endereco):
        super().__init__(endereco)
        self.nome_empresa = nome_empresa
        self.cnpj = cnpj
        

class Conta(Cliente):
    def __init__(self, numero, cliente):
        self.saldo = 0
        self._numero = numero
        self_agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()