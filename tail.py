#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import argparse


def le_comando():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-n', nargs='?', required=False, default=10,type=int, action='store', const=10)
    arg_parser.add_argument('-r', action='store_true')
    arg_parser.add_argument('nome_arquivo')
    try:
        argumentos = arg_parser.parse_args(sys.argv[1:])
    except SystemExit:
        return 'Flag Invalida'        

    num_de_linhas = argumentos.n
    if not argumentos.nome_arquivo:
        if sys.argv[0] == 'tail.py':
            return 'Especifique um Arquivo'
    if argumentos.r:
        arquivo = open(argumentos.nome_arquivo, 'r')

        linhas = arquivo.readlines()
        linhas.reverse()

        return linhas

##    num_de_linhas = 10
##    flag = None
##    if len(sys.argv) == 1:
##        if sys.argv[0] == 'tail.py':
##            return 'Especifique um Arquivo'
##    if len(sys.argv) == 2:
##        nome_arquivo = sys.argv[1]
##
##    elif len(sys.argv) == 3:
##        nome_arquivo = sys.argv[2]
##        flag = sys.argv[1]
##
##        if flag != '-r':
##            return 'Flag Invalida'
##        elif flag == '-r':
##            arquivo = open(nome_arquivo, 'r')
##
##            linhas = arquivo.readlines()
##            linhas.reverse()
##
##            return linhas
##
##    elif len(sys.argv) == 4:
##        flag = sys.argv[1]
##
##        if flag == '-n':
##            try:
##                num_de_linhas = int(sys.argv[2])
##            except ValueError:
##                return 'Parametro Invalido'
##            else:
##                nome_arquivo = sys.argv[3]
##
##        else:
##            return u'flag não reconhecida!'
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
    linhas = le_comando()
    for linha in linhas:
        sys.stdout.write(linha)
