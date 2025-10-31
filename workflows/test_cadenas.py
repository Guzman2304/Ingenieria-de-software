def invertir_texto(texto):
    return texto[::-1]

def contar_vocales(texto):
    return sum(1 for c in texto.lower() if c in "aeiou")

def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


def test_invertir_texto():
    assert invertir_texto("hola") == "aloh"

def test_contar_vocales():
    assert contar_vocales("Ingeniería") == 5

def test_es_palindromo_true():
    assert es_palindromo("Anita lava la tina") is True

def test_es_palindromo_false():
    assert es_palindromo("Hola mundo") is False
