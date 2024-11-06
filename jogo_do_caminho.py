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

# imagens
fundo_imagem = pygame.image.load("fundo_imagem.png")

# Configurar a tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo do Caminho")

# Configurar fonte
fonte = pygame.font.Font(None, 24)



# Variáveis de estado do jogo
jogo_terminado = False
mensagem_vitoria = "Parabéns! Você mandou bem, continue jogando para melhorar seus conhecimentos em estatística."
perguntas_usadas = set()  # Conjunto para rastrear perguntas já utilizadas

# Carregar perguntas e respostas do arquivo
def carregar_perguntas_respostas(arquivo):
    perguntas, opcoes, respostas = [], [], []
    with open(arquivo, 'r', encoding='utf-8') as f:
        for linha in f:
            if linha.startswith("Pergunta"):
                perguntas.append(linha.split(": ", 1)[1].strip())
            elif linha.startswith("Opções"):
                # Aqui usamos split para separar as opções pela barra
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
    "vermelho": {"cor": VERMELHO, "pos_x": 0, "pos_y": 250, "casa": 0}
}
vez_jogador = "azul"

# Função para desenhar texto com quebra de linha
def desenhar_texto_quebrado(texto, x, y, largura_maxima):
    palavras = texto.split()
    linhas = []
    linha_atual = []
    largura_atual = 0

    for palavra in palavras:
        texto_teste = fonte.render(palavra, True, PRETO)
        largura_palavra = texto_teste.get_width()
        
        if largura_atual + largura_palavra <= largura_maxima:
            linha_atual.append(palavra)
            largura_atual += largura_palavra + fonte.size(' ')[0]
        else:
            linhas.append(' '.join(linha_atual))
            linha_atual = [palavra]
            largura_atual = largura_palavra + fonte.size(' ')[0]
    
    if linha_atual:
        linhas.append(' '.join(linha_atual))

    for i, linha in enumerate(linhas):
        texto_surface = fonte.render(linha, True, PRETO)
        tela.blit(texto_surface, (x, y + i * 25))
    
    return len(linhas) * 25

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    for linha in range(2):
        for coluna in range(7):
            x = coluna * tamanho_celula
            y = linha * tamanho_celula + 200
            pygame.draw.rect(tela, PRETO, (x, y, tamanho_celula, tamanho_celula), 2)

# Função para desenhar a parede com bolas
def desenhar_parede():
    for i in range(40):
        x = (i % 10) * (tamanho_bola + espaco_bola) + 50
        y = (i // 10) * (tamanho_bola + espaco_bola) + 50
        cor = CINZA if i in perguntas_usadas else ROXO
        pygame.draw.circle(tela, cor, (x, y), tamanho_bola)
        texto = fonte.render(str(i + 1), True, BRANCO)
        tela.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))

