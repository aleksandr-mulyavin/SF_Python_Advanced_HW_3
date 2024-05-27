# Задача 4: расчет максимальной стоимости рюкзака

from traceback import print_exception


def exercise_4_core(
        count_elements: int,
        max_weight: int,
        weights: list[int],
        disable_checks: bool = False
) -> int:
    """
    Функция решения задачи №4 (основная)
    """
    if not disable_checks:
        if count_elements == 0:
            raise ValueError('Количество элементов не может равняться нулю')
        if count_elements != len(weights):
            raise ValueError(f'Количество весов не равно {count_elements}')
        if len(weights) > 100:
            raise ValueError(f'Весов больше 100')
        if max_weight > 10_000:
            raise ValueError(f'{max_weight} больше 10_000')
        if max(weights) > 100:
            raise ValueError(f'Веса не могут быть больше 100')

    # Инициализация списка значений длинной M + 1
    # Значение для каждого элемента будет N + 1
    init_val = 99999
    data: list[int] = [init_val for i in range(max_weight + 1)]

    # Значение с индексом 0 равно 0
    data[0] = 0

    # Перебор весов предметов
    for weight in weights:
        # Получение значений для каждого элемента
        for i in range(max_weight, weight - 1, -1):
            if data[i] > data[i - weight] + 1:
                data[i] = data[i - weight] + 1

    print(data)
    return 0 if data[max_weight] == init_val else data[max_weight]


def test_1():
    value = exercise_4_core(
        count_elements=5,
        max_weight=10,
        weights=[1, 5, 3, 2, 4]
    )
    assert value == 3


def test_2():
    value = exercise_4_core(
        count_elements=5,
        max_weight=10,
        weights=[8, 5, 3, 1, 3])
    assert value == 0


def test_3():
    value = exercise_4_core(
        count_elements=5,
        max_weight=10,
        weights=[1, 5, 3, 2, 4])
    assert value == 3


if __name__ == '__main__':
    n, m = map(int, input("Введите Кол-во предметов (N) и Макс.массу (M): ")
               .replace(',', ' ')
               .split())
    w_list = list(map(int, input(f"Введите {n} масс(ы) предметов: ")
                      .replace(',', ' ')
                      .split()))

    try:
        result = exercise_4_core(
            count_elements=n,
            max_weight=m,
            weights=w_list)
        print(f'{result}')
    except Exception as ex:
        print_exception(ex)
