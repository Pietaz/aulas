idade= int(input("digite sua idade: "))
def maior_idade(idade):
    if idade>=18:
        return "maior de idade"
    else:
        return "menor de idade"
    return idade
print(maior_idade(idade))