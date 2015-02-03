#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse


def le_comando():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-n', nargs=1, required=False, default=[10], type=int)
    arg_parser.add_argument('nome_arquivo')
    argumentos = arg_parser.parse_args(sys.argv[1:])

    num_de_linhas = argumentos.n[0]
    if not argumentos.nome_arquivo:
        if sys.argv[0] == 'head.py':
            return 'Especifique um Arquivo'

    if isinstance(argumentos.n, basestring):
        return 'Especifique um numero de linhas'
    # if len(sys.argv) == 2:
    #     nome_arquivo = sys.argv[1]

    # elif len(sys.argv) == 3:
    #     flag = sys.argv[1]

    #     if flag == '-n':
    #         nome_arquivo = sys.argv[2]
    #     else:
    #         return u'Flag Desconhecida'

    # elif len(sys.argv) == 4:
    #     flag = sys.argv[1]

    #     if flag == '-n':
    #         try:
    #             num_de_linhas = int(sys.argv[2])
    #             nome_arquivo = sys.argv[3]
    #         except ValueError:
    #             return u'Parametro invalido. Especifique um numero'
    #     else:
    #         return u'Flag Desconhecida'

    try:
        arquivo = open(argumentos.nome_arquivo, 'r')
    except IOError:
        return 'Arquivo inexistente'

    return arquivo.readlines()[:num_de_linhas]

if __name__ == '__main__':
    saida = le_comando()

    for i in range(len(saida)):
        sys.stdout.write(saida[i])
