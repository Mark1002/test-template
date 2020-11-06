from test_template import __version__
from test_template.module import ModuleClass1


def test_version():
    assert __version__ == '0.1.0'


class TestModuleClass1:
    """Test for module class 1."""

    def test_add_two_number(obj: ModuleClass1):
        assert 1 == 2
