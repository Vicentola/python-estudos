def saudar(nome):
    print(f"Olá, {nome}!")
    
saudar("Vicente")
saudar("Cleberson")

def avaliar_atendente(nome, nota = 0):
    
    if nota >= 8:
        print(f"{nome} tem ótima avaliacao!")
    elif nota >= 6:
        print(f"{nome} tem avaliacao reular!")
    else:
        print(f"{nome} tem avaliacao baixa!")
        
avaliar_atendente("Cleberson", 8.3)
avaliar_atendente("maria", 5.5)
avaliar_atendente("Joao", 7.0)
avaliar_atendente("Ana")

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

resultado = calcular_media(8.0, 7.5, 9.0)
print(f"Média final: {resultado}")

def atendente_aprovado(nota, experiencia):
    return nota >= 6 and experiencia >= 2


print(atendente_aprovado(7.0, 3.0))
print(atendente_aprovado(5.0, 1.0))
