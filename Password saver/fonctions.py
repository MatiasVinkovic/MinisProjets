import csv

table = list(csv.reader(open("file.csv")))

def valide(l):
    """on valide les lignes de la table"""
    site_name = str(l[0])
    user_name = str(l[1])
    password = str(l[2])

    if l[0] == " ":
        exit("erreur dans le fichier csv")
    return [site_name,user_name,password]

table_valide = [valide(ligne) for ligne in table[1:]]

def write_line(site,username,password):
    """écrire une nouvelle ligne dans le fihier csv"""
    with open('file.csv','a') as f:
        f.write("\n"+ '"' + site + '"' +"," + 
            '"' + username + '"' +"," + '"' + password + '"')

def searchInfoBySiteName(site,table):
    """on recherche les informations (username et mot de passe) correspondant au site
        mit en paramètres"""
    global siteName
    siteName="introuvable"
    global un
    un = "introuvable"
    global pw
    pw = "introuvable"

    for elements in table:
        if elements[0] == site:
            siteName = elements[0]
            un = elements[1]
            pw = elements[2]
            return elements

