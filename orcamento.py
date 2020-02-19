# -*- coding: UTF-8 -*-
from abc import abstractmethod,ABCMeta
class Estado_de_um_orcamento():
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self,orcamento):
        pass
class Em_aprovacao_(Estado_de_um_orcamento):
    def aplica_desconto_extra(self,orcamento):
        orcamento.desconto_extra += orcamento.valor * 0.05

class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self,orcamento):
            orcamento.desconto_extra += orcamento.valor * 0.02

class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self,orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')

class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self,orcamento):
        raise Exception('Orçamento finalizados não recebem descontos extra')


class orcamento():
    def __init__(self):
        self.__itens = []
        self.estado_atual = 1
        self.__desconto_extra = 0.0

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self,item):
        self.__itens.append(item)

    def adiciona_desconto_extra(self,desconto):
        self.__desconto_extra += desconto

class Item():
    def __init__(self,nome,valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor
    @property
    def nome(self):
        return self.__nome