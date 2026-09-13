import sqlite3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import DB_PATH

class DatabaseHandler:
    def __init__(self, db_path:str=DB_PATH):
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")

        if os.path.exists(schema_path):
            with open (schema_path, "r") as schema_file:
                sql_script = schema_file.read()

            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.executescript(sql_script)
                conn.commit()
            print("Database initiated successfully with schema.sql")

        else:
            print(f"Warning : Schema file not found at {schema_path}")

    def execute_query(self, query : str, params : tuple = ())-> int:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor.lastrowid  # type: ignore

    def fetch_all(self, query:str, params:tuple = ())->list[tuple] | None:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def fetch_one(self, query:str, params:tuple = ()) -> tuple | None:
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
