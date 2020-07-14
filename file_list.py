# coding: utf-8
# Lista com todos os arquivoz comprimidos GZ
# Uma forma de ler os arquivos GZ, ou via class ou via os.popen ou subprocess
# coletar informações de data de criacao E/OU modificação
# Pegando a ultima e a primeira lnha de cada arquivo seria possivel dizer o 
# periodo que contem no mesmo

import os

def list_files(start, end):
    # Criando lista com todos os arquivos
    files_gz = []
    # Por que 182? é o numero de arquivos configurado no logrotate do servidor.
    for item in range(start, end):
        files_gz.append('zimbra.log.%s.gz' % item)

    return files_gz
