# Simply pytest example
1) Simple Project: two files that reference each other.
2) DataHandler class imports data from an outside source.
3) Model class is a composite class that includes DataHandler.

# Installation
```
python3 -m venv venv
. venv/bin/activate
pip3 install -e .[dev]
```

# Topics Covered
1. [test file discovery](https://docs.pytest.org/en/latest/getting-started.html#run-multiple-tests), [test discovery](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery)
1. [monkeypatch](https://docs.pytest.org/en/latest/monkeypatch.html)
1. [pytest.ini](https://docs.pytest.org/en/latest/customize.html)
1. [fixtures](https://docs.pytest.org/en/latest/fixture.html)
1. [scopes](https://docs.pytest.org/en/latest/fixture.html#scope-sharing-a-fixture-instance-across-tests-in-a-class-module-or-session)
1. [setUp/tearDown](https://docs.pytest.org/en/latest/fixture.html#fixture-finalization-executing-teardown-code)

# Order
1. DataHandler and Model class review
1. Mock load_data with monkeypatch
1. DataHandler - Mocking Data - awkward
2. DataHandler - Mocking Data - monkeypatch
3. DataHandler - Mocking Data - scope


# Useful commands

Run all test located by pytest
```
pytest .   # Run all tests
pytest -k <test_name>  # Run specific test
pytest --durations=0  # Run tests with times displayed
pytest --capture=tee-sys  #Run tests with logs
```
