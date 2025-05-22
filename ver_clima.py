import duckdb
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'clima.duckdb')

conn = duckdb.connect(DB_PATH)
result = conn.execute("SELECT * FROM clima").fetchdf()
print(result)
