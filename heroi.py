from personagem import Personagem
from utils import registrar_acao

class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.itens = ["poção de cura", "poção de força"]

    def usar_pocao_cura(self):
        if "poção de cura" in self.itens:
            self.vida += 25
            self.itens.remove("poção de cura")
            registrar_acao(f"{self.nome} usou uma Poção de Cura! Vida agora: {self.vida}.")
        else:
            print(f"{self.nome}: 'Não tenho mais poções de cura, preciso tomar cuidado!'")

    def usar_pocao_forca(self):
        if "poção de força" in self.itens:
            self.ataque += 10
            self.itens.remove("poção de força")
            registrar_acao(f"{self.nome} usou uma Poção de Força! Ataque agora: {self.ataque}.")
        else:
            print(f"{self.nome}: 'Já usei todas as minhas poções de força, melhor continuar lutando!'")
