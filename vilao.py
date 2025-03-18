from personagem import Personagem
from utils import registrar_acao
import random

class Vilao(Personagem):
    def __init__(self, nome, vida, ataque, defesa, maldade):
        super().__init__(nome, vida, ataque, defesa)
        self.maldade = maldade

    def ataque_especial(self, alvo):
        dano = self.ataque * 1.5 if random.random() > 0.5 else self.ataque
        registrar_acao(f"{self.nome} usou um ataque especial contra {alvo.nome}, causando {dano} de dano!")
        print(f"{self.nome}: 'Sinta meu poder!'")
        alvo.receber_dano(dano)
