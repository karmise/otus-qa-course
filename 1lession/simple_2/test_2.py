"""Простые тесты"""


def test_list(func3):
    """Проверяем, что список list2 равен 50, 2.51, True"""
    list1 = [1, 'a', 2, 50, 2.51, True]
    list2 = list1[3:]
    assert list2 == [50, 2.51, True]
