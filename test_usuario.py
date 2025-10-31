usuarios = {}

def registrar_usuario(username, password):
    if username in usuarios:
        raise ValueError("Usuario ya existe")
    usuarios[username] = password
    return True

def autenticar_usuario(username, password):
    if username not in usuarios:
        return False
    return usuarios[username] == password


def test_registro_exitoso():
    assert registrar_usuario("antonio", "1234") is True

def test_registro_duplicado():
    try:
        registrar_usuario("antonio", "9999")
    except ValueError as e:
        assert str(e) == "Usuario ya existe"

def test_autenticacion_exitosa():
    assert autenticar_usuario("antonio", "1234") is True

def test_autenticacion_fallida():
    assert autenticar_usuario("antonio", "0000") is False

def test_usuario_inexistente():
    assert autenticar_usuario("pepe", "1111") is False
