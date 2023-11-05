import os
import psycopg2
import datetime
import time
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from dataclasses import dataclass, asdict

from libs.random_names import random_names


INSERT_DATA_COUNT = 10000

DEBUG_VERBOSE = False

DB_CONFIG = {
    'dbname': os.environ.get('DB_NAME', 'test_db'),
    'user': os.environ.get('DB_USER', 'test_user'),
    'password': os.environ.get('DB_PASSWORD', 'test_password'),
    'host': os.environ.get('DB_HOST', 'localhost'),
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
                dbname=self.config['dbname'],
                user=self.config['user'],
                password=self.config['password'],
                host=self.config['host']
            )
            self.cur = self.conn.cursor()
            if DEBUG_VERBOSE:
                print('Connected to the database.')
        except Exception as e:
            print(f'An error occurred while connecting to the database: {e}')

    def close(self):
        if self.conn:
            self.cur.close()
            self.conn.close()
            if DEBUG_VERBOSE:
                print('Database connection closed.')

    def insert(self, table, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        values = tuple(data.values())

        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        try:
            self.cur.execute(query, values)
            self.conn.commit()
            if DEBUG_VERBOSE:
                print(f'Inserted data into {table=}, {data=}')
        except Exception as e:
            self.conn.rollback()
            print(f'An error occurred while inserting data: {e}')


@dataclass
class ItemData:
    first_name: str
    last_name: str
    country: str


def insert_data(item_id=0):
    with PostgresDatabaseManager(DB_CONFIG) as db:
        # Insert data into the 'items' table
        item_data = ItemData(
            first_name=random_names.First(),
            last_name=random_names.Last(),
            country=random_names.Country()
        )
        db.insert('items', asdict(item_data))


def single_processing():
    for _ in tqdm(range(INSERT_DATA_COUNT), desc='Inserting data'):
        insert_data()


def multi_processing():
    # Get CPU cores
    process_count = min(cpu_count(), INSERT_DATA_COUNT)

    # Create a pool of processes
    with Pool(process_count) as pool:
        for _ in tqdm(pool.imap_unordered(insert_data, range(INSERT_DATA_COUNT)),
                      total=INSERT_DATA_COUNT,
                      desc='Inserting data'):
            pass


def main():
    # single_processing()
    multi_processing()


if __name__ == '__main__':
    print(f'Started at {datetime.datetime.now()}')
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f'Function executed in {end_time - start_time:.2f} seconds')
    print(f'Finished at {datetime.datetime.now()}')
