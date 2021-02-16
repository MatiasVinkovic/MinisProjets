import tkinter 
import send_mail
import time
from time import strftime

#https://github.com/MatiasVinkovic/Projet1

#récupération du temps en temps réel 
time = strftime("%Y-%m-%d %H:%M:%S")

#creation de la fenêtre
master = tkinter.Tk()
master.title("Matias gmail sender")
master.geometry("720x480")
master.maxsize(720,480)
master.minsize(720,480)

#récupération données dans entry

s_e = ""
r_e = ""
pw = ""
msg = ""

def recup_entree():
    """La fonction recup_entree récupère les données dans les entry box,
    les attribus à des variables, qui elles mêmes sont attribuées aux 
    variables utilisés dans send_email.py, importer de facon modulaire,
    pour etre utiliser en tant que id, pw etc... dans le mail final"""
    s_e = entry_from.get()
    r_e = entry_to.get()
    pw = entry_mdp.get()
    msg = entry_message.get()
    
    send_mail.send_email(s_e,r_e,pw,msg)
    print(f"from ",s_e," --- to ",r_e," --- txt : ",r_e,msg,"\n\n time = ",time)

#GUI de la page

#entry FROM 
title_from = tkinter.Label(master, text="Votre mail")
title_from.pack()

entry_from = tkinter.Entry(master)
entry_from.pack(expand=0)

#entry TO
title_TO= tkinter.Label(master, text="Email destinataire")
title_TO.pack()

entry_to = tkinter.Entry(master)
entry_to.pack(expand=0)

#entry message 
title_message= tkinter.Label(master, text="Votre message ci dessous : ")
title_message.pack()

entry_message = tkinter.Entry(master,font=30)
entry_message.pack()

#entry mdp
title_mdp= tkinter.Label(master, text="Votre mdp")
title_mdp.pack()

entry_mdp= tkinter.Entry(master,show="*")
entry_mdp.pack()

#validate button 
validate_button = tkinter.Button(master,text="Envoyer",font=40,command=recup_entree)
validate_button.pack()

#affichage de la page
tkinter.mainloop()