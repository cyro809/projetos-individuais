#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def le_comando():
    num_de_linhas = 10

    if len(sys.argv) == 2:
        nome_arquivo = sys.argv[1]

    elif len(sys.argv) == 3:
        flag = sys.argv[1]

        if flag == '-n':
            nome_arquivo = sys.argv[2]
        else:
            return u'Flag Desconhecida'

    elif len(sys.argv) == 4:
        flag = sys.argv[1]

        if flag == '-n':
            try:
                num_de_linhas = int(sys.argv[2])
                nome_arquivo = sys.argv[3]
            except ValueError:
                return u'Parametro invalido. Especifique um numero'
        else:
            return u'Flag Desconhecida'

    try:
        arquivo = open(nome_arquivo, 'r')
    except IOError:
        return 'Arquivo inexistente'

    return arquivo.readlines()[:num_de_linhas]

if __name__ == '__main__':
    saida = le_comando()

    for i in range(len(saida)):
        sys.stdout.write(saida[i])
