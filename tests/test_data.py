"""Test DataHandler class."""
import logging
from pathlib import Path
import shutil

import pytest

from gnarly import data
from gnarly.data import DataHandler

from tests.utils import load_mock_data_func

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

"""
Automatically finds:
Files: test_*.py, *_test.py
Classes: Test*
Tests: test_*
"""


class TestDataHandler:
    """Test DataHandler"""

    def test_local_installation_working(self, foo_fixture):
        """Test to make sure your env is working correctly."""
        assert foo_fixture.count() > 0
        LOGGER.info("Logging msg won't display")

    def _data_monkeypatch(self, monkeypatch):
        """Mocking with simple monkeypatch.
            - Mock DataHandler._load_data
        """
        pass

    def _data_extra_work(self, monkeypatch, mock_data):
        """Mocking DataHandler with mock_data fixture.
            - Make mock_data fixture.
            - def _mock_data
            - Patch DataHandler._load_data
        """
        pass

    def _data_clean(self, mock_DataHandler):
        """Data with mock_DataHandler fixture.
            - Import single mock_DataHandler for any test using a DataHandler.
        """
        pass

    def _save_data_long_way(self, mock_DataHandler):
        """Save data and remove using the long way.
            - Make temp data folder
            - Call DataHandler.save_data
            - Remove temp data folder
        """
        pass

    def _save_data(self, mock_path, mock_DataHandler):
        """Save data with tmp_path setup/teardown.
            - Call DataHandler.save_data
        """
        pass


class TestDataFunc:
    def _load_raw_data(self, monkeypatch, mock_data):
        """Mock data for load_raw_data."""
        pass
