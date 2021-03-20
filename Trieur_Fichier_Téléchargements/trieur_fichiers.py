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
master.config(background='#1E2334')
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
    commande_wav = 'move *.wav "' + path_final_msq + '"'
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_msq):
        print("dossier déjà existant")
    else:
        os.mkdir(path_final_msq)
        print("Dossier non existant, création du dossier en cours")
    os.system(commande_mp3)
    os.system(commande_sfk)
    os.system(commande_wav)

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

#fonction qui trie les fichiers videos dans un dossier
def trieur_videos():
    """fonction qui trie les fichiers musique dans un dossier"""
    downloads_end_path_msq = "\Downloads\TRI_Fichiers_Video"
    x = path_default +nom_user+ downloads_end_path_msq
    path_final_msq = ""
    for elements in x:
        if elements != " ":
            path_final_msq+= elements
    commande_mp4 = 'move *.mp4 "' + path_final_msq + '"'
    commande_avi = 'move *.avi "' + path_final_msq + '"'
    commande_mov = 'move *.mov "' + path_final_msq + '"'
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_msq):
        print("dossier déjà existant")
    else:
        os.mkdir(path_final_msq)
        print("Dossier non existant, création du dossier en cours")
    os.system(commande_mp4)
    os.system(commande_avi)
    os.system(commande_mov)

#fonction qui trie les fichiers de polices d'ecriture dans un dossier
def trieur_font():
    """fonction qui trie les fichiers font dans un dossier"""
    downloads_end_path_msq = "\Downloads\TRI_Fichiers_Polices_Ecriture"
    x = path_default +nom_user+ downloads_end_path_msq
    path_final_msq = ""
    for elements in x:
        if elements != " ":
            path_final_msq+= elements
    commande_otf = 'move *.otf "' + path_final_msq + '"'
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_msq):
        print("dossier déjà existant")
    else:
        os.mkdir(path_final_msq)
        print("Dossier non existant, création du dossier en cours")
    os.system(commande_otf)

#fonction qui trie les fichiers de code (py,c) dans un dossier
def trieur_codeFile():
    """fonction qui trie les fichiers py,c, dans un dossier"""
    downloads_end_path_msq = "\Downloads\TRI_Fichiers_CodeFiles"
    x = path_default +nom_user+ downloads_end_path_msq
    path_final_msq = ""
    for elements in x:
        if elements != " ":
            path_final_msq+= elements
    commande_py = 'move *.py "' + path_final_msq + '"'
    commande_c = 'move *.c "' + path_final_msq + '"'
    #on vérifie si un fichier existe déjà, sinon on le créer
    if os.path.exists(path_final_msq):
        print("dossier déjà existant")
    else:
        os.mkdir(path_final_msq)
        print("Dossier non existant, création du dossier en cours")
    os.system(commande_py)
    os.system(commande_c)

#tout trier
def tout_trier():
    """fonction qui trie tout d'un coup"""
    trieur_setup()
    trieur_image()
    trieur_texte()
    trieur_musique()
    trieur_packages()
    trieur_font()
    trieur_videos()

"""
#creation de la bar de menu
menu_bar = tkinter.Menu(master)
#creation des menus interieurs
file_menu = tkinter.Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Fichier")
menu_bar.add_cascade(label="Fichier", menu=file_menu)
"""

"""CREATION DE L'INTERFACE GRAPHIQUE"""

#bouton trier exe 
button_exe = tkinter.Button(master,text="Trier les fichiers exe/setup",font=('Calibri',11),command=trieur_setup,bg='white',fg='black')
button_exe.pack(expand=0.25)

#bouton trier images
button_img = tkinter.Button(master,text="Trier les fichiers image : jpg/jpeg",font=('Calibri',11),command=trieur_image)
button_img.pack(expand=0.25)

#bouton trier textes
button_txt = tkinter.Button(master,text="Trier les fichiers de texte",font=('Calibri',11),command=trieur_texte)
button_txt.pack(expand=0.25)

#bouton trier musique
button_msq = tkinter.Button(master,text="Trier les fichiers musique",font=('Calibri',11),command=trieur_musique)
button_msq.pack(expand=0.25)

#bouton trier packages
button_packg = tkinter.Button(master,text="Trier les fichiers packages",font=('Calibri',11),command=trieur_packages)
button_packg.pack(expand=0.25)

#bouton trier vidéos
button_video = tkinter.Button(master,text="Trier les fichiers vidéos",font=('Calibri',11),command=trieur_videos)
button_video.pack(expand=0.25)

#bouton trier font
button_font = tkinter.Button(master,text="Trier les fichiers Polices d'écriture",font=('Calibri',11),command=trieur_font)
button_font.pack(expand=0.25)

#bouton TOUT TRIER
button_all = tkinter.Button(master,text="Tout trier",font=('Calibri',11),command=tout_trier, height = 4, width = 7)
button_all.pack(expand=1)

#master.config(menu=menu_bar)
tkinter.mainloop()