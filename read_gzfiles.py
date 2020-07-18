# coding: utf-8
# Uma forma de ler os arquivos GZ, 
# ou via class ou via os.popen ou subprocess
import os
import re
import gzip

# from default_list import emails
# arquivo = ['zimbra.log.122.gz']
# TODO criar metodo que selecione ao executar o e-mail que sera verificado
# mail_address = emails[3]
# TODO: Criar validação para DEB e RPM
log_dir = '/var/log/'

def read_received_to(data_list, mail_address):

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
                            # s = re.findall('postfix/lmtp', l)
                            s = re.findall('postfix/lmtp', l)
                            if s:
                                if mail_address in line:
# ['Mar', '12', '17:06:21', 'zimbra', 'postfix/lmtp[9577]:', '67B7CE28D8:', 'to=<santil.santos@nazaria.com.br>,', 'relay=zimbra.nazaria.com.br[189.80.247.203]:7025,', 'delay=0.66,', 'delays=0.1/0/0.1/0.46,', 'dsn=2.1.5,', 'status=sent', '(250', '2.1.5', 'Delivery', 'OK)']

                                    if line[-1] == 'OK)':
                                        mail_ok.append(line[-1])

            else:
                print('fiz + nao tinha nada')

            if os.path.exists('%s%s' % (log_dir, file)):
                with gzip.open('%s%s' % (log_dir, file), 'r') as file_path:
                    # TODO: pegar primeira e ultima linha do arquivo para determinar o periodo que o mesmo tem os registros.
                    file_path = file_path.read()

                    for item in file_path.splitlines():
                        line = item.split(" ")

                        for l in line:
                            # s = re.findall('postfix/lmtp', l)
                            s = re.findall('postfix/smtp', l)
                            if s:
                                if mail_address in line:
# ['Mar', '12', '17:06:21', 'zimbra', 'postfix/lmtp[9577]:', '67B7CE28D8:', 'to=<santil.santos@nazaria.com.br>,', 'relay=zimbra.nazaria.com.br[189.80.247.203]:7025,', 'delay=0.66,', 'delays=0.1/0/0.1/0.46,', 'dsn=2.1.5,', 'status=sent', '(250', '2.1.5', 'Delivery', 'OK)']
                                    if line[-1] == 'spam)':
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
            print('Foram descartados %s e-mail(s) para a conta: %s.' % (len(mail_spam), m_a))
            print('')

    except TypeError as e:
        print('#############################DEU PAU###########################')
        print(e)

###############################################################################

def read_received_from(data_list, mail_address):

    msgid_ok = []
    msgid_spam = []
    remetente_ok = []
    remetente = []
    remetentes_ok = []
    remetentes = []

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
                            # s = re.findall('postfix/qmgr', l)
                            if s:
                                if mail_address in line:
# ['Mar', '12', '17:06:21', 'zimbra', 'postfix/lmtp[9577]:', '67B7CE28D8:', 'to=<santil.santos@nazaria.com.br>,', 'relay=zimbra.nazaria.com.br[189.80.247.203]:7025,', 'delay=0.66,', 'delays=0.1/0/0.1/0.46,', 'dsn=2.1.5,', 'status=sent', '(250', '2.1.5', 'Delivery', 'OK)']
                                    if line[-1] == 'OK)':
                                        msgid_ok.append(line[5])
    except TypeError as e:
        print('###############PAUPAUPAU###################')
        print(e)

    try:

        for file in data_list:
            if os.path.exists('%s%s' % (log_dir, file)):
                with gzip.open('%s%s' % (log_dir, file), 'r') as file_path:
                    # TODO: pegar primeira e ultima linha do arquivo para determinar o periodo que o mesmo tem os registros.
                    file_path = file_path.read().splitlines()
                    for item in file_path:
                        for msgid in msgid_ok:
                            z = re.findall('%s from=<' % msgid, item)
                            if z:
                                i = item.split(" ")
                                rem_ok = i[6].replace('from=<', '').replace('>,', '')
                                remetentes_ok.append(rem_ok)
                                if not rem_ok in remetente_ok:
                                    remetente_ok.append(rem_ok)

        if remetentes_ok > 0:
            print('')
            print('Remetentes aceitos:')
            print('')
            for r in remetente_ok:
                c = remetentes_ok.count(r)
                print('%s: %s' % (r, c))

    except TypeError as e:
        print('################DEU#####################')
        print(e)

# TODO criar funcao pra chamar so a lista e poupar linhas #####################
    try:
        for file in data_list:
            if os.path.exists('%s%s' % (log_dir, file)):
                with gzip.open('%s%s' % (log_dir, file), 'r') as file_path:
                    # TODO: pegar primeira e ultima linha do arquivo para determinar o periodo que o mesmo tem os registros.
                    file_path = file_path.read()
                    for item in file_path.splitlines():
                        line = item.split(" ")
###############################################################################
                        for l in line:
                            s = re.findall('postfix/smtp', l)
                            if s:
                                if mail_address in line:
# ['Mar', '12', '20:25:24', 'zimbra', 'postfix/smtp[29929]:', 'A16F1E2897:', 'to=<nfe3@nazaria.com.br>,', 'orig_to=<ti.comunicado@nazaria.com.br>,', 'relay=127.0.0.1[127.0.0.1]:10024,', 'delay=8.9,', 'delays=2/3.4/0.01/3.6,', 'dsn=2.7.0,', 'status=sent', '(250', '2.7.0', 'Ok,', 'discarded,', 'id=29060-17', '-', 'spam)']
                                    if line[-1] == 'spam)':
                                        msgid_spam.append(line[5])
    except TypeError as e:
        print('###############PAUPAUPAU###################')
        print(e)

    try:
        for file in data_list:
            if os.path.exists('%s%s' % (log_dir, file)):
                with gzip.open('%s%s' % (log_dir, file), 'r') as file_path:
                    # TODO: pegar primeira e ultima linha do arquivo para determinar o periodo que o mesmo tem os registros.
                    file_path = file_path.read()
                    for item in file_path.splitlines():
                        line = item.split(" ")
                        for msgid in msgid_spam:
                            for l in line:
                                # Consulta por item na lista line se existe o MAILID
                                # Isso filtra apenas as linhas que MAILD existe dentro do arquivo.
                                s = re.findall(msgid, l)
                                if s:
                                    for i in line:
                                        # 
                                        se = re.findall('from=<', i)
                                        if se:
                                            rem = line[6].replace('from=<', '').replace('>,', '')
                                            remetentes.append(rem)
                                            if not rem in remetente:
                                                remetente.append(rem)
# Lista os remetentes encontrados que foram marcados como SPAM.
        if remetentes > 0:
            print('')
            print('Remetentes bloqueados/descartados:')
            print('')
            for r in remetente:
                c = remetentes.count(r)
                print('%s: %s' % (r, c))
        print('')

    except TypeError as e:
        print('################DEU#####################')
        print(e)


# read_received_from(arquivo, 'to=<nfe3@nazaria.com.br>,')
