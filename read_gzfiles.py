# coding: utf-8
# Uma forma de ler os arquivos GZ, 
# ou via class ou via os.popen ou subprocess
import os
import re
import gzip

# from default_list import emails


# TODO: Criar validação para DEB e RPM
log_dir = '/var/log/'

# l = ['zimbra.log.122.gz']
# l = ['zimbra.log.122.gz', 'zimbra.log.123.gz', 'zimbra.log.124.gz', 'zimbra.log.125.gz', 'zimbra.log.126.gz']

# TODO criar metodo que selecione ao executar o e-mail que sera verificado
# mail_address = emails[13]
# mail_address = emails[-1]

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
                                    # elif line[-1] == 'spam)':
                                    #     mail_spam.append(line[-1])
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
                                    # elif line[-1] == 'spam)':
                                    #     mail_spam.append(line[-1])
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
        print(e)






















def read_received_from(data_list, mail_address):

    mail_ok = []
    mail_spam = []
    msgok_id = []
    msgspam_id = []
    from_ok = []
    from_spam = []

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
                                        msgok_id.append(line[5]) # Coleta MAILID 67B7CE28D8:
                                    elif line[-1] == 'spam)':
                                        msgspam_id.append(line[5])
# COLETAR REMETENTES ENTREGUES
                    for item in file_path.splitlines():
                        line = item.split(" ")
                        # TODO PROCURO UM ITEM DE UMA LISTA msgok_id DENTRO DE ITENS DE OUTRA LISTA, E A FORAM QUE CONSEGUI FOI ESSA. INFELIZMENTE ESTA DEMORANDO CERCA DE 1MIN1/2 PARA TER O RETORNO.
                        for msi in msgok_id: # MAILID
                            for l in line:   # line LINHA DO ARQUIVO DE LOG l CADA ITEM DA LINHA DO ARQUIVO. EU PRECISO FAZER ISSO PARA QUE NA BUSCA COM O re.findall EU CONSIGA ENCONTRAR O TEXT QUE QUERO EM EXPECIFICO.
                                if msi in line:
                                    s = re.findall('postfix/qmgr', l)
                                    if s: # O FINAL DA BUSCA s ME RETORNA DUAS LINHAS DE ARQUIVOS, UMA INUTIL QUE SEU ULTIMO ITEM É removerd E A OUTRA COM A INFORMACAO QUE BUSCO from=<email@domain.com>,
                                        if not 'removed' == line[-1]:
# ['Mar', '12', '17:17:27', 'zimbra', 'postfix/qmgr[17874]:', '2F287E2982:', 'from=<nfe@hypera.com.br>,', 'size=54390,', 'nrcpt=1', '(queue', 'active)']
                                            from_address = line[6].replace('from=<', '').replace('>,', '')
                                            from_ok.append(from_address) # Add todos os remetentes no from_ok para comparar as quantidades depois tento o from_address como base unica, por isso o if not contiver no from_address
                                            if not from_address in mail_ok:
                                                mail_ok.append(from_address)
# EXIBINDO REMETENTES E QUANTIDADE DE E-MAILS RECEBIDOS POR REMETENTE
            if len(mail_ok) > 0:
                list(mail_address)
                m_a = mail_address[4:-1]

                print('')
                print(m_a)
                print('')
                for item in mail_ok:
                    print('%s: %s' % (item, from_ok.count(item)))

    except TypeError as e:
        pass

# read_received_to(l)
# read_received_from(l)