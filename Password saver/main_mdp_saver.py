import fonctions
import tkinter

def run():
    #création et paramètrage de la fenêtre
    master = tkinter.Tk()
    master.geometry("500x500")
    master.minsize(500,500)
    master.maxsize(500,500)
    master.config(background="#1E2334")
    master.title("Password saver")

    #creation des fonctions
    def get_entry(component):
        """recupere une ligne de entry"""
        recup = component.get()
        return recup

    def get_all_entries():
        """recupere site,username,password"""
        #on recupere les entries pour les rentrer dans le csv
        site_name = get_entry(entry_site)
        user_name = get_entry(entry_user)
        password = get_entry(entry_password)
        print(site_name,user_name,password)
        #on envoie les donnees dans la base de données csv
        fonctions.write_line(site_name,user_name,password)

    def search_infos(site):
        """aeaj"""
        print(fonctions.searchInfoBySiteName(str(site),fonctions.table_valide))
        site_search = fonctions.siteName
        username_search = fonctions.un
        password_search = fonctions.pw

        print("site : " + site_search)
        print("nom utilisateur :" + username_search)
        print("mot de passe: " + password_search)

        label_display_infos.config(text="Site :" + site_search + "\nNom d'utilisateur : " + username_search + "\nMot de passe : " + password_search)

    #boutons et widgets
    label_entry_site = tkinter.Label(master,text="Site : ",bg="#1E2334",fg="white",font=('Neutra Text Alt',15))
    label_entry_site.pack()
    entry_site = tkinter.Entry(master,font=('Neutra Text Alt',15))
    entry_site.pack()


    label_entry_user = tkinter.Label(master,text="Nom compte : ",bg="#1E2334",fg="white",font=('Neutra Text Alt',15))
    label_entry_user.pack()
    entry_user = tkinter.Entry(master,font=('Neutra Text Alt',15))
    entry_user.pack()

    label_entry_password = tkinter.Label(master,text="Mot de passe : ",bg="#1E2334",fg="white",font=('Neutra Text Alt',15))
    label_entry_password.pack()
    entry_password = tkinter.Entry(master,font=('Neutra Text Alt',15))
    entry_password.pack()

    button_get = tkinter.Button(master,text="Ajouter ces informations",command=get_all_entries,font=('Neutra Text Alt',15))
    button_get.pack(expand="YES")

    label_entry_search = tkinter.Label(master,text="Rechercher : ",bg="#1E2334",fg="white",font=('Neutra Text Alt',15))
    label_entry_search.pack()
    entry_search = tkinter.Entry(master,font=('Neutra Text Alt',15))
    entry_search.pack()

    button_search = tkinter.Button(master,text="Rechercher les informations",font=('Neutra Text Alt',15),command= lambda:search_infos(get_entry(entry_search)))
    button_search.pack(expand="YES")

    label_display_infos = tkinter.Label(master,bg="#1E2334",fg="red",font=('Neutra Text Alt',15))
    label_display_infos.pack()

    #code 
    #affichage de la fenetre
    tkinter.mainloop()
