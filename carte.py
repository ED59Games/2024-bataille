from structures import *

VALEURS  = ['7', '8', '9', '10', 'V', 'D', 'R', 'As']
SYMBOLES = ['♦', '♥', '♠', '♣']

def creer_carte(v:int, s:int) -> tuple:
    """
        v : valeur  (0, ..., 7)
        s : symbole (0, ..., 3)
        
        :tests:
        >>> creer_carte(0, 0)
        Carte(valeur='7', symbole='♦')
        >>> creer_carte(7, 3)
        Carte(valeur='As', symbole='♣')
    """
    
    return CARTE(VALEURS[v], SYMBOLES[s])

def comparer_carte(c1:"CARTE", c2:"CARTE") -> int:
    """
        Renvoie :
            * 1  si c1 < c2
            * -1 si c1 > c2
            * 0  si c1 = c2
            
        :tests:
        >>> comparer_carte(creer_carte(0, 0), creer_carte(1, 0))
        1
        >>> comparer_carte(creer_carte(3, 1), creer_carte(2, 2))
        -1
        >>> comparer_carte(creer_carte(5, 2), creer_carte(5, 1))
        0
    """
    ind1 = VALEURS.index(c1.valeur)
    ind2 = VALEURS.index(c2.valeur)
    
    if ind1 < ind2 :
        res = 1
    elif ind1 > ind2 :
        res = -1
    else :
        res = 0
    return res

def afficher_carte(c:"CARTE") -> str:
    """
        Affichage d'une carte
    """
    return f"{c.valeur} de {c.symbole}"

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)