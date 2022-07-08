import email.mime.text
import smtplib
import config


def send_email(sub, message):
    username = config.username
    password = config.password
    hostname = config.hostname
    mail_from = config.mail_from
    mail_to = config.mail_to

    msg = email.mime.text.MIMEText(message)
    msg['Subject'] = sub
    msg['From'] = mail_from
    msg['To'] = mail_to

    server = smtplib.SMTP(hostname, 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(
        mail_from,
        [mail_to],
        msg.as_string(),
    )
    server.close()


# send_mail('This is testing the subject', 'This is the body')
