import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Email-Adressen und Passwort über User-Input festlegen
absender = input("Geben sie ihre Mail-Adresse ein: ")
passwort = input("Password: ")
empfänger = input("Geben sie den Empfänger an: ")

#Betreff und Text der Mail
betreff = "TEST"
text = """
Hallo
Das ist ein Test
"""

#Funktion zum anhängen von Dateien
def anhang():
    q = input("Anhang: ja oder nein? ")
    if q.lower() == "ja":
        file = input("Welche Datei möchten sie anhängen? ")
        with open(file, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
                
        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {file}",
        )
                
        mail.attach(part)
    
#mit vorherigen Eingaben Mail generieren
mail = MIMEMultipart()
mail.attach(MIMEText(text))
mail['Subject'] = betreff
mail["From"] = absender
mail['To'] = empfänger
anhang()

#Mail mit SMTP versenden
server = smtplib.SMTP('SMTP.office365.com:587')
server.starttls()
server.login(absender, passwort)
server.send_message(mail)
server.quit()