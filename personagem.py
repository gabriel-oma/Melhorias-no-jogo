import random
from utils import registrar_acao

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida = max(0, self.vida - dano_final)
        registrar_acao(f"{self.nome} recebeu {dano_final} de dano! Vida restante: {self.vida}.")

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        dano = self.ataque * 2 if random.random() < 0.1 else self.ataque
        registrar_acao(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.receber_dano(dano)
