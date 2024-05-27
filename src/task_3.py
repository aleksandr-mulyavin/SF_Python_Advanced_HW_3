# Задача 3: расчет минимального числа банкнот для набора суммы

from traceback import print_exception


def exercise_3_core(
        paper_cnt: int,
        denominations: list[int],
        amount: int
) -> dict[int, int]:

    if paper_cnt != len(denominations):
        raise ValueError('Количество банкнот не соответсвует заданным параметрам')

    result: dict[int, int] = dict()
    denominations_list = sorted(set(denominations), reverse=True)

    balance = amount
    for denomination in denominations_list:
        quot, rem = divmod(balance, denomination)
        if not quot:
            continue
        result[denomination] = quot
        old_balance = balance
        balance = balance - quot * denomination
        print(f'{old_balance} / {denomination} = {quot} по {denomination} и {rem}')

    if balance:
        result = dict()

    return result


def test_1():
    value = exercise_3_core(
        paper_cnt=6,
        denominations=[50, 100, 200, 500, 1000, 5000],
        amount=1_751)
    assert len(value) == 0


def test_2():
    value = exercise_3_core(
        paper_cnt=6,
        denominations=[50, 100, 200, 500, 1000, 5000],
        amount=2_750)
    assert len(value) != 0


def _conv_result_den_to_str(d: dict) -> str:
    if not d:
        return "No solution"
    return " ".join([" ".join([str(d) for i in range(c)]) for d, c in result.items()])


if __name__ == '__main__':
    n = int(input("Введите кол-во банкнот (N): ")
            .replace(',', ' '))
    d_list = list(map(int, input(f"Введите {n} номиналов банкнот: ")
                      .replace(',', ' ')
                      .split()))
    s = int(input(f"Введите сумму к выдаче: ")
            .replace(',', ' '))

    try:
        result = exercise_3_core(
            paper_cnt=n,
            denominations=d_list,
            amount=s)
        print(f'{_conv_result_den_to_str(result)}')
    except Exception as ex:
        print_exception(ex)
