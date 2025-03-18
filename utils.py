def registrar_acao(mensagem):
    with open("registro.txt", "a", encoding="utf-8") as log:
        log.write(mensagem + "\n")
    print(f"[LOG] {mensagem}")
