# -*- coding: UTF-8 -*-
from descontos import Desconto_por_cinco_itens,Desconto_por_mais_de_quinhentos_reais,Sem_desconto

class Calcularora_de_descontos():
    def calcular(self,orcamento):
        desconto = Desconto_por_mais_de_quinhentos_reais(
            Desconto_por_cinco_itens(
                Sem_desconto()
            )
        )
        return desconto.calcular(orcamento)


if __name__ == '__main__':
    from orcamento import orcamento,Item
    orcamento = orcamento()
    orcamento.adiciona_item(Item('Item A',100.0))
    orcamento.adiciona_item(Item('Item B',50.0))
    orcamento.adiciona_item(Item('Item C',400.0))

    calculadora_de_desconto = Calcularora_de_descontos()
    desconto = calculadora_de_desconto.calcular(orcamento)
    print("desconto calculado {}".format(desconto))
