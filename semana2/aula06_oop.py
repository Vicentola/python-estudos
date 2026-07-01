class Atendente:
    def __init__(self, nome, experiencia, nota):
        self.nome = nome
        self.experiencia = experiencia
        self.nota = nota
        self.disponivel = True
        
    def apresentar(self):
        print(f"Nome: {self.nome} | Experiência: {self.experiencia} anos | Nota: {self.nota}") 
    
    def mudar_disponibilidade(self, status):
        self.disponivel = status
        print(f"{self.nome} agora está disponível: {self.disponivel}")    
        
    def avaliar(self, nova_nota):
        self.nota = nova_nota
        print(f"Sua nova nota é {nova_nota}")
        
        
class Empresa:
    def __init__(self, nome, segmento):
        self.nome = nome 
        self.segmento = segmento
        self.atendentes = []
        
    def contratar(self, atendente):
        self.atendentes.append(atendente)

        if self.atendentes is not None:
            print(f"{atendente.nome} foi contratado(a) pela empresa {self.nome}")
    
    def listar_atendentes(self):
        for atendente in self.atendentes:
            atendente.apresentar()
        print(f"atendentes contratados: {len(self.atendentes)} - {self.segmento}")
        


atendente1 = Atendente("Cleberson", 5, 8.3)
atendente1.apresentar()
atendente1.mudar_disponibilidade(False)
atendente1.apresentar()
atendente1.apresentar()
atendente1.avaliar(6.0)
atendente1.apresentar()

empresa1 = Empresa("DoValle Eventos", "gastronomia")
empresa1.contratar(atendente1)
empresa1.listar_atendentes()