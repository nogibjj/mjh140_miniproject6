"""
ETL-Query script
"""
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
from mylib.insert import insert
from mylib.update import update
from mylib.delete import delete

# Extract
print("Extracting data...")
extract(url="https://raw.githubusercontent.com/jfinocchiaro/marchmadness/master/kenpom.csv", 
        file_path = "kenpom.csv")

# Transform and load
print("Transforming data...")
load(dataset="kenpom.csv",
     database="kenpom.db",
     tab = "kenpom_data")

# Query
print("Querying data...")
query(dbname = "kenpom.db",
      tab = 'kenpom_data')

# Insert
new_data = {
    'Year':'2018', 
    'Rank': '1',
    'Team': 'Villinova',
    'Conf': 'BE',
    'Wins': '36',
    'Losses': '4'
    }
insert(dbname = "kenpom.db",
      tab = 'kenpom_data',
      new_data = new_data)

#Update
update(dbname = 'kenpom.db',
       tab = 'kenpom_data',
       col = 'Conference',
       n_val = 'BE',
       cond_col = 'Year',
       cond_val = '2018')

#Delete
delete(dbname = 'kenpom.db',
       tab = 'kenpom_data',
       cond_col = 'Year',
       cond_val = '2018')