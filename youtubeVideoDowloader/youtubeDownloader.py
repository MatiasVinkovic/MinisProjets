import tkinter
import pytube

#creation de la fenetre
master = tkinter.Tk()
master.title("Youtube Mp3 downloader")
master.geometry("500x500")
master.minsize(500,500)
master.maxsize(500,500)
master.config(background="#1E2334")

#creation des fonctions

liste_link = []

def download_sound():
    liste_link.append(entryURL1.get())
    if entryURL2.get() != "":
        liste_link.append(entryURL2.get())
    if entryURL3.get()!= "":
        liste_link.append(entryURL3.get())
    print(liste_link)
    
    for links in liste_link:
        if links != "":
            pytube.YouTube(links).streams.filter(only_audio=True)[0].download(entryPath.get())
            print(pytube.YouTube(links).title+" téléchargé !")
    liste_link.clear()
    
    

#lien 1 = https://youtu.be/SBngx_tVpxg?list=RDLIFAx9vaXXU
#lien 2 = https://youtu.be/HqJ1qP05Si0?list=RDLIFAx9vaXXU
#lien 3 = https://youtu.be/Hpoo6R1JyKQ?list=RDLIFAx9vaXXU

#creation de l'UI

Title = tkinter.Label(master,text="Youtube Mp3 downloader by Matias ",bg="#1E2334",fg="red",font=('Calibri',20))
Title.pack(expand="YES")

entryPathLabel = tkinter.Label(master,text="Lien du répertoire où enregistrer les musiques : ",bg="#1E2334",fg="white",font=('Calibri',15))
entryPathLabel.pack()
entryPath = tkinter.Entry(master,fg="black",font=('Calibri',15))
entryPath.pack()

entryURLlabel = tkinter.Label(master,text="Liens des musiques",bg="#1E2334",fg="white",font=('Calibri',15))
entryURLlabel.pack()

#entries URL
entryURL1 = tkinter.Entry(master,fg="black",font=('Calibri',15))
entryURL1.pack()

entryURL2 = tkinter.Entry(master,fg="black",font=('Calibri',15))
entryURL2.pack()

entryURL3 = tkinter.Entry(master,fg="black",font=('Calibri',15))
entryURL3.pack()


#validate Button
validateButton = tkinter.Button(master,text="Télécharger le son",bg="white",fg="black",font=('Calibri',15),command=download_sound)
validateButton.pack(expand="YES")

tkinter.mainloop()