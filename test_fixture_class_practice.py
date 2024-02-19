import pytest


@pytest.mark.usefixtures("setup")
class Test:
    def test_one1(self):
        print("one..1")

    def test_one2(self):
        print("one..2")

    def test_one3(self):
        print("one..3")