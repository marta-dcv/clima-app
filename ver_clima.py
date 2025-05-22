import duckdb

conn = duckdb.connect('clima.duckdb')
result = conn.execute("SELECT * FROM clima").fetchdf()
print(result)
