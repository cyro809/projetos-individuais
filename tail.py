#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


def le_comando():
    num_de_linhas = 10
    flag = None
    if len(sys.argv) == 1:
        if sys.argv[0] == 'tail.py':
            return 'Especifique um Arquivo'
    if len(sys.argv) == 2:
        nome_arquivo = sys.argv[1]

    elif len(sys.argv) == 3:
        nome_arquivo = sys.argv[2]
        flag = sys.argv[1]

        if flag != '-r':
            return 'Flag Invalida'
        elif flag == '-r':
            arquivo = open(nome_arquivo, 'r')

            linhas = arquivo.readlines()
            linhas.reverse()

            return linhas

    elif len(sys.argv) == 4:
        flag = sys.argv[1]

        if flag == '-n':
            try:
                num_de_linhas = int(sys.argv[2])
            except ValueError:
                return 'Parametro Invalido'
            else:
                nome_arquivo = sys.argv[3]

        else:
            return u'flag não reconhecida!'
    try:
        arquivo = open(nome_arquivo, 'r')
    except IOError:
        return 'Arquivo Inexistente'
    else:
        linhas = arquivo.readlines()
        total_de_linhas = len(linhas)
        linha_limite = total_de_linhas - num_de_linhas

    return linhas[linha_limite:total_de_linhas]

if __name__ == '__main__':
    le_comando(raw_input())
