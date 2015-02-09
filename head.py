#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse


def le_comando(lista_argumentos):
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-n', nargs='?', required=False, default=10, type=int)
    arg_parser.add_argument('nome_arquivo')
    argumentos = arg_parser.parse_args(lista_argumentos[1:])

    num_de_linhas = argumentos.n
    if not argumentos.nome_arquivo:
        if lista_argumentos[0] == 'head.py':
            return 'Especifique um Arquivo'

    if isinstance(argumentos.n, basestring):
        return 'Especifique um numero de linhas'

    try:
        arquivo = open(argumentos.nome_arquivo, 'r')
    except IOError:
        return 'Arquivo inexistente'

    return arquivo.readlines()[:num_de_linhas]

if __name__ == '__main__':
    saida = le_comando(sys.argv)

    for i in range(len(saida)):
        sys.stdout.write(saida[i])
