#! /usr/bin/python

# Importamos smtplib
import smtplib
 
# Importamos los módulos necesarios
from email.mime.text import MIMEText
 
# Creamos el mensaje
msg = MIMEText("Contenido del e-mail a enviar")
 
# Conexión con el server
msg['Subject'] = 'Asunto del correo'
msg['From'] = 'desdedonde@gmail.com'
msg['To'] = 'hastadonde@gmail.com'
 
# Autenticamos
mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login("desdedonde@gmail.com","password")
 
# Enviamos
mailServer.sendmail("desdedonde@gmail.com", "hastadonde@gmail.com", msg.as_string())
 
# Cerramos conexión
mailServer.close()
