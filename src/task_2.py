# Задача 2: равновесие гирь

from traceback import print_exception

from task_1 import exercise_1_core


def exercise_2_core(
        count_elements: int,
        weights: list[int]) -> bool:
    """
    Функция решения задачи №2
    """
    if count_elements == 0:
        raise ValueError('Количество элементов не может равняться нулю')
    if count_elements != len(weights):
        raise ValueError(f'Количество весов не равно {count_elements}')
    if len(weights) > 100:
        raise ValueError('Количество весов больше 100')
    if max(weights) > 100:
        raise ValueError('Максимальный вес больше 100')
    if sum(weights) % 2:
        return False

    max_weight = int(sum(weights) / 2)
    max_cost = exercise_1_core(
        count_elements=count_elements,
        max_weight=max_weight,
        weights=weights,
        costs=weights)

    return max_cost == int(sum(weights) / 2)


def test_1():
    result = exercise_2_core(
        count_elements=4,
        weights=[1, 2, 3, 4])
    assert result


def test_2():
    result = exercise_2_core(
        count_elements=5,
        weights=[8, 4, 5, 3, 20])
    assert result


def test_3():
    result = exercise_2_core(
        count_elements=5,
        weights=[8, 4, 5, 3, 21])
    assert not result


if __name__ == '__main__':
    n = int(input("Введите кол-во предметов (N): ")
            .replace(',', ' '))
    w_list = list(map(int, input(f"Введите {n} масс(ы) гирь: ")
                      .replace(',', ' ')
                      .split()))

    try:
        result = exercise_2_core(
            count_elements=n,
            weights=w_list)
        print(f'{result}')
    except Exception as ex:
        print_exception(ex)
