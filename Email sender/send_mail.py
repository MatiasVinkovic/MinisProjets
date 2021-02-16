import smtplib
#https://github.com/MatiasVinkovic/Projet1


def send_email(sender,receiver,mdp,mes):
    sender_email = sender
    rec_email = receiver
    password = mdp
    message = mes

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,password)
    print("LOGIN SUCCESS")
    server.sendmail(sender_email,rec_email,message)
    print("\n EMAIL SUCCESFULLY SENT")
