nome = input("Qual seu nome? ")
experiencia = int(input("Quantos anos de experiência você tem? "))
nota = float(input("Qual sua nota média? "))
disponivel = input("Você está disponível? (sim/nao) ")

if disponivel == "sim":
    if experiencia < 3:
        print(f"{nome} está disponível e tem pouca experiência!")
    elif nota < 6:
        print(f"{nome} está disponível, mas tem nota baixa.")
    else:
        print(f"{nome} está disponível para trabalhar!")
else:
    print(f"{nome} não está disponível no momento.")