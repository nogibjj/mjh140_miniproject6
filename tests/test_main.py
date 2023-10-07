"""
Unit Testing
"""

import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

from mylib.extract import extract
from mylib.query import query
from mylib.transform_load import load

class TestLib(unittest.TestCase):
    def test_correct_path(self):
        try:
            extract(url="https://raw.githubusercontent.com/jfinocchiaro/marchmadness/master/kenpom.csv", 
                    file_path = "kenpom.csv")
        except TypeError:
            self.fail("Path Failure")
    
    def test_query(self):
        try:
            query(dbname = "kenpom.db",
                  tab = 'kenpom_data')
        except TypeError:
            self.fail("Query Failure")
    
    def test_load(self):
        try:
            load(dataset="kenpom.csv",
                 database="kenpom.db",
                 tab = "kenpom_data")
        except TypeError:
            self.fail("Load Failure")

if __name__ == '__main__':
    unittest.main()
