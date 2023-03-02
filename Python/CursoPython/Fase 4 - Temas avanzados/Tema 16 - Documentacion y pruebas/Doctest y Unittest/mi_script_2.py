def palindromo(palabra):
	"""
	La funcion palindromo(palabra) recibe una palabra.
	Si la palabra es in palindromo devuelve True, si no False

	Un palindromo es una palabra o frase que se lee igual
	tanto de izquierda a derecha como de derecha a izquierda

	>>> palindromo("somos")
	True

	>>> palindromo("radar")
	True

	>>> palindromo("Ana")
	True
		
	>>> palindromo("Atar a la rata")
	True


	"""

	if palabra.lower().replace(" ","") == palabra[::-1].lower().replace(" ",""):
		return True
	else:
		return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
