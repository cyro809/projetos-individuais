#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


class Tail(object):

    def __init__(self, input_string):
        self.input_string = input_string

    def le_comando(self):
        comando = self.input_string.split()[0]
        num_de_linhas = 10
        flag = None
        nome_arquivo = None
        linhas_a_imprimir = None

        if comando == 'tail' and len(self.input_string.split()) == 1:
            return 'Especifique um Arquivo'

        argumentos = self.input_string.split()[1:]

        if len(argumentos) == 1:
            nome_arquivo = argumentos[0]

        elif len(argumentos) == 2:
            nome_arquivo = argumentos[1]
            flag = argumentos[0]

            if flag != '-f':
                return 'Flag Invalida'

        elif len(argumentos) == 3:
            flag = argumentos[0]

            if flag == '-n':
                try:
                    num_de_linhas = int(self.input_string.split()[2])
                except ValueError:
                    return 'Parametro Invalido'
                else:
                    nome_arquivo = argumentos[2]

            else:
                return u'flag não reconhecida!'

        arquivo = open(nome_arquivo, 'r')

        linhas = arquivo.readlines()
        total_de_linhas = len(linhas)
        linha_limite = total_de_linhas - num_de_linhas

        total_de_linhas_atual = total_de_linhas
        if flag and flag == '-f':
            contador = 0
            while True:
                total_de_linhas = total_de_linhas_atual
                arquivo = open(nome_arquivo, 'r')
                linhas = arquivo.readlines()
                total_de_linhas_atual = len(linhas)

                if total_de_linhas != total_de_linhas_atual:
                    ultima_linha = linhas[total_de_linhas_atual - 1]

                    linhas_a_imprimir.append(ultima_linha)
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
