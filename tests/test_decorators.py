import pytest
from src.decorators import log


def test_log_file_ok():
    """Тестирует вывод в файл"""
    @log("mylog.txt")
    def func(x, y):
        return x + y
    func(1, 2)
    with open('mylog.txt') as file:
        result = file.read()
    assert result == 'func ok'


def test_log_file_error():
    """Тестирует вывод после ошибки в файл"""
    with pytest.raises(Exception, match="My_function error"):
        @log("mylog.txt")
        def func(x, y):
            return x + y
        result = log('mylog.txt')
        assert result == "My_function error"


def test_log_console(capsys):
    """Тестирует вывод в консоль"""

    @log(filename='')
    def func(x, y):
        return x + y
    func(2, 3)
    captured = capsys.readouterr()
    assert captured.out == 'func ok\n'


def test_log_console_error(capsys):
    """Тестирует вывод после ошибки в консоль"""
    with pytest.raises (Exception, match="My_function error"):
        @log(filename='')
        def func(x, y):
            return x + y
        captured = capsys.readouterr()
        assert captured.out == "My_function error"
