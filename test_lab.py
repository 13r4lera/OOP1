from task1 import html
from task2 import People


def test_html():
    assert html("b")("hello") == "<b>hello</b>"

def test_people():
    p = People()
    p.add("Иванов", "Иван", "123", [15, 10, 2005])
    assert p.data[0]["дата"][1] == 10