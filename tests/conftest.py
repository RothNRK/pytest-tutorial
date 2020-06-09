import shutil
import logging

import pytest
from pyspark.sql import functions as F

from gnarly.data import DataHandler
from gnarly.model import Model
from tests.mock_data import SCHEMA, RAW_DATA

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


@pytest.fixture
def foo_fixture(spark_session):
    """Fixture to see if your spark is running correctly."""
    return spark_session.createDataFrame([{'name': 'Alice', 'age': 1}])


@pytest.fixture
def mock_data(spark_session):
    """Mock data."""
    pass


@pytest.fixture(scope="function")
def mock_DataHandler(monkeypatch, mock_data):
    """A DataHandler with mocked data."""
    pass


@pytest.fixture
def mock_path(tmp_path):
    """Provide a directory path and delete when the test is done."""
    pass


@pytest.fixture
def mock_Model(mock_DataHandler):
    """Model class with mocked Model.data_handler."""
    pass


@pytest.fixture
def assert_df_equal():
    """Assert two DataFrames are equal. Example of a factory."""
    def _assert_df_equal(df_1, df_2):
        df_1 = df_1.select(F.hash(*df_1.columns).alias("hash")).orderBy("hash")
        df_2 = df_2.select(F.hash(*df_2.columns).alias("hash")).orderBy("hash")
        assert df_1.subtract(df_2).count() == 0

    return _assert_df_equal


@pytest.fixture(scope="module")
def monkeypatch_module():
    """Custom monkeypatch for module scope."""
    from _pytest.monkeypatch import MonkeyPatch

    m = MonkeyPatch()
    yield m
    m.undo()
