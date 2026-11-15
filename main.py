from board import create_board, draw_board
from input_handler import (
    get_board_size,
    get_integer,
    get_knight_coordinates
)
from knight import random_route, warnsdorff_route
from validator import validate_route


MENU_OPTIONS_LIMIT = 5


def get_output_mode_name(output_mode):
    """Возвращает название текущего способа вывода."""
    output_modes = {
        1: "в консоли",
        2: "на доске",
        3: "в консоли и на доске"
    }

    return output_modes[output_mode]


def show_menu(board_size, output_mode):
    """Выводит главное меню и текущие настройки."""
    print("\n" + "=" * 50)
    print("                 МАРШРУТ КОНЯ")
    print("=" * 50)

    print("\nТекущие настройки:")
    print(f"  Размер доски  : {board_size}x{board_size}")
    print(f"  Способ вывода : {get_output_mode_name(output_mode)}")

    print("\n" + "-" * 50)

    return get_integer(
        "1 — Случайный маршрут\n"
        "2 — Алгоритм Варнсдорфа\n"
        "3 — Изменить размер доски\n"
        "4 — Изменить способ вывода\n"
        "0 — Выход\n\n"
        "Выберите действие: "
    )


def get_output_mode():
    """Получает способ вывода маршрута."""
    while True:
        print("\n" + "-" * 50)
        print("Выберите способ вывода:")
        print("1 — В консоли")
        print("2 — На доске")
        print("3 — В консоли и на доске")
        print("-" * 50)

        output_mode = get_integer("Ваш выбор: ")

        if 1 <= output_mode <= 3:
            return output_mode

        print("\nОшибка: выберите число от 1 до 3.")


def show_route_result(result):
    """Выводит результат проверки маршрута."""
    print("\n" + "-" * 50)
    print("Результат построения маршрута:")
    print("-" * 50)

    if not result["valid"]:
        print("  Статус          : маршрут некорректный")
        print("-" * 50)
        return

    print(
        f"  Пройдено клеток : "
        f"{result['visited']}/{result['total']}"
    )

    if result["complete"]:
        print("  Статус          : полный маршрут")
    else:
        print("  Статус          : маршрут завершился раньше")

    print("-" * 50)


def main():
    board_size = 8
    output_mode = 2

    while True:
        method = show_menu(board_size, output_mode)

        # Проверяем, что выбран существующий пункт меню
        if not 0 <= method < MENU_OPTIONS_LIMIT:
            print("\nОшибка: такого пункта меню нет.")
            continue

        match method:
            case 0:
                print("\nПрограмма завершена.\n")
                break

            case 1 | 2:
                x, y = get_knight_coordinates(board_size)

                if method == 1:
                    algorithm_name = "Случайный маршрут"
                else:
                    algorithm_name = "Алгоритм Варнсдорфа"

                print("\n" + "=" * 50)
                print(f"             {algorithm_name}")
                print("=" * 50)

                print(f"Размер доски      : {board_size}x{board_size}")
                print(f"Начальная позиция : ({x}, {y})")

                print("\nПостроение маршрута...")

                move_number = 1
                visited = {(x, y): move_number}

                if method == 1:
                    visited = random_route(
                        x,
                        y,
                        board_size,
                        visited,
                        move_number
                    )
                else:
                    visited = warnsdorff_route(
                        x,
                        y,
                        board_size,
                        visited,
                        move_number
                    )

                print("\nМаршрут построен.")

                result = validate_route(
                    board_size,
                    visited
                )

                show_route_result(result)

                if output_mode == 1:
                    create_board(board_size, visited)

                elif output_mode == 2:
                    draw_board(board_size, visited)

                else:
                    create_board(board_size, visited)
                    draw_board(board_size, visited)

            case 3:
                board_size = get_board_size()

                print(
                    f"\nРазмер доски изменён: "
                    f"{board_size}x{board_size}"
                )

            case 4:
                output_mode = get_output_mode()

                print(
                    f"\nСпособ вывода изменён: "
                    f"{get_output_mode_name(output_mode)}"
                )


if __name__ == "__main__":
    main()