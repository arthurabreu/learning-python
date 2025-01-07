# snake.py
from asciimatics.screen import Screen
from asciimatics.event import KeyboardEvent
from asciimatics.exceptions import ResizeScreenError, NextScene
import sys
import time
import random

def game_loop(screen):
    # Inicialização do jogo
    snake = [(10, 10), (10, 9), (10, 8)]
    direction = (0, 1)  # Inicialmente para a direita
    food = (random.randint(1, screen.height - 2), random.randint(1, screen.width - 2))
    score = 0
    speed = 0.1  # Tempo entre atualizações

    while True:
        event = screen.get_event()
        if isinstance(event, KeyboardEvent):
            screen.print_at(f"Tecla: {event.key_code}", 0, screen.height - 1, colour=Screen.COLOUR_YELLOW)
            if event.key_code in [Screen.KEY_ESCAPE, ord('q')]:  # 'q' ou 'Esc' para sair
                raise NextScene("main")
            elif event.key_code == Screen.KEY_UP and direction != (1, 0):
                direction = (-1, 0)
            elif event.key_code == Screen.KEY_DOWN and direction != (-1, 0):
                direction = (1, 0)
            elif event.key_code == Screen.KEY_LEFT and direction != (0, 1):
                direction = (0, -1)
            elif event.key_code == Screen.KEY_RIGHT and direction != (0, -1):
                direction = (0, 1)

        # Calcular nova cabeça
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Verificar colisões com paredes
        if (new_head[0] < 0 or new_head[0] >= screen.height or
            new_head[1] < 0 or new_head[1] >= screen.width):
            break

        # Verificar colisão consigo mesmo
        if new_head in snake:
            break

        # Adicionar nova cabeça
        snake.insert(0, new_head)

        # Verificar se comeu a comida
        if new_head == food:
            score += 1
            # Gerar nova comida
            while True:
                food = (random.randint(1, screen.height - 2), random.randint(1, screen.width - 2))
                if food not in snake:
                    break
        else:
            # Remover a cauda
            snake.pop()

        # Limpar a tela
        screen.clear()

        # Desenhar comida
        screen.print_at('*', food[1], food[0], colour=Screen.COLOUR_RED)

        # Desenhar cobra
        for y, x in snake:
            screen.print_at('O', x, y, colour=Screen.COLOUR_GREEN)

        # Desenhar a pontuação
        screen.print_at(f'Score: {score}', 0, 0, colour=Screen.COLOUR_WHITE)

        # Atualizar a tela
        screen.refresh()

        # Controlar a velocidade
        time.sleep(speed)

    # Game over
    screen.clear()
    screen.print_at('Game Over!', screen.width//2 - 5, screen.height//2, colour=Screen.COLOUR_RED)
    screen.print_at(f'Score: {score}', screen.width//2 - 5, screen.height//2 + 1, colour=Screen.COLOUR_WHITE)
    screen.refresh()
    time.sleep(3)

if __name__ == '__main__':
    Screen.wrapper(game_loop)
    
    
    
    
    
# Controles do Jogo:
# Movimentação: Use as setas do teclado para mover a cobra (Cima, Baixo, Esquerda, Direita).
# Sair do Jogo: Pressione q para sair a qualquer momento.
# Descrição do Funcionamento:
# Inicialização:

# A cobra é representada por uma lista de coordenadas (y, x).
# A direção inicial é para a direita (0, 1).
# Uma comida é colocada em uma posição aleatória.
# Loop Principal:

# Captura eventos de teclado para mudar a direção da cobra.
# Calcula a nova posição da cabeça da cobra.
# Verifica colisões com paredes ou consigo mesma.
# Se a cobra come a comida, aumenta o score e gera uma nova comida.
# Atualiza a posição da cobra e a tela.
# Game Over:

# Exibe a mensagem "Game Over" e a pontuação final após uma colisão.
# Considerações Finais:
# Velocidade do Jogo: Você pode ajustar a variável speed para tornar o jogo mais rápido ou mais lento.
# Melhorias Possíveis:
# Adicionar níveis de dificuldade.
# Introduzir obstáculos.
# Implementar uma interface mais elaborada.    