from nota_fiscal import Nota_fiscal,Item

class Criador_nota_fiscal():

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = ''
        self.__itens = None

    def com_razao_social(self,razao_social):
        self.__razao_social = razao_social
        return self
    def com_cnpf(self,cnpj):
        self.__cnpj = cnpj
        return self
    def com_data_de_emissao(self,data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self
    def com_detalhes(self,detalhes):
        self.__detalhes = detalhes
    def com_itens(self,itens):
        self.__itens = itens
    def construir(self):
        if self.__razao_social is None:
            raise Exception ('A Razao social é obrigatoria')
        if self.__cnpj is None:
            raise Exception("O CNPJ é obrigatorio")
        if self.__itens is None:
            raise Exception("Itens são necessários")

        return Nota_fiscal(
            razao_social=self.__razao_social,
            cnpj=self.__cnpj,
            itens=self.__itens,
            data_de_emissao=self.__data_de_emissao,
            detalhes=self.__detalhes
        )