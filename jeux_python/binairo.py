# Compléter ici (MASSALA Ines , groupe MI22, contenu fichier Binairo, 02/12/2025)
#
#
#
#
# Ne pas supprimer cette ligne. <trace>binairo.py</trace>


####################
# Jeu du Binairo
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
    $$$ init_grille(4)
    [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
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
        print(g[i][0], '|', g[i][1], '|', g[i][2],'|',g[i][3])
        if i < n-1:
            print('-------------')
  
from copy import deepcopy
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

def ligne_valide(grille:list[list[str]],n:int)->bool:
    """ Renvoie True si la ligne est valide

    Précondition :
    Exemple(s) :
    $$$ ligne_valide([['1','1','0','0'],['1','0','1','0'],['0','0','1','1'],['0','1','1','0']],0)
    True
    $$$ ligne_valide([['1','1','0','0'],['1','0','0','0'],['0','0','1','1'],['0','1','1','0']],1)
    False
    """
    nb_un=len(grille)/2
    nb_zero=len(grille)/2
    cpt1=0
    cpt0=0
    for i in range(len(grille)):
        if '1'==grille[n][i]:
            cpt1+=1
        elif '0'==grille[n][i]:
            cpt0+=1
        else:
            cpt1=cpt1
            cpt0=cpt0
    return cpt0==nb_zero and cpt1==nb_un

def colonne_valide(grille:list[list[str]],n:int)->bool:
    """ Renvoie True si la ligne est valide

    Précondition :
    Exemple(s) :
    $$$ colonne_valide([['1','1','0','0'],['1','0','1','0'],['0','0','1','1'],['0','1','1','0']],0)
    True
    $$$ colonne_valide([['1','1','0','0'],['1','0','0','0'],['0','0','1','1'],['0','0','1','0']],1)
    False
    """
    res=colonne(grille,n)
    nb_un=len(res)/2
    nb_zero=len(res)/2
    cpt1=0
    cpt0=0
    for i in range(len(res)):
        if '1'==res[i]:
            cpt1+=1
        elif '0'==res[i]:
            cpt0+=1
        else:
            cpt1=cpt1
            cpt0=cpt0
    return cpt0==nb_zero and cpt1==nb_un

def toutes_colonnes_valides(grille:list[list[str]])->bool:
    """ Renvoie True si la ligne est valide

    Précondition :
    Exemple(s) :
    $$$ toutes_colonnes_valides([['1','1','0','0'],['1','0','1','0'],['0','0','1','1'],['0','1','1','0']])
    False
    $$$ toutes_colonnes_valides([['1','0','0','1'],['0','1','1','0'],['1','0','1','0'],['0','1','0','1']])
    True
    """
    return (colonne_valide(grille,0) and colonne_valide(grille,1) and colonne_valide(grille,2) and colonne_valide(grille,3))
toutes_colonnes_valides([['1','1','0','0'],['1','0','1','0'],['0','0','1','1'],['0','1','1','0']])    
def toutes_lignes_valide(grille:list[list[str]])->bool:
    """ Renvoie True si la ligne est valide

    Précondition :
    Exemple(s) :
    $$$ toutes_lignes_valide([['1','1','0','0'],['1','0','1','0'],['0','0','1','1'],['0','1','1','0']])
    True
    $$$ toutes_lignes_valide([['1','1','0','0'],['1','0','0','0'],['0','0','1','1'],['0','1','1','0']])
    False
    """
    return (ligne_valide(grille,0) and ligne_valide(grille,1) and ligne_valide(grille,2) and ligne_valide(grille,3))

# def ligne_unique(grille:list[list[str]])->bool:
#     """ Renvoie True si les lignes sont uniques
# 
#     Précondition :
#     Exemple(s) :
#     $$$ ligne_unique([['1','1','0','0'],['1','0','1','0'],['0','0','1','1'],['0','1','1','0']])
#     True
#     $$$ ligne_unique([['1','1','0','0'],['1','0','1','0'],['0','0','1','1'],['1','0','1','0']])
#     False
#     """
#     for i in range(len(grille)):
#         for j in rannge(len(grille)):
#             if grille[i][j]
     

def grille_valide(grille:list[list[str]])->bool:
    """ Renvoie True si la ligne est valide

    Précondition :
    Exemple(s) :
    $$$ grille_valide([['1','1','0','0'],['1','0','1','0'],['0','0','1','1'],['0','1','1','0']])
    False
    $$$ grille_valide([['1','0','0','1'],['0','1','1','0'],['1','0','1','0'],['0','1','0','1']])
    True
    """
    return (toutes_colonnes_valides(grille) and toutes_lignes_valide(grille))