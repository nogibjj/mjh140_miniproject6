"""
Extract a dataset. Preferably a csv file.
"""
import requests

def extract(url: str, file_path: str):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



