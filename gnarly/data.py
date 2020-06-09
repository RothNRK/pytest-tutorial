"""Class to handle reading source data."""
import logging

from pyspark.sql import DataFrame

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class DataHandler:
    """Handles reading source data."""

    def __init__(self):
        self._data = None
        self.tmp = 0

    @property
    def data(self) -> DataFrame:
        """Data used to create features."""
        if self._data is None:
            self._data = self._load_data()
        return self._data

    def _load_data(self):
        """Loads raw data."""
        raise SystemError("We can connect do external sources during tests")

    def save_data(self, folderpath: str):
        """Save data to folderpath.

        Args:
            folderpath
        """
        (
            self.data.write.format("parquet")
            .mode("overwrite")
            .options(compression="gzip")
            .save(path=folderpath)
        )


def load_raw_data():
    """Or if you just like functions."""
    raise SystemError("We can connect do external sources during tests")
