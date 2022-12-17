from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'email_sender@example.com'
email_password = 'your_password'
email_receiver = 'email_receiver'
subject = 'your_subject'
body = 'Hello, this mail is sent via python -esy!'

em = EmailMessage()
em['from'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
