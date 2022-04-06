"""
Aurelien CORBLIN
Lynda CABALLERO AQUINO
Ulrich HAJAHARIMINA FENITRALA
"""

import fltk
import random


largeur = 1000  # ne pas aller en dessous de 850 car ce n'est pas jouable 
hauteur = 800  # ne pas aller en dessous de 300 car ce n'est pas jouable
################################################################################### page principal & fonctions

fltk.cree_fenetre(largeur, hauteur)

normal = False
misere = False
humain = False
ordi = False
CoupAutoriser = 3
nbrangées = 1


def CreeJeu(nbcolones = 1):
    """
    fonction qui cree une liste de liste pour representer le jeu.
    le nombres de liste dans la liste represente le nombres de lignes 
    du jeu , definit par le parametre nbcolones.

    :param nbcolones: int, qui designe le nombres de lignes 

    >>>CreeJeu()
    >>>3
    [["I", "I", "I"]]

    >>>CreeJeu(3)
    >>>1
    >>>5
    >>>3
    [["I"], ["I", "I", "I", "I", "I"], ["I", "I", "I"]]

    """
    jeu = []
    for i in range(nbcolones):
        lst = []
        n = -1
        while n <= 0:
            n = int(input(f"nombres d'allumettes sur la colone {i + 1} ? "))
        for a in range(n):
            lst.append('I')
        jeu.append(lst)
    return jeu

def CoupPossible(lst, CoupAutoriser, coupjoueur, modejeu = 'normal'):
    """"
    fonction qui prend en parametre un jeu , les coup autoriser , le coup 
    du joueur ainsi que le mode de jeu pour pouvoir derterminer si le 
    coup du joueur est possible.

    :param lst: list, liste de liste representant le jeu
    :param coupautoriser: int, nombre d'objet pouvant etre retirer
    :param coupjoueur: int, tuple, coup que le joueur veut faire
    :param modejeu: str, le mode de jeu dans lequelle on joue

    >>>CoupPossible([["I", "I", "I", "I"]], 3, 3, 'normal')
    True
    >>>CoupPossible([["I", "I", "I", "I"]], 3, 4, 'normal')
    False
    >>>CoupPossible([["I", "I", "I", "I"], ["I", "I", "I"], ["I", "I"]], 3, (2, 3), 'marienbad')
    True
    >>>CoupPossible([["I", "I", "I", "I"], ["I", "I", "I"], ["I", "I"]], 3, (3, 4), 'marienbad')
    False
    """
    nbRetirer = coupjoueur
    if modejeu == 'normal':
        return len(lst[0]) >= coupjoueur and nbRetirer <= CoupAutoriser and nbRetirer > 0
    colone, nbRetirer = coupjoueur
    if modejeu == 'marienbad' and len(lst) >= colone:
        return len(lst[colone - 1]) > 0 and nbRetirer > 0 and nbRetirer <= len(lst[colone - 1])

def JouerCoup(lst, CoupAutoriser, coupjoueur, modejeu = 'normal'):
    """
    fonction qui joue le coup en prenant en compte la fonction couppossible
    pour savoir si le coup est possible et le jouer si il est, et renvoyer 
    none sinon.

    :param lst: list, liste de liste representant le jeu
    :param coupautoriser: int, nombre d'objet pouvant etre retirer
    :param coupjoueur: int, tuple, coup que le joueur veut faire
    :param modejeu: str, le mode de jeu dans lequelle on joue

    >>>JouerCoup([["I", "I", "I", "I"]], 3, 3, 'normal')
    True
    >>>JouerCoup([["I", "I", "I", "I"]], 3, 4, 'normal')
    None
    >>>JouerCoup([["I", "I", "I", "I"], ["I", "I", "I"], ["I", "I"]], 3, (2, 3), 'marienbad')
    True
    >>>JouerCoup([["I", "I", "I", "I"], ["I", "I", "I"], ["I", "I"]], 3, (3, 4), 'marienbad')
    None
    """
    if modejeu == 'normal':
        if CoupPossible(lst, CoupAutoriser, coupjoueur):
            for i in range(coupjoueur):
                lst[0].pop()
            return True
    elif modejeu == 'marienbad':
        colone, nbRetirer = coupjoueur
        if CoupPossible(lst, CoupAutoriser, coupjoueur, 'marienbad'):
            for i in range(nbRetirer):
                lst[colone-1].pop()
            return True

