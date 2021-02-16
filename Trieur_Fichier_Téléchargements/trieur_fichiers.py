import os 
import tkinter
import time
import getpass

#on récupère le nom d'utilisateur
nom_user = getpass.getuser()

#création du path pour changement de dossier
path_default = "C:\\Users\ "
downloads_end_chdir = "\Downloads"
x = path_default + nom_user + downloads_end_chdir
path_final_chdir = ""
for elements in x:
    if elements != " ":
        path_final_chdir+= elements
print(path_final_chdir)

#on accède au dossier Téléchargements
#print('avant : ',os.getcwd())
os.chdir(path_final_chdir)
#print('apres : ',os.getcwd())
#os.system('dir')

#on creer un affichage graphique
master = tkinter.Tk()
master.geometry("400x400")
master.minsize(400,400)
master.maxsize(400,400)
master.config(background='#585555')
master.title("Trieur du dossier Téléchargements")


#fonction qui trie les fichiers.exe/les setup dans un dossier
def trieur_setup():
    """fonction qui trie les fichiers.exe/les setup dans un dossier"""
    downloads_end_path_exe = "\Downloads\TRI_Fichiers_exe"
    x = path_default +nom_user+ downloads_end_path_exe
    path_final_exe = ""
    for elements in x:
        if elements != " ":
            path_final_exe+= elements
    commande_exe = 'move *.exe "' + path_final_exe + '"'
    commande_ts3 = 'move *.ts3_plugin "' + path_final_exe + '"'
    commande_zip = 'move *.zip "' + path_final_exe + '"'
    #print(commande_exe)
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_exe):
        print("dossier  exe déjà existant")
    else:
        os.mkdir(path_final_exe)
        print("Dossier pour setups non existant, création du dossier en cours")
    #on transfert les .exe dans le dossier correspondant
    os.system(commande_exe)
    os.system(commande_ts3)
    os.system(commande_zip)

#fonction qui trie les fichiers images dans un dossier
def trieur_image():
    """fonction qui trie les fichiers images dans un dossier"""
    #path pour fichiers images : 
    downloads_end_path_img = "\Downloads\TRI_Fichiers_images"
    y = path_default + nom_user + downloads_end_path_img
    path_final_img = ""
    for elements in y:
        if elements != " ":
            path_final_img+= elements
    commande_jpg = 'move *.jpg "' + path_final_img + '"'
    commande_jpeg = 'move *.jpeg "' + path_final_img + '"'
    commande_png = 'move *.png "' + path_final_img + '"'
    #print(commande_jpeg,commande_jpg)
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_img):
        print("dossier image déjà existant")
    else:
        os.mkdir(path_final_img)
        print("Dossier pour images non exisant, création du dossier en cours")
    #on transfert les .jpeg/.jpg dans le dossier correspondant
    os.system(commande_jpeg)
    os.system(commande_jpg)
    os.system(commande_png)

#fonction qui trie les fichiers texte dans un dossier
def trieur_texte():
    """fonction qui trie les fichiers texte dans un dossier"""
    downloads_end_path_txt = "\Downloads\TRI_Fichiers_Docs"
    x = path_default +nom_user+ downloads_end_path_txt
    path_final_txt = ""
    for elements in x:
        if elements != " ":
            path_final_txt+= elements
    commande_doc_x = 'move *.docx "' + path_final_txt + '"'
    commande_pdf = 'move *.pdf "' + path_final_txt + '"'
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_txt):
        print("dossier déjà existant")
    else:
        os.mkdir(path_final_txt)
        print("Dossier non existant, création du dossier en cours")
    os.system(commande_doc_x)
    os.system(commande_pdf)

#fonction qui trie les fichiers musique dans un dossier
def trieur_musique():
    """fonction qui trie les fichiers musique dans un dossier"""
    downloads_end_path_msq = "\Downloads\TRI_Fichiers_Musique"
    x = path_default +nom_user+ downloads_end_path_msq
    path_final_msq = ""
    for elements in x:
        if elements != " ":
            path_final_msq+= elements
    commande_mp3 = 'move *.mp3 "' + path_final_msq + '"'
    commande_sfk = 'move *.sfk "' + path_final_msq + '"'
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_msq):
        print("dossier déjà existant")
    else:
        os.mkdir(path_final_msq)
        print("Dossier non existant, création du dossier en cours")
    os.system(commande_mp3)
    os.system(commande_sfk)

#fonction qui trie les fichiers packages dans un dossier
def trieur_packages():
    """fonction qui trie les fichiers packages dans un dossier"""
    downloads_end_path_pack = "\Downloads\TRI_Fichiers_Packages"
    x = path_default +nom_user+ downloads_end_path_pack
    path_final_pack = ""
    for elements in x:
        if elements != " ":
            path_final_pack+= elements
    commande_msi = 'move *.msi "' + path_final_pack + '"'
    commande_jar = 'move *.jar "' + path_final_pack + '"'
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_pack):
        print("dossier déjà existant")
    else:
        os.mkdir(path_final_pack)
        print("Dossier non existant, création du dossier en cours")
    os.system(commande_msi)
    os.system(commande_jar)

def tout_trier():
    """fonction qui trie tout d'un coup"""
    trieur_setup()
    trieur_image()
    trieur_texte()
    trieur_musique()
    trieur_packages()

"""CREATION DE L'INTERFACE GRAPHIQUE"""

#bouton trier exe 
button_exe = tkinter.Button(master,text="Trier les fichiers exe/setup",font=30,command=trieur_setup,bg='#888585',fg='white')
button_exe.pack()

#bouton trier images
button_img = tkinter.Button(master,text="Trier les fichiers image : jpg/jpeg",font=30,command=trieur_image,bg='#888585',fg='white')
button_img.pack()

#bouton trier textes
button_txt = tkinter.Button(master,text="Trier les fichiers de texte",font=30,command=trieur_texte,bg='#888585',fg='white')
button_txt.pack()

#bouton trier musique
button_msq = tkinter.Button(master,text="Trier les fichiers musique",font=30,command=trieur_musique,bg='#888585',fg='white')
button_msq.pack()

#bouton trier packages
button_packg = tkinter.Button(master,text="Trier les fichiers packages",font=30,command=trieur_packages,bg='#888585',fg='white')
button_packg.pack()

#bouton TOUT TRIER
button_all = tkinter.Button(master,text="Tout trier",font=10,command=tout_trier, height = 4, width = 7,bg='#888585',fg='white')
button_all.pack(expand=1)

tkinter.mainloop()