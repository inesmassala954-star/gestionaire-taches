# Compléter ici (MASSALA Ines, groupe MI22, PUISSANCE4, date27/11/2025)
#
#
#
#
# Ne pas supprimer cette ligne. <trace>puissance4.py</trace>

####################
# Jeu du Puissance4
####################

def init_grille(nb_ligne:int,nb_col:int)->list[list[str]]:
    """ Renvoie la grille de nb_ligne et nb_col

    Précondition : nb_ligne et nb_col sont strictement positifs
    Exemple(s) :
    $$$ init_grille(2,3)
    [['.','.','.'],['.','.','.']]
    """
    res=[]
    for i in range(nb_ligne):
        res.append(['.']*nb_col)
    return res

def saisie_nom()->str:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nom1=input('joueur1, entrer votre pseudo: ')
    return nom1


# Décommenter et compléter la signature donnée puis faire la suite
def saisie_nom_different(n:str)->str:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nom2=input('joueur2, entrer votre pseudo:')
    while nom2==n:
        print(f'Le nom {n} existe déjà')
        nom2=input('Donner un nom de joueur: ')
    return nom2

def indice_autre_joueur(jcourant:int)->int:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return 1-jcourant

def affichage_grille(grille:list[list[str]])->None:
    """ Affiche la grille

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    chaine=""
    for ligne in grille:
        for case in ligne:
            print(case," ",end='')
        print()

def verification_coup(grille: list[list[str]], col: int) -> bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    if col < 0 or col >= len(grille[0]):
        return False
    return grille[0][col] == '.'
    
    
def jeu_de_pion(grille: list[list[str]], col: int, carac: str) -> int:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    for i in range(len(grille) - 1, -1, -1):
        if grille[i][col] == '.':
            grille[i][col] = carac
            return i
    return -1



def gagner_ligne(grille:list[list[str]],carac:str)->bool:
    """ Renvoie True si 4 caracteres identiques sont alignés sur une meme ligne

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    for i in range(len(grille)):
        for j in range(len(grille[0]) - 3):
            if all(grille[i][j + k] == carac for k in range(4)):
                return True
    return False

    
def gagner_colonne(grille:list[list[str]],carac:str)->bool:
    """ Renvoie True si 4 caracteres identiques sont alignés sur une meme ligne

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    for j in range(len(grille[0])):
        for i in range(len(grille) - 3):
            if all(grille[i + k][j] == carac for k in range(4)):
                return True
    return False


def verification_alignement(grille:list[list[str]],carac:str)->bool:
    """ Renvoie True si 4 caracteres identiques sont alignés sur une meme colone

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    return (
        gagner_ligne(grille, carac)
        or gagner_colonne(grille, carac)
        or gagner_diagonale_desc(grille, carac)
        or gagner_diagonale_mont(grille, carac)
    )

def gagner_diagonale_desc(grille:list[list[str]],carac:str)->bool:
    """ Renvoie True si 4 caracteres identiques sont alignés sur une meme diagonale

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    for i in range(len(grille) - 3):
        for j in range(len(grille[0]) - 3):
            if all(grille[i + k][j + k] == carac for k in range(4)):
                return True
    return False

def gagner_diagonale_mont(grille:list[list[str]],carac:str)->bool:
    """ Renvoie True si 4 caracteres identiques sont alignés sur une meme diagonale

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    for i in range(3, len(grille)):
        for j in range(len(grille[0]) - 3):
            if all(grille[i - k][j + k] == carac for k in range(4)):
                return True
    return False

def verification_grille_plein(grille:list[list[str]])->bool:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    return all(cell != '.' for cell in grille[0])

def demander_colonne(nb_col: int) -> int:
    valide = False
    col = -1

    while not valide:
        s = input("Colonne : ")
        if s.isdigit():
            col = int(s)
            if 0 <= col < nb_col:
                valide = True
            else:
                print("Hors limites")
        else:
            print("Nombre invalide")
    return col

#def est_gagnant(

def jouer():
    nb_lignes, nb_col = 6, 7
    grille = init_grille(nb_lignes, nb_col)

    nom1 = saisie_nom()
    nom2 = saisie_nom_different(nom1)

    noms = [nom1, nom2]
    symboles = ["R", "J"]
    jcourant = 0

    fini = False

    while not fini:
        affichage_grille(grille)
        print(f"Tour de {noms[jcourant]} ({symboles[jcourant]})")

        col = demander_colonne(nb_col)

        if verification_coup(grille, col):
            ligne = jeu_de_pion(grille, col, symboles[jcourant])

            if verification_alignement(grille, symboles[jcourant]):
                affichage_grille(grille)
                print(f"{noms[jcourant]} a gagné !")
                fini = True

            elif verification_grille_plein(grille):
                affichage_grille(grille)
                print("Match nul !")
                fini = True

            else:
                jcourant = indice_autre_joueur(jcourant)
        else:
            print("Colonne pleine !")
            
#Programme principale
if __name__ == '__main__':
    # éxécuté qd ce module n'est pas initialisé par un import.
    jouer()