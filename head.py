#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Head:
    def __init__(self):
        self.input_string = None
        self.comando = None
        self.num_de_linhas = 10
        self.flag = None
        self.argumentos = []
        self.arquivo = None
        self.nome_arquivo = None

    def le_comando(self):
        while self.comando != 'head' or len(self.input_string.split()) == 1:
            if self.comando != None:
                print u'Commando não reconhecido. Por favor, tente novamente'

            self.input_string = raw_input()

            self.comando = self.input_string.split()[0]

        
        
        self.confere_argumentos()
        

    def confere_argumentos(self):
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
        self.imprime_resultado()

    def imprime_resultado(self):
        for i in range(self.num_de_linhas):
                sys.stdout.write(self.arquivo.readline())


head = Head()
#head.le_comando()
