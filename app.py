# coding: utf-8
# Lista com todos os arquivoz comprimidos GZ
# Uma forma de ler os arquivos GZ, ou via class ou via os.popen ou subprocess
# coletar informações de data de criacao E/OU modificação
# Pegando a ultima e a primeira lnha de cada arquivo seria possivel dizer o 
# periodo que contem no mesmo

import os
import file_list
import read_gzfiles

inicio = raw_input('Coloque o numero incial aqui: ')

while(inicio.isdigit()) == False:
    inicio = raw_input('Coloque o numero incial aqui: ')
else:
    inicio = int(inicio)
    pass

final = raw_input('Coloque o numero final aqui: ')

while(final.isdigit()) == False:
    final = raw_input('Coloque o numero final aqui: ')
else:
    final = int(final)
    pass


read_gzfiles.read_received_gz(file_list.list_files(inicio, final))
