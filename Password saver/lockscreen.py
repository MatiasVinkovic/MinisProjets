import tkinter
import main_mdp_saver

#creation de la fenetre
master = tkinter.Tk()
master.title("ENTREZ VOTRE MOT DE PASSE")
master.geometry("400x200")
master.config(background="#1E2334")
master.minsize(400,200)
master.maxsize(400,200)

#creation des widgets
mdp = "password"
r = False

def good_pw():
    if str(pw_entry.get()) != mdp:
        print(False)
    else :
        master.destroy()
        r = True
        if r == True:
            print("page fermée")
        main_mdp_saver.run()


pw_label = tkinter.Label(master,text="Entrez un mot de passe : ",bg="#1E2334",fg="white",font=('Neutra Text Alt',15))
pw_label.pack()
pw_entry = tkinter.Entry(master,font=(60),show="*")
pw_entry.pack(expand='YES')

pw_button = tkinter.Button(master,text="Valider",font=('Neutra Text Alt',15),command=good_pw)
pw_button.pack()

#on affiche la fenetre
tkinter.mainloop()