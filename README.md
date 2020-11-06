## Unit Test Template

### Development
This project is developed by [poetry](https://python-poetry.org/), a python virtual environment and project management tool.
### Installation
Make sure ``export PATH="$HOME/.poetry/bin:$PATH"``
```
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

$ cd test-template && poetry install

# activate poetry virtual environment
$ poetry shell
```
### Project structure
```
.
├── README.md
├── poetry.lock
├── pyproject.toml
├── services
│   ├── __init__.py
│   └── module.py
└── tests
    ├── __init__.py
    ├── conftest.py
    └── test_services.py
```
### Run test
1. Run all test
```
$ pytest
```
2. Specify to run one test
```
$ pytest tests/test_services.py::TestModuleClass1::test_add_two_number_to_100 -s
```