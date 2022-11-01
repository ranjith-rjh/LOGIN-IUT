import os
clear = lambda : os.system('cls')

dict_USMB = {
    "path_Intranet"   : "https://cas-uds.grenet.fr/login?service=https%3A%2F%2Fintranet.univ-smb.fr%2F",
    "path_Moodle" : "https://cas-usmb.grenet.fr/login?service=https%3A%2F%2Fmoodle.univ-smb.fr%2Flogin%2Findex.php%3FauthCAS%3DCAS",
    "path_Scodoc" : "https://cas-uds.grenet.fr/login?service=https%3A%2F%2Fnotes.iut-acy.univ-smb.fr%2Fservices%2FdoAuth.php%3Fhref%3Dhttps%253A%252F%252Fnotes.iut-acy.univ-smb.fr%252F",
    "labelUtilisateur" : "username",
    "labelMDP" : "password",
    "bouttonConnexion" : "btn-submit",

    "boutonMessagerie" : "Messagerie",
    "boutonPlanning" : "Planning des cours",

    "labelPlanning" : "x-auto-33-input"
}

def AfficherMenuChoix() : 
    clear()
    print("=================================================================")
    print("||             PROGRAMME INFORMATIQUE AUTO LOGIN DE :          ||")
    print("=================================================================")
    print("||      __________                    __.__  __  .__           ||")
    print("||      \______   \_____    ____     |__|__|/  |_|  |__        ||")
    print("||       |       _/\__  \  /    \    |  |  \   __\  |  \       ||")
    print("||       |    |   \ / __ \|   |  \   |  |  ||  | |   Y  \      ||")
    print("||       |____|_  /(____  /___|  /\__|  |__||__| |___|  /      ||")
    print("||              \/      \/     \/\______|             \/       ||")
    print("=================================================================")
    print("Choix : ")
    print("=================================================================")
    print(" ==>   0. Quitter")
    print(" ==>   1. Intranet")
    print(" ==>   2. Moodle")
    print(" ==>   3. ScoDoc")
    print("=================================================================")
    choixUser = int(input("Votre choix : "))
    print("=================================================================")
    return choixUser
