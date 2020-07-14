# coding: utf-8
# Uma forma de ler os arquivos GZ, 
# ou via class ou via os.popen ou subprocess

import os
import gzip

# l = ['zimbra.log.1.gz', 'zimbra.log.2.gz', 'zimbra.log.3.gz']

l = ['syslog.2.gz', 'syslog.3.gz', 'syslog.4.gz']

# TODO: Criar validação para DEB e RPM
log_dir = '/var/log/'

def read_gz(data_list):

    try:
        for file in data_list:
            if os.path.exists('%s%s' % (log_dir, file)):
                with gzip.open('%s%s' % (log_dir, file), 'r') as file_path:
                    file_path = file_path.read()
                    # TODO: pegar primeira e ultima linha do arquivo para determinar o periodo que o mesmo tem os registros.
                    print(file_path)
            else:
                print('fiz + nao tinha nada')
    except TypeError as e:
        print(e)

read_gz(l)