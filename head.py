#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


input_string = raw_input()
comando = input_string.split()[0]

while comando != 'head' or len(input_string.split()) == 1:
    print u'Commando não reconhecido. Por favor, tente novamente'

    input_string = raw_input()

    comando = input_string.split()

argumentos = input_string.split()[1:]

num_de_linhas = 10
flag = None

if len(argumentos) == 1:
    nome_arquivo = argumentos[0]
    arquivo = open(nome_arquivo, 'r')

elif len(argumentos) == 3:
    flag = argumentos[0]

    if flag == '-n':
        num_de_linhas = int(input_string.split()[2])
        nome_arquivo = argumentos[2]
    else:
        print u'flag não reconhecida!'
        exit()

    arquivo = open(nome_arquivo, 'r')

for i in range(num_de_linhas):
        sys.stdout.write(arquivo.readline())
