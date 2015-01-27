#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Head(object):
    def __init__(self, input_string):
        self.input_string = input_string
        self.comando = self.input_string.split()[0]

    def le_comando(self):
        num_de_linhas = 10

        if self.comando != 'head':
                return u'Comando Invalido'
        elif self.comando == 'head' and len(self.input_string.split()) == 1:
                return u'Especifique um Arquivo'

        argumentos = self.input_string.split()[1:]
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
                    num_de_linhas = int(self.input_string.split()[2])
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
    head = Head(raw_input())

    for i in range(len(head.le_comando())):
        sys.stdout.write(head.le_comando()[i])
