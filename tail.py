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

    def le_comando(self):
        while self.comando != 'tail' or len(self.input_string.split()) == 1:
            print u'Commando não reconhecido. Por favor, tente novamente'

            self.input_string = raw_input()

            self.comando = self.input_string.split()

        self.argumentos = self.input_string.split()[1:]

        if len(self.argumentos) == 1:
            nome_arquivo = self.argumentos[0]
            arquivo = open(nome_arquivo, 'r')

        elif len(self.argumentos) == 2:
            nome_arquivo = self.argumentos[1]
            arquivo = open(nome_arquivo, 'r')
            self.flag = self.argumentos[0]

            if self.flag != '-f':
                print 'Uso errado da flag'

        elif len(self.argumentos) == 3:
            self.flag = self.argumentos[0]

            if self.flag == '-n':
                self.num_de_linhas = int(self.input_string.split()[2])
                nome_arquivo = self.argumentos[2]
            else:
                print u'flag não reconhecida!'
                exit()

            arquivo = open(nome_arquivo, 'r')

        linhas = arquivo.readlines()
        total_de_linhas = len(linhas)
        linha_limite = total_de_linhas - self.num_de_linhas

        for i in range(linha_limite, total_de_linhas):
            sys.stdout.write(linhas[i])

        total_de_linhas_atual = total_de_linhas
        if self.flag and self.flag == '-f':
            while True:
                total_de_linhas = total_de_linhas_atual
                arquivo = open(nome_arquivo, 'r')
                linhas = arquivo.readlines()
                total_de_linhas_atual = len(linhas)

                if total_de_linhas != total_de_linhas_atual:
                    ultima_linha = linhas[total_de_linhas_atual - 1]
                    print ultima_linha
                else:
                    time.sleep(5)


tail = Tail()

tail.le_comando()
