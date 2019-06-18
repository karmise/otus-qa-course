"""Простые тесты"""


def test_dict(func3):
    """Проверяем, что словарь dict равен {'name': 'Denis', 'status': 'online'} после замены значения в ключе 'status'"""
    dict = {'name': 'Denis', 'status': 'offline'}
    dict['status'] = 'online'
    assert dict == {'name': 'Denis', 'status': 'online'}
