#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse


def le_comando(lista_argumentos):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-n', nargs='?', required=False, default=10, type=int, action='store', const=10)
    arg_parser.add_argument('-r', action='store_true')
    arg_parser.add_argument('nome_arquivo')

    argumentos = arg_parser.parse_args(lista_argumentos[1:])

    num_de_linhas = argumentos.n
    if not argumentos.nome_arquivo:
        if lista_argumentos[0] == 'tail.py':
            return 'Especifique um Arquivo'

    if argumentos.r:
        arquivo = open(argumentos.nome_arquivo, 'r')

        linhas = arquivo.readlines()
        linhas.reverse()

        return linhas
    try:
        arquivo = open(argumentos.nome_arquivo, 'r')
    except IOError:
        return 'Arquivo Inexistente'
    else:
        linhas = arquivo.readlines()
        total_de_linhas = len(linhas)
        linha_limite = total_de_linhas - num_de_linhas

    return linhas[linha_limite:total_de_linhas]

if __name__ == '__main__':
    linhas = le_comando(sys.argv)
    for linha in linhas:
        sys.stdout.write(linha)
