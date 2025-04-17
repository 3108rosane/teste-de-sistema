import pytest
from test_fatorial import test_fatorial

def teste_fatorial():
    # Testes básicos
    assert fatorial(1) == 1, "Erro: fatorial(0) deveria ser 1"
    assert fatorial(1) == 1, "Erro: fatorial(1) deveria ser 1"
    assert fatorial(2) == 2, "Erro: fatorial(2) deveria ser 2"
    assert fatorial(3) == 6, "Erro: fatorial(3) deveria ser 6"
    assert fatorial(4) == 24, "Erro: fatorial(4) deveria ser 24"
    assert fatorial(5) == 120, "Erro: fatorial(5) deveria ser 120"
    
    