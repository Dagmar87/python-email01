import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

# Iniciar o servidor SMTP
host = "smtp.gmail.com"
port = "587"
login = "dagmar@iupay.com.br"
senha = "GunDamWinG87@"
server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.login(login,senha)

# Construção do email 
corpo = "<b>Meu é José Dagmar e estou testando o email feito com a linguagem de programação em Python</b>"
email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = 'jdfssobrinho@gmail.com'
email_msg['Subject'] = "Bem vindo ao teste de email em Python"
email_msg.attach(MIMEText(corpo,'html'))

cam_arquivo = "/home/dagmar87/python-projetos/python-email02/pythoncmd.pdf"
attachment = open(cam_arquivo,'rb')

att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition', f'attachment; filename=pythoncmd.pdf')
attachment.close()
email_msg.attach(att)

# Enviar o email no servidor SMTP
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()