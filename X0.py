import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 300, 350  # Увеличиваем высоту для отображения информации о ходе
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Создание объекта шрифта для отображения информации о ходах
font = pygame.font.SysFont(None, 30)

# Функция отрисовки сетки игрового поля
def draw_grid():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT - 50), LINE_WIDTH)  # Уменьшаем высоту на 50 пикселей

# Функция отрисовки крестика
def draw_x(row, col):
    x_offset = SQUARE_SIZE * 0.1
    y_offset = SQUARE_SIZE * 0.1
    pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + x_offset, row * SQUARE_SIZE + y_offset),
                     (col * SQUARE_SIZE + SQUARE_SIZE - x_offset, row * SQUARE_SIZE + SQUARE_SIZE - y_offset), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + x_offset, row * SQUARE_SIZE + SQUARE_SIZE - y_offset),
                     (col * SQUARE_SIZE + SQUARE_SIZE - x_offset, row * SQUARE_SIZE + y_offset), LINE_WIDTH)

# Функция отрисовки нолика
def draw_o(row, col):
    center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
    center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2
    radius = SQUARE_SIZE // 2 - 10
    pygame.draw.circle(screen, BLACK, (center_x, center_y), radius, LINE_WIDTH)

# Функция проверки победителя
def check_winner(board, player):
    # Проверка строк и столбцов
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player for j in range(BOARD_COLS)):
            return True
        if all(board[j][i] == player for j in range(BOARD_ROWS)):
            return True

    # Проверка диагоналей
    if all(board[i][i] == player for i in range(BOARD_ROWS)):
        return True
    if all(board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)):
        return True

    return False

# Функция отрисовки информации о ходе
def draw_turn_info(current_player):
    turn_text = font.render(f"Turn: {current_player}", True, BLACK)
    screen.blit(turn_text, (10, HEIGHT - 40))  # Размещаем ниже игрового поля

# Функция основной игровой логики
def tic_tac_toe():
    """
    Main game func

    Args:
        None.

    Returns:
        None.
    """

    # Игровое поле
    board = [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

    # Текущий игрок
    current_player = "X"

    # Цикл игры
    while True:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Обработка нажатия кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN and not check_winner(board, current_player):
                row = event.pos[1] // SQUARE_SIZE
                col = event.pos[0] // SQUARE_SIZE

                # Проверка, свободна ли ячейка
                if board[row][col] == " ":
                    # Заполнение ячейки
                    board[row][col] = current_player

                    # Отрисовка символа
                    if current_player == "X":
                        draw_x(row, col)
                        current_player = "O"
                    else:
                        draw_o(row, col)
                        current_player = "X"

                    # Проверка победителя
                    if check_winner(board, "X"):
                        print("Player X wins!")
                        return  # Выход из игрового цикла
                    elif check_winner(board, "O"):
                        print("Player O wins!")
                        return  # Выход из игрового цикла
                    elif all(board[i][j] != " " for i in range(BOARD_ROWS) for j in range(BOARD_COLS)):
                        print("It's a tie!")
                        return  # Выход из игрового цикла

        # Очистка экрана
        screen.fill(WHITE)

        # Отрисовка сетки
        draw_grid()

        # Отрисовка символов
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if board[i][j] == "X":
                    draw_x(i, j)
                elif board[i][j] == "O":
                    draw_o(i, j)

        # Отрисовка информации о ходе
        draw_turn_info(current_player)

        # Обновление экрана
        pygame.display.update()

        # Переворот буфера
        pygame.display.flip()

if __name__ == "__main__":
    tic_tac_toe()