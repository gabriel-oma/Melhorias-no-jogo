
# Projeto: Batalha entre Herói e Vilão com Sistema de Log

Este projeto é um jogo de batalha em turnos entre um herói e um vilão, desenvolvido em Python. O herói pode atacar, usar poções de cura e poções de força, enquanto o vilão possui um ataque especial que causa dano adicional. O jogo é interativo, com diálogos entre os personagens, um menu para o jogador escolher suas ações e um sistema de log que registra todas as ações durante a batalha em um arquivo `registro.txt`.

---

## Funcionalidades

- **Batalha em turnos**: O herói e o vilão se enfrentam em turnos alternados.
- **Ações do Herói**:
  - **Atacar**: Causa dano ao vilão.
  - **Poção de Cura**: Restaura a vida do herói.
  - **Poção de Força**: Aumenta o ataque do herói.
- **Ataque Especial do Vilão**: O vilão tem uma chance de causar dano adicional ao herói.
- **Diálogos**: Interações entre o herói e o vilão durante a batalha.
- **Menu Interativo**: O jogador escolhe as ações do herói através de um menu.
- **Sistema de Log**: Todas as ações e diálogos são registrados em um arquivo `registro.txt`, que é criado automaticamente durante a execução do jogo.

---

## Como Executar


2. **Clonar o repositório** (se aplicável):
   ```bash
   git clone https://github.com/gabriel-oma/Projeto-3v.a.git
   cd Projeto-3v.a
   ```

3. **Executar o jogo**:
   - Navegue até o diretório onde os arquivos do jogo estão localizados.
   - Execute o arquivo `main.py`:
     ```bash
     python main.py
     ```

4. **Jogar**:
   - Siga as instruções no console para escolher as ações do herói.
   - A batalha continua até que o herói ou o vilão seja derrotado.
   - Todas as ações e diálogos serão registrados no arquivo `registro.txt`, que será criado automaticamente na mesma pasta onde o jogo está sendo executado.

---

## Estrutura do Projeto

- **`main.py`**: Contém a lógica principal do jogo, incluindo o menu e a batalha.
- **`heroi.py`**: Define a classe `Heroi`, com métodos para atacar e usar poções.
- **`vilao.py`**: Define a classe `Vilao`, com um ataque especial.
- **`personagem.py`**: Define a classe base `Personagem`, com atributos como vida, ataque e defesa.
- **`utils.py`**: Contém a função `registrar_acao`, que registra as ações e diálogos no arquivo `registro.txt`.
- **`README.md`**: Este arquivo, com informações sobre o projeto.

---

## Sistema de Log

O sistema de log é implementado no arquivo `utils.py`. Ele registra todas as ações e diálogos durante a batalha em um arquivo chamado `registro.txt`. O arquivo é criado automaticamente na primeira execução do jogo e é atualizado a cada ação.

### Exemplo de Conteúdo do `registro.txt`:
```
Batalha começou: Link vs Ganon!
Link atacou Ganon causando 20 de dano!
Ganon recebeu 10 de dano! Vida restante: 110.
Ganon usou um ataque especial contra Link, causando 37 de dano!
Link recebeu 29 de dano! Vida restante: 71.
Link usou uma Poção de Cura! Vida agora: 96.
Ganon foi derrotado por Link!
```

---

### Menu de Ações
```
--- Menu ---
1. Atacar (A)
2. Poção de Cura (C)
3. Poção de Força (F)
4. Ver Registro de Ações (R)
5. Sair (S)
Escolha uma opção: A
```


## Personalização

- **Herói e Vilão**:
  - Você pode alterar os atributos do herói e do vilão no arquivo `main.py`:
    ```python
    heroi = Heroi("Link", 100, 20, 8)
    vilao = Vilao("Ganon", 120, 25, 10, "Alta")
    ```

- **Log**:
  - O arquivo `registro.txt` é gerado automaticamente. Se quiser limpar o log, basta excluir o arquivo `registro.txt` antes de executar o jogo novamente.

---

