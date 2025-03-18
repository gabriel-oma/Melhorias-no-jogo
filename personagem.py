import random

class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.habilidades = []

    def receber_dano(self, dano):
        dano_final = max(0, dano - self.defesa)
        self.vida = max(0, self.vida - dano_final)
        print(f'{self.nome} recebeu {dano_final} de dano! Vida restante: {self.vida}')

    def esta_vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        if random.random() < 0.1:
            dano = self.ataque * 2
            print(f'{self.nome} realizou um ATAQUE CRÍTICO! Dano dobrado!')
        else:
            dano = self.ataque
        alvo.receber_dano(dano)
    def dialogar(self, outro):
        mensagens = [
            f'{self.nome}: "você acha que pode me vencer, {outro.nome}? "',
            f'{self.nome}: "se prepare, que agora eu vou te atacar!"',
            f'{self.nome}: "é só isso que você tem, {outro.nome}?"',
            f'{self.nome}: "eu não vou perder tão fácil!"'
        ]
        print(random.choice(mensagens))

    def __str__(self):
        return f'{self.nome} - Vida: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}'

class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.itens = []

    def usar_pocao_cura(self):
        if "poção de cura" in self.itens:
            self.vida += 25
            self.itens.remove("poção de cura")
            print(f'{self.nome} usou uma Poção de Cura! Vida restaurada para {self.vida}.')
        else:
            print(f'{self.nome} você não tem mais poção de cura!')

    def usar_pocao_forca(self):
        if "poção de força" in self.itens:
            self.ataque += 10
            self.itens.remove("poção de força")
            print(f'{self.nome} usou uma Poção de Força! Ataque aumentado para {self.ataque}.')
        else:
            print(f'{self.nome} você não tem mais poção de força!')
