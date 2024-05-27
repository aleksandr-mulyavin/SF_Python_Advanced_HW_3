# Задача 1: расчет максимальной стоимости рюкзака

import numpy as np

from traceback import print_exception


def exercise_1_core(
        count_elements: int,
        max_weight: int,
        weights: list[int],
        costs: list[int],
        disable_checks: bool = False
) -> int:
    """
    Функция решения задачи №1
    """
    if not disable_checks:
        if count_elements == 0:
            raise ValueError('Количество элементов не может равняться нулю')
        if count_elements != len(weights) or count_elements != len(costs):
            raise ValueError(f'Количество элементов и/или количество весов/стоимостей не равно {count_elements}')
        if len(weights) > 100:
            raise ValueError(f'Количество весов/стоимостей больше 100')
        if max_weight > 10_000:
            raise ValueError(f'Максимальный вес больше 10_000')

    # Инициализация массива
    values: np.ndarray = np.zeros(
        shape=(count_elements + 1, max_weight + 1),
        dtype=np.int32)

    # Перебор всех ячеек массива и вычисление максимального веса
    for i in range(values.shape[0]):
        for w in range(values.shape[1]):
            # Для нулевых строк и столбцов будет 0
            if i == 0 or w == 0:
                values[i][w] = 0
                continue
            # Получение веса и цены для данной вещи
            weight: int = weights[i - 1]
            cost: int = costs[i - 1]
            # Если вес вещи меньше чем столбец веса,
            # то посчитаем набольший подходящий вес
            if weight <= w:
                values[i][w] = max(
                    cost + values[i - 1][w - weight],
                    values[i - 1][w])
                continue
            # Иначе вес копируется от предыдущей вещи
            values[i][w] = values[i - 1][w]

    return int(values[count_elements][max_weight])


def test_1():
    value = exercise_1_core(
        count_elements=3,
        max_weight=4,
        weights=[4, 1, 3],
        costs=[4000, 2500, 2000])
    assert value == 4500


def test_2():
    value = exercise_1_core(
        count_elements=4,
        max_weight=4,
        weights=[1, 1, 2, 3],
        costs=[3, 1, 5, 3])
    assert value == 9


def test_3():
    value = exercise_1_core(
        count_elements=10,
        max_weight=900,
        weights=[790, 220, 572, 761, 41, 383, 205, 846, 848, 627],
        costs=[273, 34, 21, 14, 270, 222, 793, 173, 132, 110])
    assert value == 1319


if __name__ == '__main__':
    n, m = map(int, input("Введите Кол-во предметов (N) и Макс. массу (M): ")
               .replace(',', ' ')
               .split())
    w_list = list(map(int, input(f"Введите {n} масс(ы) предметов: ")
                      .replace(',', ' ')
                      .split()))
    c_list = list(map(int, input(f"Введите {n} стоимостей предметов: ")
                      .replace(',', ' ')
                      .split()))

    try:
        result = exercise_1_core(
            count_elements=n,
            max_weight=m,
            weights=w_list,
            costs=c_list)
        print(f'{result}')
    except Exception as ex:
        print_exception(ex)
