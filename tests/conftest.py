"""Sharing fixture functions."""
import pytest
from collections import namedtuple


@pytest.fixture
def db_conn():
    """Some db connection fixture."""
    print('initial db connection!')
    DBconn = namedtuple("DBconn", ["ip", "port"])
    yield DBconn(ip='127.0.0.1', port='5432')
    print('close db connection!')
    del DBconn
