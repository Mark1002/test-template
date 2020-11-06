## Unit Test Template

### development
This project is developed by [poetry](https://python-poetry.org/), a python virtual environment and project management tool.
### installation
Make sure ``export PATH="$HOME/.poetry/bin:$PATH"``
```
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

$ cd test-template && poetry install

# activate poetry virtual environment
$ poetry shell
```


### run test
1. all test
```
$ pytest
```
2. specify run one test
```
$ pytest tests/test_test_template.py::TestModuleClass1::test_add_two_number -s
```
```
pytest tests/test_test_template.py::test_version -s      
```