# coding: utf-8
# Uma forma de ler os arquivos GZ, 
# ou via class ou via os.popen ou subprocess
import os
import gzip

from default_list import emails

# TODO: Criar validação para DEB e RPM
log_dir = '/var/log/'

def read_gz(data_list):

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

                        # emails[13] é o endereço do destinatario na linha da lista | to=<destination@email.com>
                        if emails[13] in line:
                            # tratando o endereço do rementente para que fique mais amigavel a leitura
                            remetentes_item = line[16].replace("from=<", "").replace(">", "")
                            remetentes.append(remetentes_item)
                            if not remetentes_item in remetente:
                                remetente.append(remetentes_item)

            else:
                print('fiz + nao tinha nada')

        for rem in remetente:
            s = remetentes.count(rem)
            print('%s   = %s' % (s, rem))

    except TypeError as e:
        print(e)
