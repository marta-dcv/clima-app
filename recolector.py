import time
import datetime
import requests
import duckdb
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

API_KEY = os.getenv("API_KEY")
CIUDAD = os.getenv("CIUDAD", "Vigo")
UNIDADES = os.getenv("UNIDADES", "metric")

# Obtener ruta absoluta del archivo actual
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'clima.duckdb')

# Conectar a archivo DuckDB local con ruta absoluta
conn = duckdb.connect(DB_PATH)

# Crear tabla si no existe
conn.execute("""
CREATE TABLE IF NOT EXISTS clima (
    fecha TIMESTAMP,
    temperatura DOUBLE,
    humedad INTEGER,
    presion INTEGER
)
""")

# Consultar API
print(f"Consultando clima en {CIUDAD} - {datetime.datetime.now()}")
url = f"https://api.openweathermap.org/data/2.5/weather?q={CIUDAD}&units={UNIDADES}&appid={API_KEY}"
respuesta = requests.get(url)
datos = respuesta.json()

if respuesta.status_code == 200:
    temperatura = datos['main']['temp']
    humedad = datos['main']['humidity']
    presion = datos['main']['pressure']
    fecha_hora = datetime.datetime.now()

    conn.execute("INSERT INTO clima VALUES (?, ?, ?, ?)", (fecha_hora, temperatura, humedad, presion))
    print(f"✅ Datos guardados: {fecha_hora} | {temperatura}°C | {humedad}% humedad | {presion} hPa")
else:
    print(f"❌ Error al consultar API: {datos.get('message')}")
