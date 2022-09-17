import pytest
import os

from dotenv import load_dotenv, find_dotenv
from class_ya import Yandex

load_dotenv(find_dotenv())
TOKEN = os.getenv('TOKEN')

ya = Yandex(token=TOKEN)


#данные для теста
test_data = [
    ('test1', ('test1', 201)), #создаем новую папку
    ('test2', ('test2', 201)), #создаем новую папку
    ('test1', ('test1', 409)), #папка уже существует
]


@pytest.mark.parametrize('name, result', test_data)
def test_create_directory(name, result):
    assert ya.create_directory(name) == result
