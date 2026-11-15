import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def create_board(board_size, visited):
    """Выводит маршрут коня в консоль."""
    board = [
        ['.' for _ in range(board_size)]
        for _ in range(board_size)
    ]

    for (x, y), move in visited.items():
        board[y][x] = str(move)

    for row in board:
        print(' '.join(f'{cell:>2}' for cell in row))


def draw_board(board_size, visited):
    """Рисует маршрут коня на шахматной доске."""
    fig, ax = plt.subplots()

    light_color = "#EEEED2"
    dark_color = "#769656"

    # Рисуем клетки шахматной доски
    for x in range(board_size):
        for y in range(board_size):
            cell_color = (
                light_color
                if (x + y) % 2 == 0
                else dark_color
            )

            square = Rectangle(
                (x, y),
                1,
                1,
                facecolor=cell_color
            )

            ax.add_patch(square)

    # Рисуем рамку вокруг доски
    border = Rectangle(
        (0, 0),
        board_size,
        board_size,
        fill=False,
        edgecolor="#3C3C3C",
        linewidth=2,
        clip_on=False
    )

    ax.add_patch(border)

    # Добавляем номера ходов
    for (x, y), move in visited.items():
        ax.text(
            x + 0.5,
            y + 0.5,
            str(move),
            ha="center",
            va="center"
        )

    # Настраиваем отображение
    ax.set_xlim(0, board_size)
    ax.set_ylim(board_size, 0)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.show()