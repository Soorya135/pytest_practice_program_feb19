import pytest

@pytest.fixture()
def setup():
    print("This is called first")
    yield
    print("This is called last")


def test_using_fixture(setup):
    print("This is called second")