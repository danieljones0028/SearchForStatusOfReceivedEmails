# coding: utf-8
# Uma forma de ler os arquivos GZ, 
# ou via class ou via os.popen ou subprocess

import os
import gzip

# l = ['zimbra.log.1.gz', 'zimbra.log.2.gz', 'zimbra.log.3.gz']

l = ['zimbra.log.123.gz']

# TODO: Criar validação para DEB e RPM
log_dir = '/var/log/'

def read_gz(data_list):

    emails = ['to=<nfe1@nazaria.com.br>', 'to=<nfe2@nazaria.com.br>', 'to=<nfe3@nazaria.com.br>', 'to=<nfe4@nazaria.com.br>', 'to=<nfe5@nazaria.com.br>', 'to=<nfe6@nazaria.com.br>', 'to=<nfe7@nazaria.com.br>', 'to=<nfe8@nazaria.com.br>', 'to=<nfe9@nazaria.com.br>', 'to=<nfe10@nazaria.com.br>', 'to=<nfe11@nazaria.com.br>', 'to=<nfe12@nazaria.com.br>', 'to=<nfe13@nazaria.com.br>', 'to=<nfe14@nazaria.com.br>', 'to=<nfe15@nazaria.com.br>', 'to=<nfe16@nazaria.com.br>', 'to=<nfe17@nazaria.com.br>', 'to=<recepcionistarn@nazaria.com.br>']

    remetente = [] # Adiciona apenas 1x um endereço de remetente
    remetentes = []# Adiciona endereço de remetente sempre que ele aperecer

    try:
        for file in data_list:
            if os.path.exists('%s%s' % (log_dir, file)):
                with gzip.open('%s%s' % (log_dir, file), 'r') as file_path:
                    # TODO: pegar primeira e ultima linha do arquivo para determinar o periodo que o mesmo tem os registros.
                    file_path = file_path.read()

                    for item in file_path.splitlines():
                        line = item.split(" ")
                        mes = line[0]
                        day = line[1]
                        hora = line[2]
                        if emails[13] in line:
                            remetentes.append(line[16])
                            if not line[16] in remetente:
                                remetente.append(line[16])
                            # print(line)
                            # print(len(line))
                            # print(line[16], line[17])
                            # if emails[-1] in line:
                                # print(len(line))
                                # print(line)
#                                 print("""
# From Host: %s
# Hostname: %s
# Remetente: %s
# Destinatario: %s
# """) % (line[9], line[19], line[20], line[21])

            else:
                print('fiz + nao tinha nada')
        print(len(remetentes))
        print(len(remetente))

        for rem in remetente:
            print remetentes.count(rem)

    except TypeError as e:
        print(e)

read_gz(l)