def gagnant(lst):
    """
    fonction qui sert a determiner si le joueur a gagner en 
    verifiant si les listes dans la liste sont vides

    :param lst: list, liste de liste representant le jeu

    >>>gagnant([["I", "I"]])
    False
    >>>gagnant([[],[]])
    True
    """
    cpt = len(lst)
    for i in range (len(lst)):
        if len (lst[i]) == 0:
            cpt -= 1
    return cpt == 0

def dessin(x, y):
    """
    fonction qui dessine un rectangle en fonction de x et y 
    pour les coordonnées du rectangle.

    :param x: int
    :param y: int
    """
    fltk.rectangle(x, y, x + 5, y + (hauteur // 2 ) //len(jeu), remplissage='black', tag='obj')

def affichejeu(jeu):
    """
    fonction qui utilise la fonction dessin pour afficher 
    le jeu en le representant par des rectangles.

    :param jeu: list, liste de liste qui represente le jeu
    """
    x = 10
    y = 100
    n = (hauteur - 100) // len(jeu)
    for i in range(len(jeu)):
        b = largeur // (len(jeu[i]) + 1)
        x = 10
        for a in range(len(jeu[i])):
            dessin(x, y)
            x += b
        y += n



while True:
    fltk.rectangle(0, 0, largeur, hauteur, remplissage="gray")
    fltk.rectangle((largeur // 2) - 100, (hauteur // 2) - 25, (largeur // 2) + 100, (hauteur // 2) + 25, remplissage='green')
    fltk.texte(largeur // 2, hauteur // 2, "jouer", ancrage='center')
    fltk.rectangle(largeur - 110, 10, largeur - 10, 60, remplissage='black')
    fltk.texte(largeur - 60, 35, "settings", ancrage='center', taille= 20, couleur='white')
    fltk.rectangle((largeur // 2) - 100, (hauteur // 2) + 50, (largeur // 2) + 100, (hauteur // 2) + 100, remplissage="red")
    fltk.texte(largeur // 2, (hauteur // 2) + 75, "quitter", ancrage='center')

###################################################################################

    x, y = fltk.attend_clic_gauche()
    if x > (largeur // 2) - 100 and x < (largeur // 2) + 100 and y > (hauteur // 2) + 50 and y < (hauteur // 2) + 100:
        fltk.ferme_fenetre()
    if x > largeur - 110 and x < largeur - 10 and y > 10 and y < 60:
        fltk.ferme_fenetre()
        fltk.cree_fenetre(1000, 800)

        ################################################################################### page reglage

        fltk.rectangle(0, 0, 1000, 800, remplissage='gray')
        fltk.rectangle(50, 700, 150, 750, remplissage='red')
        fltk.texte(100, 725, "retour", ancrage='center')
        fltk.texte(50, 50, "mode de victoire : ")
        if normal == True:
            fltk.rectangle(400, 50, 600, 100, remplissage='green')
        else:
            fltk.rectangle(400, 50, 600, 100, remplissage='red')
        fltk.texte(500, 75, "normal", ancrage='center')
        if misere == True:
            fltk.rectangle(700, 50, 900, 100, remplissage='green')
        else:    
            fltk.rectangle(700, 50, 900, 100, remplissage='red')
        fltk.texte(800, 75, 'misere', ancrage='center')
        fltk.texte(50, 150, "adversaire : ")
        if humain == True:
            fltk.rectangle(400, 150, 600, 200, remplissage='green')
        else: 
            fltk.rectangle(400, 150, 600, 200, remplissage='red')
        fltk.texte(500, 175, "humain", ancrage='center')
        if ordi == True:
            fltk.rectangle(700, 150, 900, 200, remplissage='green')
        else:
            fltk.rectangle(700, 150, 900, 200, remplissage='red')
        fltk.texte(800, 175, "ordi", ancrage='center')
        fltk.texte(50, 250, "coup autoriser : ")
        fltk.rectangle(450, 250, 500, 300, remplissage='green')
        fltk.texte(475, 275, "-", ancrage='center')
        fltk.rectangle(750, 250, 800, 300, remplissage='green')
        fltk.texte(775, 275, "+", ancrage='center')
        fltk.texte(625, 275, CoupAutoriser, ancrage='center', tag='coupautoriser')
        fltk.texte(50, 350, "nombres de rangées : ")
        fltk.rectangle(450, 350, 500, 400, remplissage='green')
        fltk.texte(475, 375, "-", ancrage='center')
        fltk.rectangle(750, 350, 800, 400, remplissage='green')
        fltk.texte(775, 375, "+", ancrage='center')
        fltk.texte(625, 375, nbrangées, ancrage='center', tag='nbrangees')
        fltk.texte(50, 420, "* pour jouer en mode marienbad il suffit de mettre 2 ou plus sur \
le nombre de rangées.", taille=15)
        fltk.texte(50, 450, "  le nombres d'allumettes par rangées sera a saisir dans le terminal", taille=15)


        while True:
            xclic, yclic= fltk.attend_clic_gauche()
            if xclic > 50 and xclic < 150 and yclic > 700 and yclic < 750:
                fltk.ferme_fenetre()
                fltk.cree_fenetre(largeur, hauteur)
                break
            if xclic > 400 and xclic < 600 and yclic > 50 and yclic < 100:
                normal = not normal
                if normal == True and misere == False:
                    fltk.rectangle(400, 50, 600, 100, remplissage='green')
                    fltk.texte(500, 75, "normal", ancrage='center')
                else:
                    fltk.rectangle(400, 50, 600, 100, remplissage='red')
                    fltk.texte(500, 75, "normal", ancrage='center')
                    normal = False
                
            if xclic > 700 and xclic < 900 and yclic > 50 and yclic < 100:
                misere = not misere
                if misere == True and normal == False:
                    fltk.rectangle(700, 50, 900, 100, remplissage='green')
                    fltk.texte(800, 75, 'misere', ancrage='center')
                else:
                    fltk.rectangle(700, 50, 900, 100, remplissage='red')
                    fltk.texte(800, 75, 'misere', ancrage='center')
                    misere = False
            
            if xclic > 400 and xclic < 600 and yclic > 150 and yclic < 200:
                humain = not humain
                if humain == True and ordi == False:
                    fltk.rectangle(400, 150, 600, 200, remplissage='green')
                    fltk.texte(500, 175, "humain", ancrage='center')
                else:
                    fltk.rectangle(400, 150, 600, 200, remplissage='red')
                    fltk.texte(500, 175, "humain", ancrage='center')
                    humain = False

            if xclic > 700 and xclic < 900 and yclic > 150 and yclic < 200:
                ordi = not ordi
                if ordi == True and humain == False:
                    fltk.rectangle(700, 150, 900, 200, remplissage='green')
                    fltk.texte(800, 175, "ordi", ancrage='center')
                else:
                    fltk.rectangle(700, 150, 900, 200, remplissage='red')
                    fltk.texte(800, 175, "ordi", ancrage='center')
                    ordi = False

            if xclic > 450 and xclic < 500 and yclic > 250 and yclic < 300:
                if CoupAutoriser > 1:
                    CoupAutoriser -= 1
            if xclic > 750 and xclic < 800 and yclic > 250 and yclic < 300:
                if CoupAutoriser < 99:
                    CoupAutoriser += 1
            fltk.efface('coupautoriser')
            fltk.texte(625, 275, CoupAutoriser, ancrage='center', tag='coupautoriser')

            if xclic > 450 and xclic < 500 and yclic > 350 and yclic < 400:
                if nbrangées > 1:
                    nbrangées -= 1
            if xclic > 750 and xclic < 800 and yclic > 350 and yclic < 400:
                if nbrangées < 99:
                    nbrangées += 1

            fltk.efface('nbrangees')
            fltk.texte(625, 375, nbrangées, ancrage='center', tag='nbrangees')

            
            fltk.mise_a_jour()

        ###################################################################################
    
    if x > (largeur // 2) - 100 and x < (largeur // 2) + 100 and y > (hauteur // 2) - 25 and\
    y < (hauteur // 2) + 25 and (normal == True or misere == True) and (humain == True or ordi == True):
        jeu = CreeJeu(nbrangées)
        retirerobj = 1
        jouercolone = 1
        cpt = 1

        if ordi == True and nbrangées == 1:
            if (len(jeu[0]) % (CoupAutoriser + 1) != 0) and normal == True:
                cpt = 2
            elif len(jeu[0]) % (CoupAutoriser + 1) != 1 and misere == True:
                cpt = 2        

        while True:
            fltk.efface_tout()
            fltk.rectangle(0, 0, largeur, hauteur, remplissage='gray')
            fltk.texte(480, 10, 'mode misere:', taille=15)
            if misere:
                fltk.texte(600, 10, 'on', couleur='green', taille=15)
            else:
                fltk.texte(600, 10, 'off', couleur='red', taille=15)
            if cpt % 2 == 0 and humain == True:
                fltk.texte(650, 10, "au tour du joueur 2", taille=15)
            elif cpt % 2 != 0 and humain == True:
                fltk.texte(650, 10, "au tour du joueur 1", taille=15)
            if cpt % 2 != 0 and ordi == True:
                fltk.texte(650, 10, "au tour du joueur", taille=15)
            fltk.texte(10, 10, "nb d'objets a retirer : ", taille=15)
            fltk.rectangle(200, 10, 220, 30, remplissage='green')
            fltk.texte(210, 20, '-', ancrage='center', taille=15)
            fltk.rectangle(250, 10, 270, 30, remplissage='green')
            fltk.texte(260, 20, '+', ancrage='center', taille=15)
            fltk.texte(222, 10, retirerobj, taille=15, tag='obj')
            fltk.rectangle(450, 40, 550, 80, remplissage='green')
            fltk.texte(500, 60, 'validé', ancrage='center')
            if nbrangées >= 2:
                fltk.texte(290, 10, "rangée : ", taille=15)
                fltk.rectangle(360, 10, 380, 30, remplissage='green')
                fltk.texte(370, 20, '-', ancrage='center', taille=15)
                fltk.rectangle(420, 10, 440, 30, remplissage='green')
                fltk.texte(430, 20, '+', ancrage='center', taille=15)
                fltk.texte(395, 10, jouercolone, taille=15, tag='col')

            affichejeu(jeu)

            x, y = fltk.attend_clic_gauche()
            if x > 200 and x < 220 and y > 10 and y < 30:
                if retirerobj > 1:
                    retirerobj -= 1
            if x > 250 and x < 270 and y > 10 and y < 30:
                if retirerobj < CoupAutoriser or (nbrangées >= 2 and retirerobj < len(jeu[jouercolone - 1])):
                    retirerobj += 1
            
            if nbrangées >= 2 and x > 360 and x < 380 and y > 10 and y < 30:
                if jouercolone > 1:
                    jouercolone -= 1
                    retirerobj = 1
            if nbrangées >= 2 and x > 420 and x < 440 and y > 10 and y < 30:
                if jouercolone < len(jeu):
                    jouercolone += 1
                    retirerobj = 1


            if humain == True:
                if nbrangées >= 2:
                    if x > 450 and x < 550 and y > 40 and y < 80:
                        cpt += 1
                        if len(jeu[jouercolone-1]) == 0:
                            print ("il n'y a plus d'allumettes dans cette rangée !")
                        coupjoueur = jouercolone, retirerobj
                        possible = JouerCoup(jeu, CoupAutoriser, coupjoueur, 'marienbad')
                        if possible == None:
                            cpt -= 1
                        if misere == True:
                            if gagnant(jeu):
                                if cpt % 2 == 0:
                                   print('joueur 2 gagné')
                                else:
                                    print('joueur 1 gagné')
                                break
                        else:
                            if gagnant(jeu):
                                if cpt % 2 == 0:
                                    print('joueur 1 gagné')
                                else:
                                    print('joueur 2 gagné')
                                break
                elif nbrangées == 1:
                    if x > 450 and x < 550 and y > 40 and y < 80:
                        cpt += 1
                        if len(jeu[jouercolone-1]) == 0:
                            print ("il n'y a plus d'allumettes dans cette rangée !")
                        possible = JouerCoup(jeu, CoupAutoriser, retirerobj, 'normal')
                        if possible == None:
                            cpt -= 1
                        if misere == True:
                            if gagnant(jeu):
                                if cpt % 2 == 0:
                                    print('joueur 2 gagné')
                                else:
                                    print('joueur 1 gagné')
                                break
                        else:
                            if gagnant(jeu):
                                if cpt % 2 == 0:
                                    print('joueur 1 gagné')
                                else:
                                    print('joueur 2 gagné')
                                break
            
            if ordi == True:
                if nbrangées >= 2:
                    if x > 450 and x < 550 and y > 40 and y < 80:    
                        cpt += 1
                        if len(jeu[jouercolone-1]) == 0:
                            print ("il n'y a plus d'allumettes dans cette rangée !")
                        coupjoueur = jouercolone, retirerobj
                        possible = JouerCoup(jeu, CoupAutoriser, coupjoueur, 'marienbad')
                        if possible == None:
                            cpt -= 1
                        if misere == True:
                            if gagnant(jeu):
                                if cpt % 2 == 0:
                                   print('ordi a gagné')
                                   break
                        else:
                            if gagnant(jeu):
                                if cpt % 2 == 0:
                                    print('joueur a gagné')
                                    break
                    
                    if cpt % 2 == 0:
                        cpt += 1
                        choix_ligne =  random.randint(1, len(jeu) )

                        while  len (jeu[choix_ligne - 1]) == 0 :
                            choix_ligne =  random.randint(1, len(jeu) )

                        coup= random.randint (1, len(jeu[choix_ligne - 1]))
                        jeu_ordi=  choix_ligne , coup 
                        possible = JouerCoup (jeu, CoupAutoriser, jeu_ordi,  'marienbad')

                        while possible == None  :
                            choix_ligne =  random.randint(1, len(jeu) )
                            while  len (jeu[choix_ligne - 1]) == 0 :
                                choix_ligne =  random.randint(1, len(jeu) )
                            coup= random.randint (1, len(jeu[choix_ligne - 1]))
                            jeu_ordi=  choix_ligne , coup 
                            possible = JouerCoup (jeu, CoupAutoriser, jeu_ordi,  'marienbad')

                        print (f'ordi a pris {coup} dans la ligne {choix_ligne} ')
                        if misere == True:
                            if gagnant(jeu):
                                print(f'joueur a gagné')
                                break
                        else:
                            if gagnant(jeu):
                                print(f'ORDI a gagné')
                                break
                elif nbrangées == 1:
                    if cpt % 2 != 0:
                        if x > 450 and x < 550 and y > 40 and y < 80:
                            cpt += 1
                            if len(jeu[jouercolone-1]) == 0:
                                print ("il n'y a plus d'allumettes dans cette rangée !")
                            possible = JouerCoup(jeu, CoupAutoriser, retirerobj, 'normal')
                            if possible == None:
                                cpt -= 1
                            if misere == True:
                                if gagnant(jeu):
                                    if cpt % 2 == 0:
                                        print('ordi a gagné')
                                        break
                            else:
                                if gagnant(jeu):
                                    if cpt % 2 == 0:
                                        print('joueur a gagné')
                                        break
                    
                    if cpt % 2 == 0:
                        cpt += 1
                        if normal == True:
                            if  len(jeu[0]) % (CoupAutoriser+1) != 0 :
                                coup_ordi = random.randint(1,CoupAutoriser)
                                while (len(jeu[0]) - coup_ordi  ) % (CoupAutoriser+1) != 0:
                                    coup_ordi= random.randint(1,CoupAutoriser)
                            else:
                                coup_ordi= random.randint(1,CoupAutoriser)
                            possible = JouerCoup(jeu, CoupAutoriser,coup_ordi,  'normal' )
                            while possible == None:
                                if  len(jeu[0]) % (CoupAutoriser+1) != 0 :
                                    coup_ordi= random.randint(1,CoupAutoriser)
                                    while (len(jeu[0]) - coup_ordi ) % (CoupAutoriser+1) != 0:
                                        coup_ordi= random.randint(1,CoupAutoriser)
                                else:
                                    coup_ordi= random.randint(1,CoupAutoriser)
                                possible = JouerCoup(jeu, CoupAutoriser,coup_ordi, 'normal' )
                            if gagnant(jeu):
                                print(f' ORDI a gagner')
                                break   
                            print(f'il reste {len(jeu[0])} allumettes')
                        
                        if misere == True:
                            print ('Au tour de ordi')
                            if  len(jeu[0]) % (CoupAutoriser+1) != 1 :
                                coup_ordi = random.randint(1,CoupAutoriser)
                                while (len(jeu[0]) - coup_ordi  ) % (CoupAutoriser+1) != 1:
                                    coup_ordi= random.randint(1,CoupAutoriser)
                            else:
                                coup_ordi= random.randint(1,CoupAutoriser)
                            possible = JouerCoup(jeu, CoupAutoriser,coup_ordi,  'normal' )
                            while possible == None:
                                if  len(jeu[0]) % (CoupAutoriser+1) != 1 :
                                    coup_ordi= random.randint(1,CoupAutoriser)
                                    while (len(jeu[0]) - coup_ordi ) % (CoupAutoriser+1) != 1:
                                        coup_ordi= random.randint(1,CoupAutoriser)
                                else:
                                    coup_ordi= random.randint(1,CoupAutoriser)
                                possible = JouerCoup(jeu, CoupAutoriser,coup_ordi, 'normal' )
                            print ()
                            if gagnant(jeu):
                                print(f' ORDI a gagner')
                                break   
                            print(f'il reste {len(jeu[0])} allumettes')

    fltk.efface_tout()
