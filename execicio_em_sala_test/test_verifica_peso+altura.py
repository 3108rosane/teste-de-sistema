from imc import calcular_imc

def test_peso_normal():
    assert calcular_imc(70, 1.75) == "IMC: 22.86 - Peso normal"

def test_muito_abaixo_peso():
    assert calcular_imc(50, 1.75) == "IMC: 16.33 - Muito abaixo do peso"

def test_sobrepeso():
    assert calcular_imc(85, 1.75) == "IMC: 27.76 - Sobrepeso"

def test_obesidade_grau_2():
    assert calcular_imc(110, 1.75) == "IMC: 35.92 - Obesidade grau 2 (severa)"

def test_altura_invalida():
    assert calcular_imc(70, 0) == "Altura inválida"
