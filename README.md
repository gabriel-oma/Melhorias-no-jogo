# **MELHORIAS- PROJETO 3.VA**

Este projeto é um jogo de batalha entre um herói e um vilão, desenvolvido em **Python**. O jogador pode atacar, usar poções e enfrentar inimigos em combates estratégicos.

---

## **Estrutura do Projeto**

O código está organizado da seguinte maneira:

- **main.py** → Arquivo principal que executa o jogo.
- **personagem.py** → Contém a classe base `Personagem` e a classe `Heroi`.
- **vilao.py** → Contém a classe `Vilao`, derivada de `Personagem`.
- **README.md** → Documentação do projeto.

---

## **Como Jogar**

1. Clone o repositório:
   ```sh
   git clone https://github.com/gabriel-oma/Melhorias-no-jogo.git
   cd Melhorias-no-jogo
   ```

2. Execute o jogo:
   ```sh
   python main.py
   ```

3. Interaja com o jogo:
   - Escolha entre **Atacar (A)**, **Usar Poção de Cura (C)** ou **Usar Poção de Força (F)**.
   - O objetivo é **derrotar o vilão antes que ele derrote você!**

---

## **Descrição dos Arquivos**

### **main.py**
- Gerencia a batalha entre o herói e o vilão.
- Permite a interação do jogador via entrada do teclado.
- Controla a lógica do jogo e a sequência de turnos.

### **personagem.py**
- Contém a classe `Personagem`, base para heróis e vilões.
- Define atributos como vida, ataque e defesa.
- Possui métodos para ataque, defesa e diálogo.
- Inclui a classe `Heroi`, que pode usar poções para se fortalecer.

### **vilao.py**
- Contém a classe `Vilao`, que herda de `Personagem`.
- Possui ataques especiais e falas ameaçadoras.

---

## **Exemplo de Jogo**

```
=== Batalha: Link vs Ganon ===
Ganon: "Seus esforços são inúteis!"
Link: "Se prepare, que agora eu vou te atacar!"
Escolha: Atacar (A), Usar Poção de Cura (C) ou Usar Poção de Força (F): A
Ganon recebeu 12 de dano! Vida restante: 108
Ganon: "Agora você vai ver!!"
Link recebeu 15 de dano! Vida restante: 85
...
```

---






