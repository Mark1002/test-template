"""Test case for services."""
import pytest
from services import __version__
from services.module import ModuleClass1
from services.module import ModuleClass2
# for mock
from services.module import requests


def test_version():
    assert __version__ == '0.1.0'


def test_demo_fixture(db_conn):
    """Demo for user define pytest fixture."""
    assert db_conn.port == '5432'


class TestModuleClass1:
    """Test for module class 1."""

    def setup_method(self):
        print("setup_method called for every method")
        self.obj = ModuleClass1()

    def teardown_method(self):
        print("teardown_method called for every method")
        del self.obj

    def test_add_two_number_to_100(self):
        # given
        n1, n2 = 32, 68
        # when
        total = self.obj.add_two_number(n1, n2)
        # then
        assert total == 100

    @pytest.mark.parametrize(
        "n1, n2, result",
        [
            (3, 3, 9),
            (8, 7, 56),
            (7, 9, 63)
        ]
    )
    def test_multiply_two_number(self, n1: int, n2: int, result: int):
        """multiple parameter unit test."""
        assert self.obj.multiply_two_number(n1, n2) == result


class TestModuleClass2:
    """Test for module class 2."""

    def setup_method(self):
        print("setup_method called for every method")
        self.obj = ModuleClass2()

    def teardown_method(self):
        print("teardown_method called for every method")
        del self.obj

    def test_get_my_ip(self, monkeypatch):
        """Mock test demo."""
        my_ip = '127.0.0.1'

        class MockResponse:
            """Mock response class."""
            def __init__(self, json_body):
                self.json_body = json_body

            def json(self):
                return self.json_body
        # mock request's get function
        monkeypatch.setattr(
            requests, 'get', lambda x: MockResponse({'ip': my_ip})
        )
        assert self.obj.get_my_ip() == my_ip
