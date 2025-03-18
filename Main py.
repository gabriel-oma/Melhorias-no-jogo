from personagem import Heroi
from vilao import Vilao
import time


def batalha(heroi, vilao):
    print(f'=== Batalha: {heroi.nome} vs {vilao.nome} ===')
    while heroi.esta_vivo() and vilao.esta_vivo():
        heroi.dialogar(vilao)
        vilao.dialogar(heroi)

        escolha = input("Escolha: Atacar (A), Usar Poção de Cura (C) ou Usar Poção de Força (F): ").strip().upper()
        if escolha == "C":
            heroi.usar_pocao_cura()
        elif escolha == "F":
            heroi.usar_pocao_forca()
        else:
            vilao.receber_dano(heroi.ataque)

        if not vilao.esta_vivo():
            print(f'{vilao.nome} foi derrotado! {heroi.nome} vence!')
            break

        time.sleep(1)

        vilao.ataque_especial(heroi)
        if not heroi.esta_vivo():
            print(f'{heroi.nome} foi derrotado! {vilao.nome} vence!')
            break

        time.sleep(1)


heroi = Heroi("Link", 100, 20, 8)
heroi.itens.append("poção de cura")
heroi.itens.append("poção de força")
vilao = Vilao("Ganon", 120, 15, 10, "Alta")

batalha(heroi, vilao)
