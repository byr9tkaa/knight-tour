from random import choice


# Все возможные ходы коня
ALL_POSSIBLE_MOVES = [
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
    (-2, 1),
    (-1, 2)
]


def get_possible_moves(x, y, board_size, visited):
    """Возвращает все доступные клетки для следующего хода."""
    possible_moves = []

    for dx, dy in ALL_POSSIBLE_MOVES:
        new_x = x + dx
        new_y = y + dy

        # Проверяем, что клетка находится внутри доски
        if not (0 <= new_x < board_size and 0 <= new_y < board_size):
            continue

        # Проверяем, что на клетке ещё не были
        if (new_x, new_y) in visited:
            continue

        possible_moves.append((new_x, new_y))

    return possible_moves


def random_route(x, y, board_size, visited, move_number):
    """Строит случайный маршрут коня."""
    while True:
        possible_moves = get_possible_moves(
            x,
            y,
            board_size,
            visited
        )

        # Если доступных ходов больше нет, маршрут заканчивается
        if not possible_moves:
            break

        # Случайно выбираем следующую клетку
        x, y = choice(possible_moves)

        move_number += 1
        visited[(x, y)] = move_number

    return visited


def get_move_degree(x, y, board_size, visited):
    """Возвращает количество доступных ходов из клетки."""
    return len(get_possible_moves(x, y, board_size, visited))


def warnsdorff_route(x, y, board_size, visited, move_number):
    """Строит маршрут коня по алгоритму Варнсдорфа."""
    while True:
        possible_moves = get_possible_moves(
            x,
            y,
            board_size,
            visited
        )

        # Если доступных ходов больше нет, маршрут заканчивается
        if not possible_moves:
            break

        # Выбираем клетку с наименьшим количеством дальнейших ходов
        next_move = min(
            possible_moves,
            key=lambda move: get_move_degree(
                move[0],
                move[1],
                board_size,
                visited
            )
        )

        x, y = next_move
        move_number += 1
        visited[(x, y)] = move_number

    return visited