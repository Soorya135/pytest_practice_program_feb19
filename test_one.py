import pytest


@pytest.mark.smoke
def test_regression():
    print("hello world")
    assert 1 == 1


@pytest.mark.regression
def test_two():
    print("hello world")
    assert 1 == 1


@pytest.mark.soorya
def test_three():
    print("hello world")
    assert 1 == 1

@pytest.mark.skip
def test_three_four():
    print("hello world")
    assert 1 == 1

@pytest.mark.xfail
def test_three_four_five():
    print("hello world")
    assert 1 == 1


