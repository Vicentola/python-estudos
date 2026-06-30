contador = 1

while contador <= 5:
    print(f"Atendendo número {contador}")
    contador += 1
    
print("Fim da lista")

atendentes = ["vicente","Pedro","Helena","rubens"]

for atendente in atendentes:
        print(f"atende disponível: {atendente}")
        

notas = [8.5, 5.2, 9.0, 4.8, 7.1]

for nota in notas:
    if nota >= 6:
        print(f"Nota {nota} - aprovado")
    else:
        print(f"Nota {nota} - reprovado")
        
experiencias = [1,2,3,4,5]

for experiencia in experiencias:
    if experiencia >= 3:
        print(f"experiencia {experiencia} - experiente")
    else:
        print(f"experiencia {experiencia} - inexperiente")