# Função para exibir a área lateral
def mostrar_area_lateral():
    largura_area = 550
    altura_area = altura_tela - 100
    x_area = largura_tela - largura_area - 20
    y_area = 50

    # Redimensionar a imagem para cobrir toda a área lateral 
    fundo_imagem_redimensionada = pygame.transform.scale(fundo_imagem, (largura_area, altura_area))

    # Desenhar a imagem de plano de fundo em toda a área lateral 
    tela.blit(fundo_imagem_redimensionada, (x_area, y_area))

    pygame.draw.rect(tela, VERDE, (x_area, y_area, largura_area, altura_area))
    pygame.draw.rect(tela, PRETO, (x_area, y_area, largura_area, altura_area), 3)

    if jogo_terminado:
        altura_texto = desenhar_texto_quebrado(mensagem_vitoria, 
                                             x_area + 10, y_area + 20, 
                                             largura_area - 20)
        return None, None
    if pergunta_selecionada is not None:
        altura_texto = desenhar_texto_quebrado(perguntas[pergunta_selecionada], 
                                            x_area + 10, y_area + 20, 
                                            largura_area - 20)
        
        # As opções agora são uma lista de listas
        for i, opcao in enumerate(opcoes[pergunta_selecionada]):
            desenhar_texto_quebrado(opcao, x_area + 10, y_area + 40 + altura_texto + i * 25, largura_area - 20)

        if resposta_revelada:
            desenhar_texto_quebrado(f"Resposta: {respostas[pergunta_selecionada]}", 
                                x_area + 10, y_area + 30 + altura_texto + (i + 1) * 25, 
                                largura_area - 20)



            # Botões "Acertou" e "Errou"
            largura_botao = 100
            y_botao_acertou = y_area + altura_area - 70
            botao_acertou = pygame.Rect(x_area + 10, y_botao_acertou, largura_botao, 30)
            pygame.draw.rect(tela, AZUL, botao_acertou)  # Mudado para AZUL
            texto_acertou = fonte.render("Acertou", True, BRANCO)
            tela.blit(texto_acertou, (botao_acertou.x + 10, botao_acertou.y + 5))

            botao_errou = pygame.Rect(x_area + 10 + largura_botao + 10, y_botao_acertou, largura_botao, 30)  # Adiciona 10 pixels de espaço entre os botões
            pygame.draw.rect(tela, VERMELHO, botao_errou)
            texto_errou = fonte.render("Errou", True, BRANCO)
            tela.blit(texto_errou, (botao_errou.x + 10, botao_errou.y + 5))

            return botao_acertou, botao_errou
        else:
            largura_botao_revelar = 150
            y_botao_revelar = y_area + altura_area - 70
            botao_revelar = pygame.Rect(x_area + 10, y_botao_revelar, largura_botao_revelar, 30)
            pygame.draw.rect(tela, PRETO, botao_revelar)
            texto_revelar = fonte.render("Revelar Resposta", True, BRANCO)
            tela.blit(texto_revelar, (botao_revelar.x + 10, botao_revelar.y + 5))
            return botao_revelar, None

    return None, None

# Função para movimentar o jogador
def movimentar_jogador(acertou):
    global vez_jogador, jogo_terminado
    jogador = jogadores[vez_jogador]
    if acertou:
        jogador["casa"] += 1
        if jogador["casa"] >= 6:  # Última casa (índice 6 = 7ª casa)
            jogador["casa"] = 6
            jogador["pos_x"] = 6 * tamanho_celula
            jogo_terminado = True
            return

    else:
        jogador["casa"] = max(0, jogador["casa"] - 1)

    jogador["pos_x"] = (jogador["casa"] % 7) * tamanho_celula
    jogador["pos_y"] = 200 if vez_jogador == "azul" else 250

    # Alternar para o próximo jogador
    vez_jogador = "vermelho" if vez_jogador == "azul" else "azul"

# Loop principal
while True:
    tela.fill(BRANCO)
    desenhar_tabuleiro()
    desenhar_parede()
    
    # Desenhar os jogadores
    for jogador in jogadores.values():
        pygame.draw.rect(tela, jogador["cor"], (jogador["pos_x"], jogador["pos_y"], tamanho_celula, tamanho_celula))

    botoes = mostrar_area_lateral()
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not jogo_terminado:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Verificar clique em uma bola
            for i in range(40):
                x = (i % 10) * (tamanho_bola + espaco_bola) + 50
                y = (i // 10) * (tamanho_bola + espaco_bola) + 50
                if (x - mouse_x) ** 2 + (y - mouse_y) ** 2 <= tamanho_bola ** 2:
                    if i not in perguntas_usadas:  # Só permite selecionar perguntas não usadas
                        pergunta_selecionada = i
                        resposta_revelada = False
                        perguntas_usadas.add(i)  # Adiciona a pergunta ao conjunto de usadas
                    break

            # Verificar clique nos botões
            if botoes and botoes[0]:  # Se existe algum botão
                if not resposta_revelada:
                    # Botão "Revelar Resposta"
                    if botoes[0].collidepoint(mouse_x, mouse_y):
                        resposta_revelada = True
                else:
                    # Botão "Acertou"
                    if botoes[0].collidepoint(mouse_x, mouse_y):
                        movimentar_jogador(True)
                        pergunta_selecionada = None
                        resposta_revelada = False
                    # Botão "Errou"
                    elif botoes[1] and botoes[1].collidepoint(mouse_x, mouse_y):
                        movimentar_jogador(False)
                        pergunta_selecionada = None
                        resposta_revelada = False

    pygame.display.flip()