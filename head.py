#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Head:
    def __init__(self):
        self.input_string = raw_input()
        self.comando = self.input_string.split()[0]
        self.num_de_linhas = 10
        self.flag = None
        self.argumentos = []

    def le_comando(self):
        while self.comando != 'head' or len(self.input_string.split()) == 1:
            print u'Commando não reconhecido. Por favor, tente novamente'

            self.input_string = raw_input()

            self.comando = self.input_string.split()

        self.argumentos = self.input_string.split()[1:]

        if len(self.argumentos) == 1:
            nome_arquivo = self.argumentos[0]

        elif len(self.argumentos) == 3:
            self.flag = self.argumentos[0]

            if self.flag == '-n':
                self.num_de_linhas = int(self.input_string.split()[2])
                nome_arquivo = self.argumentos[2]
            else:
                print u'flag não reconhecida!'
                exit()

        arquivo = open(nome_arquivo, 'r')

        for i in range(self.num_de_linhas):
                sys.stdout.write(arquivo.readline())


head = Head()
head.le_comando()
