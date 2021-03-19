
"""

a == b -> égalité
a = 2 b = 1 -> user
a = 1 b = 2 -> pc
a = 1 b = 3 -> user
a = 2 b = 3 -> pc
a = 3 b = 2 -> user


"""
usr_gagne = " Vous gagné ! "
usr_perd = " Vous perdez..."
usr_egal = " égalité !"
result = ""
pc_score = " SCORE DU PC : "
usr_score = " SCORE DU PC : "
x = 0
y = 0

def regles_jeu(choix_user,choix_pc):
    global result
    global pc_score
    global usr_score
    global x
    global y

    if choix_user == choix_pc:
        result = "Résultat de la manche : " + usr_egal
        print(usr_egal)

    #le joueur gagne
    elif choix_user == 2 and choix_pc == 1 or choix_user == 1 and choix_pc == 3 or choix_user == 3 and choix_pc == 2:
        result = "Résultat de la manche : " + usr_gagne
        print(result)
        x += 1
        usr_score = " VOTRE SCORE : " + str(x)

    #le joeur perd
    elif choix_user == 1 and choix_pc == 2 or choix_user == 2 and choix_pc == 3 or choix_user == 3 and choix_pc == 1:
        result = "Résultat de la manche : " + usr_perd
        print(result)
        y += 1
        pc_score = " SCORE DU PC : " + str(y)
