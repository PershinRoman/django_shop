import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USER"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT", "5432"),
    )
    print("Успешное подключение к PostgreSQL!")
    conn.close()
except psycopg2.OperationalError as e:
    print("Ошибка подключения:")
    print(e)
except Exception as e:
    print("Другая ошибка:")
    print(e)
