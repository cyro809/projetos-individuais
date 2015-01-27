#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Head(object):

    def le_comando(self, input_string):
        num_de_linhas = 10
        comando = input_string.split()[0]

        if comando != 'head':
                return u'Comando Invalido'
        elif comando == 'head' and len(input_string.split()) == 1:
                return u'Especifique um Arquivo'

        argumentos = input_string.split()[1:]
        if len(argumentos) == 1:
            nome_arquivo = argumentos[0]

        elif len(argumentos) == 2:
            flag = argumentos[0]

            if flag == '-n':
                nome_arquivo = argumentos[1]
            else:
                return u'Flag Desconhecida'

        elif len(argumentos) == 3:
            flag = argumentos[0]

            if flag == '-n':
                try:
                    num_de_linhas = int(input_string.split()[2])
                    nome_arquivo = argumentos[2]
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
    head = Head()

    for i in range(len(head.le_comando(raw_input()))):
        sys.stdout.write(head.le_comando()[i])
