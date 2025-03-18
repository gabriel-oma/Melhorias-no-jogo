from personagem import Personagem
import random


class Vilao(Personagem):
    def __init__(self, nome, vida, ataque, defesa, maldade):
        super().__init__(nome, vida, ataque, defesa)
        self.maldade = maldade

    def ataque_especial(self, alvo):
        if random.random() > 0.5:
            dano = self.ataque * 1.5
            print(f'{self.nome}: "hahaha sinta o meu poder!"')
        else:
            dano = self.ataque
            print(f'{self.nome}: "agora você vai ver!!"')
        alvo.receber_dano(dano)

    def dialogar(self, outro):
        mensagens = [
            f'{self.nome}: "hahaha! você é fraco, {outro.nome}!"',
            f'{self.nome}: "vou te esmagar!"',
            f'{self.nome}: "seus esforços são inúteis!"',
            f'{self.nome}: "sinta o terror!"'
        ]
        print(random.choice(mensagens))
