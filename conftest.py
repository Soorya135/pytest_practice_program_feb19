import pytest


@pytest.fixture()
def setup():
    print("This is called first")
    yield
    print("This is called last")


@pytest.fixture(scope="class")
def setup_scope():
    print("This is called first")
    yield
    print("This is called last")


@pytest.fixture()
def data_load():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome", "Rahul", "Shetty"), ("Firefox", "Rahul", "Shetty"), ("IE", "Rahul", "Shetty")])
def cross_browser(request):
    return request.param
