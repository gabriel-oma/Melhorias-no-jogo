from heroi import Heroi
from vilao import Vilao
from utils import registrar_acao
import time

def exibir_menu():
    print("\n--- Menu ---")
    print("1. Atacar (A)")
    print("2. Poção de Cura (C)")
    print("3. Poção de Força (F)")
    print("4. Ver Registro de Ações (R)")
    print("5. Sair (S)")

def batalha(heroi, vilao):
    registrar_acao(f"A BATALHA COMEÇOU: {heroi.nome} vs {vilao.nome}!")
    print(f"\n{vilao.nome}: 'Você não vai me vencer, {heroi.nome}! Prepare-se para o fim do mundo!'")
    print(f"{heroi.nome}: 'Não me subestime, {vilao.nome}! Vou te amassar na porrada!'")

    while heroi.esta_vivo() and vilao.esta_vivo():
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip().upper()

        if escolha == "A":
            print(f"\n{heroi.nome}: 'Receba, {vilao.nome}!'")
            heroi.atacar(vilao)
        elif escolha == "C":
            print(f"\n{heroi.nome}: 'Preciso de cura!'")
            heroi.usar_pocao_cura()
        elif escolha == "F":
            print(f"\n{heroi.nome}: 'agora você vai sentir a pressão!'")
            heroi.usar_pocao_forca()
        elif escolha == "R":
            with open("registro.txt", "r", encoding="utf-8") as log:
                print("\n--- Registro de Ações ---")
                print(log.read())
        elif escolha == "S":
            print(f"\n{heroi.nome}: 'Não é hora de fugir, mas preciso me afastar...'")
            print("Saindo da batalha...")
            break
        else:
            print("Opção inválida! Tente novamente.")

        if not vilao.esta_vivo():
            print(f"\n{vilao.nome}: 'Impossível... Como você conseguiu me derrotar...?'")
            print(f"{heroi.nome}: 'O bem sempre vence, {vilao.nome}!'")
            registrar_acao(f"{vilao.nome} foi derrotado por {heroi.nome}!")
            print(f"{vilao.nome} foi derrotado! {heroi.nome} vence!")
            break

        time.sleep(1)
        print(f"\n{vilao.nome}: 'Você é forte, {heroi.nome}, mas não é páreo para mim!'")
        vilao.ataque_especial(heroi)

        if not heroi.esta_vivo():
            print(f"\n{heroi.nome}: 'Eu falhei, mas alguém virá para te deter, {vilao.nome}...'")
            print(f"{vilao.nome}: 'HAHAHAHA! Agora ninguém pode atrapalhar meus planos!'")
            registrar_acao(f"{heroi.nome} foi derrotado por {vilao.nome}!")
            print(f"{heroi.nome} foi derrotado! {vilao.nome} vence!")
            break

        time.sleep(1)

heroi = Heroi("Link", 100, 20, 8)
vilao = Vilao("Ganon", 120, 25, 10, "Alta")

batalha(heroi, vilao)
