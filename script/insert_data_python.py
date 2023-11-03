import os
import psycopg2
import datetime
from libs.random_names import random_names

INSERT_DATA_COUNT = 10

DB_CONFIG = {
    "dbname": os.environ.get("DB_NAME", "test_db"),
    "user": os.environ.get("DB_USER", "test_user"),
    "password": os.environ.get("DB_PASSWORD", "test_password"),
    "host": os.environ.get("DB_HOST", "localhost"),
}


class PostgresDatabaseManager:
    def __init__(self, config):
        self.config = config
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.config["dbname"],
                user=self.config["user"],
                password=self.config["password"],
                host=self.config["host"]
            )
            self.cur = self.conn.cursor()
            print("Connected to the database.")
        except Exception as e:
            print(f"An error occurred while connecting to the database: {e}")

    def close(self):
        if self.conn:
            self.cur.close()
            self.conn.close()
            print("Database connection closed.")

    def insert(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        try:
            self.cur.execute(query, values)
            self.conn.commit()
            print(f"Inserted data into {table=}, {data=}")
        except Exception as e:
            self.conn.rollback()
            print(f"An error occurred while inserting data: {e}")

def main():
    with PostgresDatabaseManager(DB_CONFIG) as db:
        # Insert data into the 'items' table
        for id in range(INSERT_DATA_COUNT):
            item_data = {'id': id,
                         'first_name': random_names.First(),
                         'last_name': random_names.Last(),
                         'country': random_names.Country()
                         }
            db.insert('items', item_data)


if __name__ == '__main__':
    print(f"Started at {datetime.datetime.now()}")
    main()
    print(f"Finished at {datetime.datetime.now()}")

