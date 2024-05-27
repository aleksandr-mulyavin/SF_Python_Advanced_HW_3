# Задача 5: Количество способов добраться фигурой до угла доски

import numpy as np

from traceback import print_exception

# Разрешенные схемы движения фигуры (стоки, столбцы)
MOVEMENTS: list[tuple[int, int]] = [(2, 1), (1, 2)]


def exercise_5_core(rows: int, columns: int) -> int:
    """
    Функция решения задачи №5 (основная)
    """
    if rows < 1:
        raise ValueError(f'{rows} меньше 1')
    if rows > 50:
        raise ValueError(f'{rows} больше 50')
    if columns < 1:
        raise ValueError(f'{columns} меньше 1')
    if columns > 50:
        raise ValueError(f'{columns} больше 50')


    # Инициализация массива N x M
    desk: np.ndarray = np.zeros(
        shape=(rows, columns),
        dtype=np.int64)

    # Получим максимальный шаг по вертикали и горизонтали
    max_row_move: int = max([move[0] for move in MOVEMENTS])
    max_col_move: int = max([move[1] for move in MOVEMENTS])

    # В условиях не полное ограничение!
    # Фигура не может двигаться, если высота
    # или ширина меньше максимального шага
    if rows < max_row_move or columns < max_col_move:
        return 0

    # Инициализация начального числа
    desk[0][0] = 1

    # Перебор строки и столбцов для расчета сумм ходов по шагам
    for row in range(rows):
        for column in range(columns):
            # Если сумма ячейки 0, то фигура сюда не ходила,
            # а значит и отсюда не пойдет
            if not desk[row][column]:
                continue
            # Перебор доступных движений фигуры
            for move in MOVEMENTS:
                # Получение шагов по горизонтали и вертикали
                row_move: int = move[0]
                col_move: int = move[1]
                # Если индекс ячейки плюс шаг выходит за рамки,
                # то ходить дальше нельзя, иначе сходим
                if rows > row + row_move >= 0 \
                        and columns > column + col_move >= 0:
                    # Прибавляем количество попаданий ячейки
                    # в последующие с учетом возможных шагов
                    desk[row + row_move][column + col_move] += desk[row][column]

    # Вернем весь массив
    return int(desk[rows - 1][columns - 1])


def test_1():
    value = exercise_5_core(
        rows=3,
        columns=3)
    assert value == 0


def test_2():
    value = exercise_5_core(
        rows=3,
        columns=5)
    assert value == 1


def test_3():
    value = exercise_5_core(
        rows=6,
        columns=5)
    assert value == 3


if __name__ == '__main__':
    n, m = map(int, input("Введите кол-во строк (N) и столбцов (M): ")
               .replace(',', ' ')
               .split())

    try:
        result = exercise_5_core(
            rows=n,
            columns=m)
        print(f'{result}')
    except Exception as ex:
        print_exception(ex)
