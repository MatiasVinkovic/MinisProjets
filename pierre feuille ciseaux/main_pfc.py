import tkinter
import random
import fonctions_pfc
import time

#creation de la fenêtre
master = tkinter.Tk()
master.geometry("720x480")
master.maxsize(720,480)
master.minsize(720,480)
master.config(background="#895E42")

#importation des images
largeur = 300
hauteur = 300
image_boutonPierre = tkinter.PhotoImage(file="pierre.gif").zoom(20).subsample(40)
image_boutonFeuille = tkinter.PhotoImage(file="papier.gif").zoom(20).subsample(40)
image_boutonCiseaux = tkinter.PhotoImage(file="ciseaux.gif").zoom(20).subsample(40)


usr_choice = 0
time_wait = 2000
x = "bonjour"


#DISPLAY ET UNDISPLAY DES ELEMENTS DE L'ECRAN

#UNDISPLAY
def undisplay_pack_component():
    """ retirer tout ce qu'il y a à l'écran"""
    label_pierre.pack_forget()
    boutonPierre.pack_forget()
    label_feuille.pack_forget()
    boutonFeuille.pack_forget()
    label_ciseaux.pack_forget()
    boutonCiseaux.pack_forget()
    boutonJouer.pack_forget()
    LabelResultats.pack_forget()
    LabelScorePc.pack_forget()
    LabelScoreJoueur.pack_forget()
#DISPLAY
def display_pack_component():
    """on affiche tous les composants à l'écran"""
    boutonEnd.pack_forget()
    bouttonHome.pack_forget()
    label_pierre.pack()
    boutonPierre.pack()
    label_feuille.pack()
    boutonFeuille.pack()
    label_ciseaux.pack()
    boutonCiseaux.pack()
    boutonJouer.pack()
    LabelResultats.pack(expand="YES")
    LabelScorePc.pack(side='left')
    LabelScoreJoueur.pack(side='right')

def clickPierre():
    global usr_choice
    usr_choice = 1
    print("votre choix : ",usr_choice)
    disable()

def clickFeuille():
    global usr_choice
    usr_choice = 2
    print("votre choix : ",usr_choice)
    disable()

def clickCiseaux():
    global usr_choice
    usr_choice = 3
    print("votre choix : ",usr_choice)
    disable()

def jeu():
    pc_choice = random.randint(1,3)
    print("le joueur choisit : ", usr_choice)
    print("le pc choisit : ", pc_choice)
    fonctions_pfc.regles_jeu(usr_choice,pc_choice)
    enable()

    #on affiche si le joueur perd ou gagne
    LabelResultats.config(text=fonctions_pfc.result)

    #on affiche le score du pc
    LabelScorePc.config(text=fonctions_pfc.pc_score)
    LabelScoreJoueur.config(text=fonctions_pfc.usr_score)

    #FIXER LA LIMITE DU SCORE POUR GAGNER -->le premier arrivé à 10 à gagner
    if fonctions_pfc.y == 5:
        print("le pc a gagné la partie ! ")
        undisplay_pack_component()
        boutonEnd.pack(expand='YES')
    elif fonctions_pfc.x == 5:
        print("le joueur a gagné la partie ! ")
        undisplay_pack_component()
        boutonEnd.pack(expand='YES')

def goToZero():
    usr_choice = 0
    fonctions_pfc.x = 0
    fonctions_pfc.y = 0
    result = ""
    fonctions_pfc.pc_score = " SCORE DU PC : "
    fonctions_pfc.usr_score = " SCORE DU PC : "

    display_pack_component()



def disable():
    boutonPierre["state"] = "disabled"
    boutonFeuille["state"] = "disabled"
    boutonCiseaux["state"] = "disabled"

def enable():
    boutonPierre["state"] = "normal"
    boutonFeuille["state"] = "normal"
    boutonCiseaux["state"] = "normal"



#création et insertion des Label/boutons
label_pierre = tkinter.Label(master,text="Pierre",bg="#895E42",fg="white")

boutonPierre = tkinter.Button(master,text="Pierre",image=image_boutonPierre,command=clickPierre)

label_feuille = tkinter.Label(master,text="Feuille",bg="#895E42",fg="white")

boutonFeuille = tkinter.Button(master,image=image_boutonFeuille,command=clickFeuille)

label_ciseaux = tkinter.Label(master,text="Ciseaux",bg="#895E42",fg="white")

boutonCiseaux = tkinter.Button(master,image=image_boutonCiseaux,command=clickCiseaux)

#BOUTONS NON JOUABLES, cad afficher resultat, et valider le coup
boutonJouer = tkinter.Button(master,text="MONTRER",fg="white",bg="#895E42",command=jeu)

LabelResultats = tkinter.Label(master,fg="white",bg="#895E42",font=40)

#afficher les scores à l'écran
LabelScorePc = tkinter.Label(master,fg="white",bg="#895E42",font=40)

LabelScoreJoueur = tkinter.Label(master,fg="white",bg="#895E42",font=40)


#PAGE ACCUEIL AVEC BOUTON JOUER
bouttonHome = tkinter.Button(master,text="LANCER LE JEU ! ",bg="#895E42",fg="white",font=100,command=display_pack_component)
bouttonHome.pack()

#PAGE FINAL AVEC AFFICHAGE NOM DU VAINQUEUR, AINSI QUE LE BOUTON POUR PRENDRE UNE REVANCHE
boutonEnd = tkinter.Button(master,text="PRENEZ VOTRE REVANCHE ICI !",bg="#895E42",fg="white",font=100,command= goToZero)


#affichage final de la fenêtre
tkinter.mainloop()
