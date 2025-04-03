from funcao import *


def test_email_valido():
    assert email_valido("rosanemaia3108@gmail.com") is True
    assert email_valido("rosane.com") is False


def test_dividir():
    assert dividir(2,2)== 1
    assert dividir(2,0) ==None

