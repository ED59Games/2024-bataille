def creer_pile() -> list:
    """
        Créer une pile
        
        :tests:
        >>> creer_pile()
        []
    """
    return []

def est_vide(p:"pile") -> bool:
    """
        Teste si une pile est vide
    
        :tests:
        >>> p = creer_pile()
        >>> est_vide(p)
        True
    """
    return p == []

def empiler(p:"pile", v:"ELT") -> None:
    """
        Empile la valeur v dans p
    
        :tests:
        >>> p = creer_pile()
        >>> empiler(p, 12)
        >>> est_vide(p)
        False
    """
    p.append(v)
    
def depiler(p:"pile") -> "ELT":
    """
        Dépile et renvoie le sommet de la pile
        
        :tests:
        >>> p = creer_pile()
        >>> empiler(p, 15)
        >>> depiler(p)
        15
        >>> est_vide(p)
        True
    """
    if not est_vide(p):
        res = p.pop()
    return res
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)