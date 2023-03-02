def suma(a,b):
    """
    La funcion suma recibe 2 parametros 
    y devuelve la suma de estos
       
    >>> suma(5,10)
    15

    >>> suma(0,0)
    0

    >>> suma(-5,7)
    2

    >>> suma("aa", "bb")
    'aabb'
    
    """
    
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()