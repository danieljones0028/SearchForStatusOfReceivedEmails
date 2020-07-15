# coding: utf-8
# Uma forma de ler os arquivos GZ, 
# ou via class ou via os.popen ou subprocess
import os
import re
import gzip

from default_list import emails

# TODO: Criar validação para DEB e RPM
log_dir = '/var/log/'

l = ['zimbra.log.122.gz', 'zimbra.log.123.gz', 'zimbra.log.124.gz', 'zimbra.log.125.gz', 'zimbra.log.126.gz']
mail_address = emails[13]

def read_received_gz(data_list):

    mail_ok = []
    mail_spam = []
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

                        for l in line:
                            s = re.findall('postfix/lmtp', l)
                            if s:
                                if mail_address in line:
# ['Mar', '12', '17:06:21', 'zimbra', 'postfix/lmtp[9577]:', '67B7CE28D8:', 'to=<santil.santos@nazaria.com.br>,', 'relay=zimbra.nazaria.com.br[189.80.247.203]:7025,', 'delay=0.66,', 'delays=0.1/0/0.1/0.46,', 'dsn=2.1.5,', 'status=sent', '(250', '2.1.5', 'Delivery', 'OK)']
                                    if line[-1] == 'OK)':
                                        mail_ok.append(line[-1])
                                    elif line[-1] == 'spam)':
                                        mail_spam.append(line[-1])

            else:
                print('fiz + nao tinha nada')

        for rem in remetente:
            s = remetentes.count(rem)
            print('%s   = %s' % (s, rem))
        
        if len(mail_ok) > 0:
            list(mail_address)
            #TODO resolver caracteres no fim do m_a 
            # Foram recebidos 31 e-mails para a conta: nfe14@nazaria.com.br>.
            m_a = mail_address[4:-1]
            print('')
            print('Foram recebidos %s e-mails para a conta: %s.' % (len(mail_ok), m_a))
            print('')

        if len(mail_spam) > 0:
            list(mail_address)
            #TODO resolver caracteres no fim do m_a 
            # Foram recebidos 31 e-mails para a conta: nfe14@nazaria.com.br>.
            m_a = mail_address[4:-1]
            print('')
            print('Foram descartados %s e-mails para a conta: %s.' % (len(mail_ok), m_a))
            print('')

    except TypeError as e:
        print(e)
