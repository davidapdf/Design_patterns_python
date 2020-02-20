# -*- coding: UTF-8 -*-

def envia_por_email(nota_fiscal):
    print(f'A nota com a razao social: {nota_fiscal.razao_social} foi enviada')

def salva_no_banco(nota_fiscal):
    print(f'salvo no banco a razao social {nota_fiscal.razao_social}')

def imprime(nota_fiscal):
    print(nota_fiscal)