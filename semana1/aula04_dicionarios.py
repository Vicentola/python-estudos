atendente = {
    "nome": "Cleberson",
    "experiencia": 5,
    "nota": 8.3,
    "disponivel": True
}

print(atendente["nome"])
print(atendente["experiencia"])
print(atendente)


atendentes = [
    {"nome": "Cleberson", "experiencia": 5, "nota": 8.3, "disponivel": True},
    {"nome": "Maria", "experiencia": 2, "nota": 9.1, "disponivel": False},
    {"nome": "João", "experiencia": 7, "nota": 7.5, "disponivel": True}
]

for atendente in atendentes:
    if atendente ["disponivel"] == True:
    
        if atendente ["nota"] >= 8:
            print(f"{atendente['nome']} - {atendente['experiencia']} anos - nota {atendente['nota']}")
        else:
            print("NOta necessaria nao atendida")
        

        
    else:
        print("Atendente nao disponível")
    
    
