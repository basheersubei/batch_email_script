from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import csv

# read in emails, author names, and abstract titles from csv file
def read_csv_file(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        # for every abstract
        for (i, row) in enumerate(reader):

            # send email for every email in AuthorsEmail (for this abstract)
            for email in row['AuthorsEmail'].split(','):
                if email and email.strip():  # avoid empty emails
                    # TODO for now, I put the to-address to mine for testing
                    send_email("info@we-are-phi.com", "basheersubei@gmail.com", email, row['Title'], "accepted") 


# send email notification about abstract status to author
def send_email(fromaddr, toaddr, name, title, status):

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SIMEC2016 Abstract Notification"
    body = ''' 
Dear {},
Your abstract submission to SIMEC2016 titled "{}" has been {}. bla bla bla
'''.format(name, title, status)
     
    msg.attach(MIMEText(body, 'plain'))
    message = msg.as_string()


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # TODO replace fake password with real one
    server.login("info@we-are-phi.com", "notTheRealPassword")
    server.sendmail(fromaddr, toaddr, message)
    

if __name__ == '__main__':

    read_csv_file('AllAbstracts.csv')
