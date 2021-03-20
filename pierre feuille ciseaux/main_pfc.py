import tkinter
import random
import fonctions_pfc
import time
from tkinter import font

#creation de la fenêtre
master = tkinter.Tk()
master.geometry("720x480")
master.maxsize(720,480)
master.minsize(720,480)
master.title("Jeu du Pierre Feuille Ciseaux")
master.config(background="#895E42")

#importation des images
largeur = 300
hauteur = 300
image_boutonPierre = tkinter.PhotoImage(file="pierre.gif").zoom(20).subsample(40)
image_boutonFeuille = tkinter.PhotoImage(file="papier.gif").zoom(20).subsample(40)
image_boutonCiseaux = tkinter.PhotoImage(file="ciseaux.gif").zoom(20).subsample(40)
image_boutonHome = tkinter.PhotoImage(file="bouton_jouer.png").zoom(40).subsample(40)

#initialisation du choix du joueur par défault = 0
usr_choice = 0


#DISPLAY ET UNDISPLAY DES ELEMENTS DE L'ECRAN

#UNDISPLAY
def undisplay_pack_component():
    """ retirer tout ce qu'il y a à l'écran"""
    label_reprise_jeu.pack_forget()
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
    whatPlayerDoes_Button.pack_forget()
    whatPcDoes_Button.pack_forget()
    label_usr_plays.pack_forget()
    label_pc_plays.pack_forget()

#DISPLAY
def display_pack_component():
    """on affiche tous les composants à l'écran"""
    boutonEnd.pack_forget()
    bouttonHome.pack_forget()
    label_reprise_jeu.pack()
    label_pierre.pack()
    boutonPierre.pack()
    label_feuille.pack()
    boutonFeuille.pack()
    label_ciseaux.pack()
    boutonCiseaux.pack()
    boutonJouer.pack()

    label_usr_plays.pack(side='right')
    whatPlayerDoes_Button.pack(side="right")

    label_pc_plays.pack(side="left")
    whatPcDoes_Button.pack(side="left")

    LabelResultats.pack(expand="YES")
    LabelScorePc.pack(side='left')
    LabelScoreJoueur.pack(side='right')


def clickPierre():
    """action cliquer sur bouton pierre"""
    global usr_choice
    usr_choice = 1
    print("votre choix : ",usr_choice)
    disable()

def clickFeuille():
    """action cliquer sur bouton feuille/papier"""
    global usr_choice
    usr_choice = 2
    print("votre choix : ",usr_choice)
    disable()

def clickCiseaux():
    """action cliquer sur bouton ciseaux"""
    global usr_choice
    usr_choice = 3
    print("votre choix : ",usr_choice)
    disable()


def jeu():
    """fonction principale qui lance le jeu/contient le code principale"""

    #le pc choisit un nombre
    pc_choice = random.randint(1,3)

    #on change l'image en fonction de ce que montre le pc
    if pc_choice == 1:
        whatPcDoes_Button.config(image = image_boutonPierre)
    elif pc_choice == 2:
        whatPcDoes_Button.config(image = image_boutonFeuille)
    else:
        whatPcDoes_Button.config(image = image_boutonCiseaux)

    #on change l'image en fonction de ce que montre le joueur
    if usr_choice == 1:
        whatPlayerDoes_Button.config(image = image_boutonPierre)
    elif usr_choice == 2:
        whatPlayerDoes_Button.config(image = image_boutonFeuille)
    else:
        whatPlayerDoes_Button.config(image = image_boutonCiseaux)

    #actions sur la console
    print("le joueur choisit : ", usr_choice)
    print("le pc choisit : ", pc_choice)
    #application des règles du jeu
    fonctions_pfc.regles_jeu(usr_choice,pc_choice)
    #on réactive les boutons pierre feuille et ciseaux
    enable()

    #on affiche si le joueur perd ou gagne
    LabelResultats.config(text=fonctions_pfc.result)

    #on affiche le score du pc
    LabelScorePc.config(text=fonctions_pfc.pc_score,font=("Berlin Sans FB Demi",15))
    LabelScoreJoueur.config(text=fonctions_pfc.usr_score,font=("Berlin Sans FB Demi",15))

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
    """fonction de reboot du jeu"""
    #on remet tout à zero
    usr_choice = 0
    fonctions_pfc.x = 0
    fonctions_pfc.y = 0
    fonctions_pfc.result = ""
    fonctions_pfc.pc_score = " SCORE DU PC : "
    fonctions_pfc.usr_score = " SCORE DU PC : "
    #on ré-affiche tous les composants
    display_pack_component()

#fonctions bloquer/débloquer les boutons
def disable():
    """bloquer les boutons pierre feuille et ciseaux"""
    boutonPierre["state"] = "disabled"
    boutonFeuille["state"] = "disabled"
    boutonCiseaux["state"] = "disabled"

def enable():
    """bloquer les boutons pierre feuille et ciseaux"""
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
boutonJouer = tkinter.Button(master,text="MONTRER",fg="white",bg="#895E42",font=("Berlin Sans FB Demi",10),command=jeu)

LabelResultats = tkinter.Label(master,fg="white",bg="#895E42",font=("Berlin Sans FB Demi",15))

#afficher les scores à l'écran
LabelScorePc = tkinter.Label(master,fg="white",bg="#895E42",font=("Berlin Sans FB Demi",15))

LabelScoreJoueur = tkinter.Label(master,fg="white",bg="#895E42",font=("Berlin Sans FB Demi",15))


#PAGE ACCUEIL AVEC BOUTON JOUER
bouttonHome = tkinter.Button(master,text="LANCER LE JEU ! ",image=image_boutonHome,bg="#895E42",fg="white",font=font.Font(family='Arial', size=30),command=display_pack_component)
bouttonHome.pack(expand="yes")

#PAGE FINAL AVEC AFFICHAGE NOM DU VAINQUEUR, AINSI QUE LE BOUTON POUR PRENDRE UNE REVANCHE
boutonEnd = tkinter.Button(master,text="PRENEZ VOTRE REVANCHE ICI !",bg="#895E42",fg="white",font=("Berlin Sans FB Demi",30),command= goToZero)
label_reprise_jeu = tkinter.Label(master,text="JEU DU PIERRE FEUILLE CISEAUX ",bg="#895E42",fg="white",font=("Berlin Sans FB Demi",15))


#que joue le pc ?
whatPcDoes_Button = tkinter.Label(master)
label_pc_plays = tkinter.Label(master,text="LE PC JOUE : ",bg="#895E42",fg="white",font=("Berlin Sans FB Demi",15))


#que joue le joueur ?
whatPlayerDoes_Button = tkinter.Label(master)
label_usr_plays = tkinter.Label(master,text="VOUS JOUEZ : ",bg="#895E42",fg="white",font=("Berlin Sans FB Demi",15))

#affichage final de la fenêtre
tkinter.mainloop()