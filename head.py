#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Head(object):
    def __init__(self, input_string):
        self.input_string = input_string
        self.comando = self.input_string.split()[0]
        self.num_de_linhas = 10
        self.flag = None
        self.argumentos = []
        self.arquivo = None
        self.nome_arquivo = None
        self.linhas_a_imprimir = None


    def le_comando(self):
        if self.comando != 'head' and len(self.input_string.split()) == 1:
                return u'Comando Invalido'
        elif self.comando == 'head' and len(self.input_string.split()) == 1:
                return u'Especifique um Arquivo'

        self.argumentos = self.input_string.split()[1:]
        if len(self.argumentos) == 1:
            self.nome_arquivo = self.argumentos[0]

        elif len(self.argumentos) == 2:
            self.flag = self.argumentos[0]

            if self.flag == '-n':
                self.nome_arquivo = self.argumentos[1]
            else:
                return u'Flag Desconhecida'
            
        elif len(self.argumentos) == 3:
            self.flag = self.argumentos[0]

            if self.flag == '-n':
                self.num_de_linhas = int(self.input_string.split()[2])
                self.nome_arquivo = self.argumentos[2]
            else:
                return u'Flag Deconhecida!'

        try:
            self.arquivo = open(self.nome_arquivo, 'r')
        except IOError:
            return 'Arquivo inexistente'
            

        return self.arquivo.readlines()[:self.num_de_linhas]

if __name__ == '__main__':
    head = Head(raw_input())

    for i in range(len(head.le_comando())):
        sys.stdout.write(head.le_comando()[i])
