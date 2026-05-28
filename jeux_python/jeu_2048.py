# Compléter ici (MASSALA Ines , groupe MI22, contenu fichier Binairo, 02/12/2025)
#
#
#
#
# Ne pas supprimer cette ligne. <trace>jeu_2048.py</trace>


####################
# Jeu du 2048
####################
def saisie_nom()->str:
    """ Demande la saisie d'un nom

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nom=input("joueur 1 Saisissez votre nom: ")
    while nom=="":
        nom=input("Nom vide,recommencer: ")
    return nom

def init_grille(n:int)->list[list[int]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    res=[]
    i=0
    while i<n:
        res.append([0]*n)
        i+=1
    return res

def afficher_grille(g:list[list[str]])->None:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    n = len(g)
    for i in range(n):
        for j in range(n):
            print(f"{g[i][j]:4}", end=" | ")
        print()
    
    
def perdu(grille:list[list[str]])->bool:
    """ Renvoie True si il n'ya plus de cases libres

    Précondition :
    Exemple(s) :
    $$$ perdu([[1,2,0,4],[3,4,0,0],[6,8,9,7],[0,0,3,3]])
    False
    $$$ perdu([[1,2,3,4],[3,4,3,2],[6,8,9,7],[1,3,3,3]])
    True
    """
    for ligne in grille:
        for case in ligne:
            if case == 0:
                return False
    return True
        
def gagner(grille:list[list[str]])->bool:
    """ renvoie True si il y a une valeur 2048

    Précondition :
    Exemple(s) :
    $$$ gagner([[1,2048,3,4],[3,4,5,6],[6,8,9,7],[4,5,3,3]])
    True
    $$$ gagner([[1,2,0,4],[3,4,0,0],[6,8,9,7],[0,0,3,3]])
    False
    """
    for ligne in grille:
        for case in ligne:
            if case == 2048:
                return True
    return False
        
from random import randint
from random import choice
def ajoute_tuile(grille:list[list[int]])->list[list[int]]:
    """Ajoute une seule tuile (2 ou 4) sur une case vide aléatoire."""
    vide = []
    i = 0
    while i < len(grille):
        j = 0
        while j < len(grille[i]):
            if grille[i][j] == 0:
                vide.append((i,j))
            j += 1
        i += 1

    if len(vide) > 0:
        l,c = vide[randint(0,len(vide)-1)]
        grille[l][c] = choice([2,4])

    return grille
        
def deplacer_ligne(ligne: list[int]) -> list[int]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    #  On enlève les zéros
    nums = []
    for x in ligne:
        if x != 0:
            nums.append(x)

    # On fusionne les cases identiques
    res = []
    i = 0
    while i < len(nums):
        if i < len(nums) - 1 and nums[i] == nums[i+1]:
            res.append(nums[i] * 2)
            i += 2  # on saute la fusion
        else:
            res.append(nums[i])
            i += 1

    # On rajoute des zéros à droite
    while len(res) < len(ligne):
        res.append(0)

    return res

  
#deplacer(haut,bas,gauche,droite)
def deplacer_gauche(grille)->list[list[int]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    i = 0
    while i < len(grille):
        grille[i] = deplacer_ligne(grille[i])
        i += 1
    return grille


def deplacer_droite(grille:list[list[int]])->list[list[int]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    for i in range(len(grille)):
        ligne = deplacer_ligne(grille[i][::-1])
        grille[i] = ligne[::-1]
    return grille

def transpose(grille:list[list[int]])->list[list[int]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    n = len(grille)
    grille_transposee = []
    for i in range(n):
        nouvelle_ligne = []
        for j in range(n):
            nouvelle_ligne.append(grille[j][i])
        grille_transposee.append(nouvelle_ligne)
    return grille_transposee

def deplacer_haut(grille:list[list[int]])->list[list[int]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    grille_t = transpose(grille)
    grille_t = deplacer_gauche(grille_t)
    return transpose(grille_t)

def deplacer_bas(grille:list[list[int]])->list[list[int]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    grille_t = transpose(grille)
    grille_t = deplacer_droite(grille_t)
    return transpose(grille_t)

def deplacement(carac:str,grille:list[list[int]])->list[list[int]]:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    ancienne = [ligne[:] for ligne in grille]

    if carac in 'Gg':
        grille = deplacer_gauche(grille)
    elif carac in 'Dd':
        grille = deplacer_droite(grille)
    elif carac in 'Hh':
        grille = deplacer_haut(grille)
    elif carac in 'Bb':
        grille = deplacer_bas(grille)
    else:
        print('caractere invalide ressaisissez une direction')
        return grille

    # si rien ne bouge → ne pas ajouter de tuile
    if grille != ancienne:
        return grille
    else:
        return ancienne
    
def jouer()->None:
    grille1 = init_grille(4)
    grille = ajoute_tuile(grille1)
    grille = ajoute_tuile(grille)

    nom = saisie_nom()
    print("\nBienvenue", nom, "!\n")
    afficher_grille(grille)

    while not perdu(grille) and not gagner(grille):
        carac = input('Choisissez une direction g/d/h/b : ')

        nouvelle_grille = deplacement(carac, grille)

        if nouvelle_grille != grille:
            grille = ajoute_tuile(nouvelle_grille)

        afficher_grille(grille)

    if gagner(grille):
        print('🎉 Félicitations ! Vous avez gagné ! 🎉')
    else:
        print('Grille pleine, vous avez perdu !')

if __name__ == '__main__':
    jouer()
    # éxécuté qd ce module n'est pas initialisé par un import.
    