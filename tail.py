#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


class Tail(object):

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
        if self.comando == 'tail' and len(self.input_string.split()) == 1:
            return 'Especifique um Arquivo'

        self.argumentos = self.input_string.split()[1:]

        if len(self.argumentos) == 1:
            self.nome_arquivo = self.argumentos[0]

        elif len(self.argumentos) == 2:
            self.nome_arquivo = self.argumentos[1]
            self.flag = self.argumentos[0]

            if self.flag != '-f':
                return 'Flag Invalida'

        elif len(self.argumentos) == 3:
            self.flag = self.argumentos[0]

            if self.flag == '-n':
                try:
                    self.num_de_linhas = int(self.input_string.split()[2])
                except ValueError:
                    return 'Parametro Invalido'
                else:
                    self.nome_arquivo = self.argumentos[2]

            else:
                return u'flag não reconhecida!'

        self.arquivo = open(self.nome_arquivo, 'r')

        linhas = self.arquivo.readlines()
        total_de_linhas = len(linhas)
        linha_limite = total_de_linhas - self.num_de_linhas

        total_de_linhas_atual = total_de_linhas
        if self.flag and self.flag == '-f':
            contador = 0
            while True:
                total_de_linhas = total_de_linhas_atual
                self.arquivo = open(self.nome_arquivo, 'r')
                linhas = self.arquivo.readlines()
                total_de_linhas_atual = len(linhas)

                if total_de_linhas != total_de_linhas_atual:
                    ultima_linha = linhas[total_de_linhas_atual - 1]

                    self.linhas_a_imprimir.append(ultima_linha)
                    print ultima_linha

                    contador = 0
                else:
                    time.sleep(1)
                    contador = contador + 1

                if contador >= 7:
                    break

        return linhas[linha_limite:total_de_linhas]

if __name__ == '__main__':
    tail = Tail(raw_input())
