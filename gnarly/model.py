"""Simple Model class to orchastrate model steps."""
from pyspark.sql import functions as F

from gnarly.data import DataHandler

class Model:
    """Model for gnarly predictions."""

    def __init__(self):
        self.data_handler = DataHandler()

    @property
    def data(self):
        """Returns raw data."""
        return self.data_handler.data
