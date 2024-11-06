
# Prova do Caminho

Este é um jogo de tabuleiro interativo desenvolvido em Python, utilizando a biblioteca Pygame. O objetivo do jogo é responder corretamente às perguntas de múltipla escolha para avançar no tabuleiro. Dois jogadores competem para ver quem alcança o final primeiro, alternando turnos e enfrentando perguntas ao longo do percurso.

## Características do Jogo
* Desenho do Tabuleiro: O tabuleiro possui duas linhas e sete colunas de células.
* Parede com Bolas: Cada bola representa uma pergunta disponível. As bolas já respondidas ficam em cinza.
* Modal de Pergunta: Exibe a pergunta, opções de resposta e permite revelar a resposta correta.
*  Jogadores: Dois jogadores, identificados pelas cores azul e vermelho, que alternam turnos.
* Imagem de Plano de Fundo: Um plano de fundo é exibido na área da pergunta.

## Requisitos
* Python 3.6 ou superior
* Pygame 1.9.6 ou superior

## Como Jogar
1. Instale as Dependências:

```bash
    pip install pygame 
```

2. Configure suas Perguntas:

```bash
    Pergunta 1: Qual é a capital da França?
    Opções: A) Roma / B) Londres / C) Paris / D) Berlim
    Resposta 1: C

    Pergunta 2: Qual é o maior planeta do Sistema Solar?
    Opções: A) Terra / B) Marte / C) Júpiter / D) Saturno
    Resposta 2: C
```

3. Execute o Jogo:

```bash
    python seu_jogo.py
```

## Estrutura do Código

* Carregar_perguntas_respostas(arquivo): Carrega as perguntas, opções e respostas do arquivo de texto.
* desenhar_texto_quebrado(texto, x, y, largura_maxima): Desenha o texto com quebra de linha para a modal de perguntas.
* desenhar_tabuleiro(): Desenha o tabuleiro do jogo na tela.
* desenhar_parede(): Desenha a parede com as bolas representando as perguntas.
* mostrar_area_lateral(): Exibe a modal de pergunta com a pergunta, opções de resposta e botões de ação.
* movimentar_jogador(acertou): Move o jogador conforme a resposta (acerto ou erro).

## Exemplo de Código

### Abaixo está um trecho básico do código:

```bash
import pygame
import sys
import textwrap

# Inicializar o Pygame
pygame.init()

# Definir as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
CINZA = (128, 128, 128)
ROXO = (147, 112, 219)

# Tamanho da tela e das células
largura_tela = 1000
altura_tela = 500
tamanho_celula = 50
tamanho_bola = 20
espaco_bola = 15

# Imagem de fundo
fundo_imagem = pygame.image.load("fundo_imagem.png")

# Configurar a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Tabuleiro com Perguntas")

# Configurar fonte
fonte = pygame.font.Font(None, 24)

# Variáveis de estado do jogo
jogo_terminado = False
mensagem_vitoria = "Parabéns! Você mandou bem, continue jogando para melhorar seus conhecimentos em estatística."
perguntas_usadas = set()

# Carregar perguntas e respostas do arquivo
def carregar_perguntas_respostas(arquivo):
    perguntas, opcoes, respostas = [], [], []
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            if linha.startswith("Pergunta"):
                perguntas.append(linha.split(": ", 1)[1].strip())
            elif linha.startswith("Opções"):
                opcoes.append(linha.split(": ", 1)[1].strip().split(" / "))
            elif linha.startswith("Resposta"):
                respostas.append(linha.split(": ", 1)[1].strip())
    if len(perguntas) != len(opcoes) or len(perguntas) != len(respostas):
        raise ValueError("O número de perguntas, opções e respostas deve ser o mesmo.")
    return perguntas, opcoes, respostas

perguntas, opcoes, respostas = carregar_perguntas_respostas('perguntas.txt')
pergunta_selecionada = None
resposta_revelada = False

# Jogadores
jogadores = {
    "azul": {"cor": AZUL, "pos_x": 0, "pos_y": 200, "casa": 0},
    "vermelho": {"cor": VERMELHO, "pos_x": 0, "pos_y": 250, "casa": 0},
}
```
## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`API_KEY`

`ANOTHER_API_KEY`


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherineoelsner.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)


## Autores

- [@BarrosWesley](https://github.com/BarrosWesley)


## Instalação

Instale my-project com npm

```bash
  npm install my-project
  cd my-project
```
    
## Licença

[MIT](https://choosealicense.com/licenses/mit/)


## Melhorias

- Ajustar o tabeuleiro para trazer como perguntas imagens, inserir imagem de plano de fundo mudar os jogadores, mudar o tabuleiro para 3d, incluir música e etc...
- Adapte o Feedback de Respostas no Jogo: Considere adicionar uma explicação adicional ou um pequeno feedback ao usuário para cada resposta, especialmente para as perguntas mais complexas


## Roadmap

- Criar a versão mobile

- Adicionar mais integrações


## Stack utilizada

**Front-end:** Python, pygame, sys, textwrap




## Usado por

Esse projeto é usado pelas seguintes empresas:

- WB Consultoria e serviços de TI
- Professores SENAC
- Alunos SENAC

