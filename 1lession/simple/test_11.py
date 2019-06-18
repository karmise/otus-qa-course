"""Простые тесты"""


def test_multiplication(func1):
    """Проверяем, что (2+2)*4 равно 16"""
    assert (2+2)*4 == 16


def test_division(func1):
    """Проверяем, что ((2+2)*4)/2 равно 8"""
    assert ((2+2)*4)/2 == 8


def test_addition(func1):
    """Проверяем, что 200+50 не равно 300"""
    assert 200+50 != 300


def test_odd_number(func1):
    """Проверяем, что при делении 121 на 22 остаток будет равен 11"""
    assert 121 % 22 == 11


def test_subtraction(func1):
    """Проверяем, что разница между 500 и 400 равна 100"""
    assert 500-400 == 100


def test_len_string(func1):
    """Проверяем, что длинна строки равна 4"""
    string = 'otus'
    assert len(string) == 4


def test_tuple(func1):
    """Проверяем, что 44 встречается 3 раза в кортеже"""
    negative_val = (1, 'name', 44, 21, 2.33, 44, False, -2, 44)
    assert negative_val.count(44) == 3


def test_set(func2):
    """Проверка на уникальность первого множества со вторым"""
    mul1 = {5, 4, 2, 9}
    mul2 = {1, 7, 3, 8}
    assert mul1.isdisjoint(mul2) is True
