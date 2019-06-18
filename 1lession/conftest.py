"""Импортируем pytest, создаем фикстуры для дальнейшего использования"""

import pytest


@pytest.fixture()
def func1():
    print("\nprint before each func test")


@pytest.fixture(scope="session")
def func2():
    print("\nprint before session test")


@pytest.fixture(scope="module")
def func3():
    print("\nprint before each module test")
