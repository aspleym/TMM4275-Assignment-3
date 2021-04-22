import smtplib

gmail_user = 'wckbesolution@gmail.com'


def sendMailToClient(adress, password, projectName):
    sent_from = "WC Designer"
    to = adress
    subject = 'Your WC Design has been submitted'
    body = f"Your design {projectName} is now submitted and is waiting for a designer to process it"
    email_text = f"From: {sent_from}\nTo: {adress}\nSubject: {subject}\n{body}"

    if password:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, password)
            server.sendmail(sent_from, adress, email_text)
        except:
            print('The email could not be sent')


def sendMailToDesigner(adress, password, projectName):
    sent_from = "WC Company"
    to = adress
    subject = 'A new design has been submitted'
    body = f"A design called {projectName} was submitted a few seconds ago and is waiting for you to process it.\n\
        You can find it in the Products folder."
    email_text = f"From: {sent_from}\nTo: {adress}\nSubject: {subject}\n{body}"

    if password:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, adress, email_text)
        except:
            print('The email could not be sent')
