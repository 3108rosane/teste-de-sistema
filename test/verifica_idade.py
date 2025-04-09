def verifica_idade(idade):
    if idade < 18:
        raise valueError("Acesso negado para menor de 18 anos")
        return "acesso permitido"