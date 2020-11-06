from test_template import __version__
from test_template.module import ModuleClass1


def test_version():
    assert __version__ == '0.1.0'


def test_demo_fixture(db_conn):
    assert db_conn.port == '5432'


class TestModuleClass1:
    """Test for module class 1."""

    def test_add_two_number(obj: ModuleClass1, db_conn):
        assert 1 == 2
