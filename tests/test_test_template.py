from test_template import __version__
from test_template.module import ModuleClass1


def test_version():
    assert __version__ == '0.1.0'


def test_demo_fixture(db_conn):
    """Demo for pytest fixture."""
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
