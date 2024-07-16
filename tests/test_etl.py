import unittest
import pandas as pd
from src.etl import AirbnbETLFlow

class TestAirbnbETL(unittest.TestCase):
    def setUp(self):
        self.flow = AirbnbETLFlow()

    def test_load_data(self):
        self.flow.load_data()
        self.assertIsInstance(self.flow.df, pd.DataFrame)
        self.assertGreater(len(self.flow.df), 0)

    def test_transform_data(self):
        self.flow.load_data()
        self.flow.transform_data()
        self.assertIn('date', self.flow.df.columns)
        self.assertIn('time', self.flow.df.columns)
        self.assertIn('price_per_person', self.flow.df.columns)
        self.assertIn('is_expensive', self.flow.df.columns)

if __name__ == '__main__':
    unittest.main()
