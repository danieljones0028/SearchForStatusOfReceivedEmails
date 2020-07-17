# coding: utf-8
# Lista com todos os arquivoz comprimidos GZ
# Uma forma de ler os arquivos GZ, ou via class ou via os.popen ou subprocess
# coletar informações de data de criacao E/OU modificação
# Pegando a ultima e a primeira lnha de cada arquivo seria possivel dizer o 
# periodo que contem no mesmo

import os
import time
from default_list import emails
import file_list
import read_gzfiles

# EXEMPLO DE ARQUIVO zimbra.log.XXX.gz ONDE XXX É O NUMERO DO ARQUIVO
inicio = raw_input('Coloque o numero incial aqui\n(Exemplo zimbra.log.XXX.gz, voce deve digitar o numero representado pelo XXX\n(NAO É PRECISO POR ZEROS A ESQUERDA)): ')

while(inicio.isdigit()) == False:
    inicio = raw_input('Coloque o numero incial aqui\n(Exemplo zimbra.log.XXX.gz, voce deve digitar o numero representado pelo XXX\n(NAO É PRECISO POR ZEROS A ESQUERDA)): ')
else:
    inicio = int(inicio)
    pass

final = raw_input('Coloque o numero final aqui\n(Exemplo zimbra.log.XXX.gz, voce deve digitar o numero representado pelo XXX\n(NAO É PRECISO POR ZEROS A ESQUERDA)): ')

while(final.isdigit()) == False:
    final = raw_input('Coloque o numero final aqui\n(Exemplo zimbra.log.XXX.gz, voce deve digitar o numero representado pelo XXX\n(NAO É PRECISO POR ZEROS A ESQUERDA)): ')
else:
    final = int(final)
    pass

endereco_email = raw_input(
    """
    Escolha o endereço de e-mail para verificação:
        1 nfe1@nazaria.com.br
        2 nfe2@nazaria.com.br
        3 nfe3@nazaria.com.br
        4 nfe4@nazaria.com.br
        5 nfe5@nazaria.com.br
        6 nfe6@nazaria.com.br
        7 nfe7@nazaria.com.br
        8 nfe8@nazaria.com.br
        9 nfe9@nazaria.com.br
        10 nfe10@nazaria.com.br
        11 nfe11@nazaria.com.br
        12 nfe12@nazaria.com.br
        13 nfe13@nazaria.com.br
        14 nfe14@nazaria.com.br
        15 nfe15@nazaria.com.br
        16 nfe16@nazaria.com.br
        17 nfe17@nazaria.com.br

Digite o numero correspondente ao endereço: """)

while(endereco_email.isdigit()) == False:
    endereco_email = raw_input(
    """
    Escolha o endereço de e-mail para verificação:
        1 nfe1@nazaria.com.br
        2 nfe2@nazaria.com.br
        3 nfe3@nazaria.com.br
        4 nfe4@nazaria.com.br
        5 nfe5@nazaria.com.br
        6 nfe6@nazaria.com.br
        7 nfe7@nazaria.com.br
        8 nfe8@nazaria.com.br
        9 nfe9@nazaria.com.br
        10 nfe10@nazaria.com.br
        11 nfe11@nazaria.com.br
        12 nfe12@nazaria.com.br
        13 nfe13@nazaria.com.br
        14 nfe14@nazaria.com.br
        15 nfe15@nazaria.com.br
        16 nfe16@nazaria.com.br
        17 nfe17@nazaria.com.br
    
Digite o numero correspondente ao endereço: """)
else:
    endereco_email = int(endereco_email)
    pass


# Emails recebidos e descartados
t1 = time.time()
m = emails[endereco_email].replace('from=<', '').replace('>,', '')
print('')
print('Email escolhido foi: %s' % m)

read_gzfiles.read_received_to(file_list.list_files(inicio, final), emails[endereco_email])

read_gzfiles.read_received_from(file_list.list_files(inicio, final), emails[endereco_email])

t2 = time.time()
print('')
print '%0.3f ms' % ((t2-t1)*1000.0)
tempo_decorrido = ((t2-t1)*1000.0/(1000*60))%60
print(tempo_decorrido)
print('')