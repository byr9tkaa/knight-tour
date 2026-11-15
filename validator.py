from knight import ALL_POSSIBLE_MOVES


def validate_route(board_size, visited):
    """Проверяет корректность построенного маршрута."""
    coordinates = list(visited.keys())
    moves = list(visited.values())
    total_cells = board_size ** 2

    # Проверяем последовательность номеров ходов
    expected_moves = list(range(1, len(moves) + 1))

    if moves != expected_moves:
        return {
            "valid": False,
            "complete": False,
            "visited": len(moves),
            "total": total_cells
        }

    # Проверяем, что каждый ход действительно является ходом коня
    for current, next_position in zip(coordinates, coordinates[1:]):
        x1, y1 = current
        x2, y2 = next_position

        move = (x2 - x1, y2 - y1)

        if move not in ALL_POSSIBLE_MOVES:
            return {
                "valid": False,
                "complete": False,
                "visited": len(moves),
                "total": total_cells
            }

    # Проверяем координаты всех посещённых клеток
    for x, y in coordinates:
        if not (0 <= x < board_size and 0 <= y < board_size):
            return {
                "valid": False,
                "complete": False,
                "visited": len(moves),
                "total": total_cells
            }

    return {
        "valid": True,
        "complete": len(moves) == total_cells,
        "visited": len(moves),
        "total": total_cells
    }