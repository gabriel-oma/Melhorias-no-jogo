from heroi import Heroi
from vilao import Vilao
from utils import registrar_acao
import time

def batalha(heroi, vilao):
    registrar_acao(f"Batalha começou: {heroi.nome} vs {vilao.nome}!")
    while heroi.esta_vivo() and vilao.esta_vivo():
        escolha = input("Escolha: Atacar (A), Poção de Cura (C), Poção de Força (F): ").strip().upper()
        if escolha == "C":
            heroi.usar_pocao_cura()
        elif escolha == "F":
            heroi.usar_pocao_forca()
        else:
            heroi.atacar(vilao)

        if not vilao.esta_vivo():
            registrar_acao(f"{vilao.nome} foi derrotado por {heroi.nome}!")
            print(f"{vilao.nome} foi derrotado! {heroi.nome} vence!")
            break

        time.sleep(1)
        vilao.ataque_especial(heroi)

        if not heroi.esta_vivo():
            registrar_acao(f"{heroi.nome} foi derrotado por {vilao.nome}!")
            print(f"{heroi.nome} foi derrotado! {vilao.nome} vence!")
            break

        time.sleep(1)

heroi = Heroi("Link", 100, 20, 8)
vilao = Vilao("Ganon", 120, 25, 10, "Alta")

batalha(heroi, vilao)
