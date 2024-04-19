from Aston import Task1, Task2, Task3
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
    t_1 = Task1(value_1, value_2)

    assert t_1.compares_two_numbers() == expected, 'The actual result does not match the expected!'


@pytest.mark.task_1
@pytest.mark.parametrize('value_1, value_2, expected',
                         [(1, 4, '1 + 4 = 5'),
                          (100, 23, '100 + 23 = 123'),
                          (-1, 5, '-1 + 5 = 4'),
                          pytest.param(20, 10, '20 + 10 = 20', marks=pytest.mark.xfail)
                          ])
def test_additions_numbers(value_1, value_2, expected):
    t_1 = Task1(value_1, value_2)
    assert t_1.additions_numbers() == expected, 'The actual result does not match the expected!'


@pytest.mark.task_1
@pytest.mark.parametrize('value_1, value_2, expected',
                         [(10, 4, '10 - 4 = 6'),
                          (100, 123, '100 - 123 = -23'),
                          (-1, 5, '-1 - 5 = -6'),
                          pytest.param(20, 10, '20 - 10 = 20', marks=pytest.mark.xfail)
                          ])
def test_subtraction_numbers(value_1, value_2, expected):
    t_1 = Task1(value_1, value_2)
    assert t_1.subtraction_numbers() == expected, 'The actual result does not match the expected!'

    exception = Task1('e', '')
    with pytest.raises(Exception):  # Ожидаем, что будет выброшено исключение TypeError.
        assert exception.subtraction_numbers(), ''


@pytest.mark.task_1
@pytest.mark.parametrize('value_1, value_2, expected',
                         [(12, 4, '12 : 4 = 3.0'),
                          (15, 20, '15 : 20 = 0.75')])
def test_division_numbers(value_1, value_2, expected):
    t_1 = Task1(value_1, value_2)
    assert t_1.division_numbers() == expected


@pytest.mark.task_2
@pytest.mark.parametrize('string_1, string_2, expected',
                         [('Hello', 'Hello', 'The strings are identical!'),
                          ('world', 'world', 'The strings are identical!'),
                          (' ', ' ', 'The strings are identical!'),
                          ('10', '10', 'The strings are identical!'),
                          ('qwer ty@123456', 'qwer ty@123456', 'The strings are identical!'),
                          ('Test', 'test', 'The strings are non-identical!'),
                          ('system', 'System', 'The strings are non-identical!'),
                          ('1', '-1', 'The strings are non-identical!'),
                          (' ', '  ', 'The strings are non-identical!')])
def test_compares_two_strings(string_1, string_2, expected):
    t_2 = Task2(string_1, string_2)
    assert t_2.compares_two_strings() == expected


@pytest.mark.task_3
@pytest.mark.parametrize('value, expected',
                         [(6, [0, 2, 4, 6]),
                          (9, [0, 2, 4, 6, 8]),
                          (11, [0, 2, 4, 6, 8, 10])])
def test_even_numbers(value, expected):
    t_3 = Task3(value)
    assert t_3.even_numbers() == expected


"""
- Для того чтоб запустить определённый тест, в консоли нужно прописать(где -к ,это команда для запуска 
определённого теста + указать названия тест-функции):
pytest -k test_compares_two_numbers

- Для того, чтоб запустить тесты например c mark.task_1, в консоли нужно прописать(где -m ,это команда для запуска
тестов с меткой + указать названия метки):
pytest -m task_1

- Если есть файл, который содержит список тестов для выполнения, то его можно использовать для выбора тестов. 
Для этого нужно передать этот файл в качестве аргумента команде pytest. 
Например, команда pytest -m @tests.txt запустит все тесты, указанные в файле tests.txt.

 Команда -v печатает более детальный отчёт о выполнении тестов.
 Команда -s напечатает принты, если используются в программе
"""
