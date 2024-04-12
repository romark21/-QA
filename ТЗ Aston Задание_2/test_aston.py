import Aston
import pytest


@pytest.mark.task_1
@pytest.mark.parametrize('value_1, value_2, expected',
                         [(8, 2, '8 > 2'),
                          (5, 10, '5 < 10'),
                          (23, 23, '23 = 23'),
                          (-1, 6, '-1 < 6'),
                          (10, -5, '10 > -5'),
                          pytest.param(0, 0, '0 > 0', marks=pytest.mark.xfail),
                          pytest.param(34, 31, '34 < 31', marks=pytest.mark.xfail),
                          pytest.param(20, 80, '34 > 31', marks=pytest.mark.xfail),
                          pytest.param(67, 80, '34 = 31', marks=pytest.mark.xfail),
                          pytest.param('a', 80, 'a = 31', marks=pytest.mark.xfail)
                          ])
def test_compares_two_numbers(value_1, value_2, expected):
    assert Aston.compares_two_numbers(value_1, value_2) == expected, 'The actual result does not match the expected!'


@pytest.mark.task_1
@pytest.mark.parametrize('value_1, value_2, expected',
                         [(1, 4, '1 + 4 = 5'),
                          (100, 23, '100 + 23 = 123'),
                          (-1, 5, '-1 + 5 = 4'),
                          pytest.param(20, 10, '20 + 10 = 20', marks=pytest.mark.xfail)
                          ])
def test_additions_numbers(value_1, value_2, expected):
    assert Aston.additions_numbers(value_1, value_2) == expected, 'The actual result does not match the expected!'


@pytest.mark.task_1
@pytest.mark.parametrize('value_1, value_2, expected',
                         [(10, 4, '10 - 4 = 6'),
                          (100, 123, '100 - 123 = -23'),
                          (-1, 5, '-1 - 5 = -6'),
                          pytest.param(20, 10, '20 - 10 = 20', marks=pytest.mark.xfail)
                          ])
def test_subtraction_numbers(value_1, value_2, expected):
    assert Aston.subtraction_numbers(value_1, value_2) == expected, 'The actual result does not match the expected!'


"""
- Для того чтоб запустить определённый тест, в консоли нужно прописать(где -к ,это команда для запуска 
определённого теста + указать названия тест-функции):
pytest -k test_compares_two_numbers

- Для того, чтоб запустить тесты например c mark.task_1, в консоли нужно прописать(где -m ,это команда для запуска
тестов с меткой + указать названия метки):
pytest -m task_1
 Команда -v печатает более детальный отчёт о выполнении тестов.
 Команда -s напечатает принты, если используются в программе
"""