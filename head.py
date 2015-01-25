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
        while self.comando != 'head':
            if self.comando:
                print u'Commando não reconhecido. Por favor, tente novamente'

            self.input_string = raw_input()

            self.comando = self.input_string.split()[0]

        self.argumentos = self.input_string.split()[1:]
        if len(self.argumentos) == 1:
            self.nome_arquivo = self.argumentos[0]

        elif len(self.argumentos) == 3:
            self.flag = self.argumentos[0]

            if self.flag == '-n':
                self.num_de_linhas = int(self.input_string.split()[2])
                self.nome_arquivo = self.argumentos[2]
            else:
                print u'flag não reconhecida!'
                exit()

        self.arquivo = open(self.nome_arquivo, 'r')

        self.linhas_a_imprimir = self.arquivo.readlines()[:self.num_de_linhas]
        for i in range(self.num_de_linhas):
                sys.stdout.write(self.linhas_a_imprimir[i])

if __name__ == '__main__':
    head = Head(raw_input())

    head.le_comando()
