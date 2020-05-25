import smtplib

sender = "Private Person <from@smtp.mailtrap.io>"
receiver = "A Test User <to@smtp.mailtrap.io>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}
is it working?
This is a test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("d4fba62757cd84", "f6d0cff236a0c9")
    server.sendmail(sender, receiver, message)
