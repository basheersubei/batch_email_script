from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

# TODO read in emails, author names, and abstract titles from csv file


def send_email(fromaddr, toaddr, text):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("info@we-are-phi.com", "notTheRealPassword")
    server.sendmail(fromaddr, toaddr, text)
    

if __name__ == '__main__':

    fromaddr = "info@we-are-phi.com"
    toaddr = "basheersubei@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Python test email"
    body = ''' 
Dear {},
Your abstract submission to SIMEC2016 titled "{}" has been {}. bla bla bla
'''.format('idiot', 'why doctors are not idiots', 'accepted')
    
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    send_email(fromaddr, toaddr, text)
