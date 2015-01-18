#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

class Tail:
    def __init__(self):
        self.input_string = raw_input()
        self.comando = self.input_string.split()[0]
        self.num_de_linhas = 10
        self.flag = None
        self.argumentos = []
        self.arquivo = None
        self.nome_arquivo = None
        self.linhas_a_imprimir = None

    def le_comando(self):
        while self.comando != 'tail' or len(self.input_string.split()) == 1:
            if self.comando != None:
                print u'Commando não reconhecido. Por favor, tente novamente'

            self.input_string = raw_input()

            self.comando = self.input_string.split()

        self.confere_argumentos()

    def confere_argumentos(self):
        self.argumentos = self.input_string.split()[1:]

        if len(self.argumentos) == 1:
            self.nome_arquivo = self.argumentos[0]

        elif len(self.argumentos) == 2:
            self.nome_arquivo = self.argumentos[1]
            self.flag = self.argumentos[0]

            if self.flag != '-f':
                print 'Uso errado da flag'

        elif len(self.argumentos) == 3:
            self.flag = self.argumentos[0]

            if self.flag == '-n':
                self.num_de_linhas = int(self.input_string.split()[2])
                self.nome_arquivo = self.argumentos[2]
            else:
                print u'flag não reconhecida!'
                exit()

        self.arquivo = open(self.nome_arquivo, 'r')

        self.imprimi_resultado()

    def imprimi_resultado(self):
        linhas = self.arquivo.readlines()
        total_de_linhas = len(linhas)
        linha_limite = total_de_linhas - self.num_de_linhas

        self.linhas_a_imprimir = linhas[linha_limite:total_de_linhas]

        for i in range(len(self.linhas_a_imprimir)):
            sys.stdout.write(self.linhas_a_imprimir[i])

        total_de_linhas_atual = total_de_linhas
        if self.flag and self.flag == '-f':
            while True:
                total_de_linhas = total_de_linhas_atual
                self.arquivo = open(self.nome_arquivo, 'r')
                linhas = self.arquivo.readlines()
                total_de_linhas_atual = len(linhas)

                if total_de_linhas != total_de_linhas_atual:
                    ultima_linha = linhas[total_de_linhas_atual - 1]
                    print ultima_linha
                else:
                    time.sleep(1)


tail = Tail()

tail.le_comando()
