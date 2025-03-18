# MELHORIAS DESAFIO: Melhoria do Jogo de Personagens - POO em Python
Este projeto é um jogo de batalha entre um herói e um vilão, desenvolvido em Python. O jogador pode atacar, usar poções e enfrentar inimigos em combates estratégicos.

#Estrutura do Projeto
O código está organizado da seguinte maneira:

rpg_batalha ├── main.py # Arquivo principal que executa o jogo ├── personagem.py # Classe base Personagem e a classe Heroi ├── vilao.py # Classe Vilao derivada de Personagem └── README.md # Documentação do projeto

1. Clone o repositório:
git clone https://github.com/gabriel-oma/Melhorias-no-jogo.git
cd Melhorias-no-jogo

2. Execute o jogo:
python main.py

3. Interaja com o jogo:

Escolha entre atacar (A), usar uma poção de cura (C) ou uma poção de força (F).

O objetivo é derrotar o vilão antes que ele derrote você!
Descrição dos Arquivos
main.py
Gerencia a batalha entre o herói e o vilão.

Permite a interação do jogador via entrada do teclado.

Controla a lógica do jogo e a sequência de turnos.

personagem.py
Contém a classe Personagem, base para heróis e vilões.

Define atributos como vida, ataque e defesa.

Possui métodos para ataque, defesa e diálogo.

Inclui a classe Heroi, que pode usar poções para se fortalecer.

vilao.py
Contém a classe Vilao, que herda de Personagem.

Possui ataques especiais e falas ameaçadoras.

Exemplo de Jogo
=== Batalha: Link vs Ganon === Ganon: "seus esforços são inúteis!" Link: "se prepare, que agora eu vou te atacar!" Escolha: Atacar (A), Usar Poção de Cura (C) ou Usar Poção de Força (F): A Ganon recebeu 12 de dano! Vida restante: 108 Ganon: "agora você vai ver!!" Link recebeu 15 de dano! Vida restante: 85 ...

Melhorias Futuras
Implementar múltiplos vilões e heróis jogáveis.

Adicionar novas habilidades e estratégias de combate.

Criar uma interface gráfica para o jogo.

Licença
Este projeto é de código aberto e pode ser usado livremente para aprendizado e melhorias.

