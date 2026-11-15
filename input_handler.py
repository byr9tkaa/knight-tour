def get_integer(prompt):
    """Получает целое число от пользователя."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите целое число.")


def get_board_size():
    """Получает корректный размер доски."""
    while True:
        board_size = get_integer("Введите размер доски: ")

        if board_size > 0:
            return board_size

        print("Ошибка: размер доски должен быть больше 0.")


def get_knight_coordinates(board_size):
    """Получает корректные координаты начальной позиции коня."""
    while True:
        x = get_integer("Введите координату X: ")
        y = get_integer("Введите координату Y: ")

        if 0 <= x < board_size and 0 <= y < board_size:
            return x, y

        print(
            f"Ошибка: координаты должны быть в диапазоне "
            f"от 0 до {board_size - 1}."
        )