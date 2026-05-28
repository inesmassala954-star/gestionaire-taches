# Compléter ici (MASSALA Ines , groupeMI22, JEU TIC TAC TOE, date 19/11/2025)
#
#
#
#
# Ne pas supprimer cette ligne. <trace>tictactoe.py</trace>


####################
# Jeu du Tic Tac Toe
####################

from random import randint

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

def saisie_nom_different(name:str)->str :
    """ Demande la saisie d'un nom 

    Précondition : 
    Exemple(s) :
    $$$ 
    """
    nom=input(" joueur 2 Saisissez votre nom: ")
    while nom==name:
        nom=input("Ce nom existe déja,Saisissez un nom different: ")
    return nom

def init_grille(n:int)->list[list[str]]:
    """ Affiche une grille carree

    Précondition :n est superieur ou egale à 3
    Exemple(s) :
    $$$ init_grille(3)
    [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    """
    res=[]
    for i in range(n):
        res.append([' ']*n)
    return res
        
def afficher_grille(g:list[list[str]])->None:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    
    n = len(g)
    for i in range(n):
        print(g[i][0], '|', g[i][1], '|', g[i][2])
        if i < n-1:
            print('--------')
    
    
def joueur_courant(joueur_courant:int)->int:
    """Renvoie l'indice de l'autre joueur 

    Précondition :
    Exemple(s) :
    $$$ joueur_courant(0)
    1
    $$$ joueur_courant(1)
    0
    """
    return 1-joueur_courant

def indice_case(grille)->int:
    """ à_remplacer_par_ce_que_fait_la_fonction

    Précondition :
    Exemple(s) :
    $$$ 
    """
    n = len(grille)
    i = -1
    j = -1
    while i<0 or j<0 or i>=n or j>=n or grille[i][j]!=' ':
        i = input(f"Ligne (0-{n-1}) : ")
        j = input(f"Colonne (0-{n-1}) : ")
        if i.isdigit() and j.isdigit():
            i = int(i)
            j = int(j)
        else:
            i = j = -1
        if i<0 or j<0 or i>=n or j>=n:
            print("Indices hors limites.")
        elif grille[i][j] != ' ':
            print("Case déjà occupée.")
    return i,j


def colonne(liste:list[list[int]],ind:int)->list[list[int]]:
    """ Renvoie la liste

    Précondition :n est positif et superieur a 0
    Exemple(s) :
    $$$ colonne([[1,2,3],[4,5,6]],1)
    [2, 5]
    """
    g=deepcopy(liste)
    res=[]
    for elt in liste:
        res.append(elt[ind])
    return res
        
def transposee(grille:list[list[int]])->list[list[int]]:
    """ Renvoie la transpose de la grille

    Précondition :
    Exemple(s) :
    $$$ transposee([[1,2,3,4],[4,5,6,7]])
    [[1,4],[2,5],[3,6],[4,7]]
    """
    res=[]
    for i in range(len(grille[0])):
        liste=colonne(grille,i)
        res.append(liste)
    return res
    
                                             

def gagnant(g:list[list[str]],c:str)->bool:
    """ Renvoie True si la grille a des caractères alignés. """
    n = len(g)
    # lignes
    for i in range(n):
        if g[i][0]==c and g[i][1]==c and g[i][2]==c:
            return True
    # colonnes
    for j in range(n):
        if g[0][j]==c and g[1][j]==c and g[2][j]==c:
            return True
    # diagonales
    if g[0][0]==c and g[1][1]==c and g[2][2]==c:
        return True
    if g[0][2]==c and g[1][1]==c and g[2][0]==c:
        return True
    return False
    
def grille_pleine(grille:list[list[str]])->bool:
    """ Vérifie si la grille est entièrement remplie. """
    for ligne in grille:
        if ' ' in ligne:
            return False
    return True


def jouer() -> None:
    """Fonction principale.
    """
    # initiation de la grille : elle est vide
    grille=init_grille(3)
    # autres initialisations
    nom1=saisie_nom()
    nom2=saisie_nom_different(nom1)
    joueurs=[nom1,nom2]
    caracteres=['X','O']
    ### boucle de jeu
    
    ind_joueur_courant=randint(0,1)
    partie_gagnee=False
    while not partie_gagnee and not grille_pleine(grille):
        # affichage de la grille
        carac_courant = caracteres[ind_joueur_courant]
        nom_courant = joueurs[ind_joueur_courant]
        
        afficher_grille(grille)
        
        # affichage du joueur courant (qui s'apprête à jouer)
        
        print(f"{nom_courant} ({carac_courant}): à vous !")

        # saisie des indices de la case choisie par le joueur
        ligne,colonne=indice_case(grille)
        grille[ligne][colonne]=carac_courant
        
        # changement de l'état du jeu en conséquence (grille etc)
        if gagnant(grille, carac_courant):
            partie_gagnee = True
        # changement de joueur courant
        elif not partie_gagnee and not grille_pleine(grille):
            ind_joueur_courant = joueur_courant(ind_joueur_courant)
    # affichage de la grille finale
    afficher_grille(grille)
    if partie_gagnee:
        print(f"\n Félicitations ! {nom_courant} a gagné la partie !") 
    else:
        print("\n La grille est pleine. Match Nul !")
    # affichage du résultat du jeu : soit les 2 joueurs ont perdu, soit
    # l'un d'entre eux (à afficher) a gagné


if __name__ == '__main__':
    jouer()
    # éxécuté qd ce module n'est pas initialisé par un import.
    