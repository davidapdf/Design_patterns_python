class calculadora():
    def realiza_calculo(self,orcamento,tipo):
        calculado = tipo.calcula(orcamento)
        print (calculado)

if __name__ == "__main__":
    from orcamento import orcamento, Item
    from imposto import ICMS, ISS, IKCV, ICPP

    orcamento = orcamento()
    orcamento.adiciona_item(Item('Item 1',100))
    orcamento.adiciona_item(Item('Item 2',50))
    orcamento.adiciona_item(Item('Item 3',200))
    orcamento.adiciona_item(Item('Item 4',100))
    calculadora = calculadora()
    print("ICMS, ISS")
    calculadora.realiza_calculo(orcamento,ICMS())
    calculadora.realiza_calculo(orcamento,ISS())
    print("IKCV, ISS")
    calculadora.realiza_calculo(orcamento,IKCV())
    calculadora.realiza_calculo(orcamento,ICPP())
    print("Imposto Composto")
    calculadora.realiza_calculo(orcamento,IKCV(ICMS(IKCV())))
    calculadora.realiza_calculo(orcamento, IKCV(ICPP()))