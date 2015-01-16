#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time


input_string = raw_input()
comando = input_string.split()[0]

while comando != 'tail' or len(input_string.split()) == 1:
    print u'Commando não reconhecido. Por favor, tente novamente'

    input_string = raw_input()

    comando = input_string.split()

argumentos = input_string.split()[1:]

num_de_linhas = 10
flag = None

if len(argumentos) == 1:
    nome_arquivo = argumentos[0]
    arquivo = open(nome_arquivo, 'r')

elif len(argumentos) == 2:
    nome_arquivo = argumentos[1]
    arquivo = open(nome_arquivo, 'r')
    flag = argumentos[0]

    if flag != '-f':
        print 'Uso errado da flag'

elif len(argumentos) == 3:
    flag = argumentos[0]

    if flag == '-n':
        num_de_linhas = int(input_string.split()[2])
        nome_arquivo = argumentos[2]
    else:
        print u'flag não reconhecida!'
        exit()

    arquivo = open(nome_arquivo, 'r')

linhas = arquivo.readlines()
total_de_linhas = len(linhas)
linha_limite = total_de_linhas - num_de_linhas

for i in range(linha_limite, total_de_linhas):
    sys.stdout.write(linhas[i])

total_de_linhas_atual = total_de_linhas
if flag and flag == '-f':
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
