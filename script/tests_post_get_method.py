import os
import unittest
import requests
import psycopg2
import datetime
import time

BASE_URL = "http://app:8080/item"

headers = {
    "Content-Type": "application/json"
}

# Test data
post_data = [
    {"fname": "Alice", "lname": "Smith", "country": "Canada"},
    {"fname": "Bob", "lname": "Brown", "country": "Australia"},
    {"fname": "Charlie", "lname": "Davis", "country": "UK"},
    {"fname": "Diana", "lname": "Evans", "country": "USA"},
    {"fname": "Edward", "lname": "Fisher", "country": "New Zealand"},
]

DB_CONFIG = {
    "dbname": os.environ.get("DB_NAME", "test_db"),
    "user": os.environ.get("DB_USER", "test_user"),
    "password": os.environ.get("DB_PASSWORD", "test_password"),
    "host": os.environ.get("DB_HOST", "localhost"),
}

def drop_table_if_exists(cursor, table_name):
    cursor.execute(f"""
        TRUNCATE TABLE {table_name};
    """)

def check_table_exist(cursor, table_name):
    cursor.execute(f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_schema = 'public'
            AND table_name = '{table_name}'
        );
    """)
    return cursor.fetchone()[0]


def deep_compare(d1, d2):
    if isinstance(d1, dict) and isinstance(d2, dict):
        if d1.keys() != d2.keys():
            return False
        for key in d1:
            if not deep_compare(d1[key], d2[key]):
                return False
        return True
    elif isinstance(d1, list) and isinstance(d2, list):
        return all(deep_compare(a, b) for a, b in zip(d1, d2))
    else:
        return d1 == d2

class TestItemAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(f"Tests started at {datetime.datetime.now()}")
        cls.connection = psycopg2.connect(**DB_CONFIG)
        cls.connection.autocommit = True
        table_name = os.environ.get("DB_TABLE", "test_table")
        with cls.connection.cursor() as cursor:
            print(f"Wait for table: {table_name} ready, it will take 1 minute to finish")
            while True:
                if check_table_exist(cursor, table_name):
                    break
                else:
                    print(".", end="", flush=True)
                    time.sleep(1)

            print(f"\n Table: {table_name} is ready")
            drop_table_if_exists(cursor, table_name)

    @classmethod
    def tearDownClass(cls):
        print(f"Tests finished at {datetime.datetime.now()}")
        cls.connection.close()

    def test_post_and_get(self):
        # Perform POST requests and verify response
        for data in post_data:
            # Post Method
            post_response = requests.post(BASE_URL, headers=headers, json=data)
            self.assertEqual(post_response.status_code, 200)
            response_json = post_response.json()
            self.assertIsNotNone(response_json['id'])

            # Get Method
            item_id = response_json['id']
            get_response = requests.get(f"{BASE_URL}?id={item_id}")
            self.assertEqual(get_response.status_code, 200)


            # Verify GET data == POST data using deep_compare()
            data['id'] = item_id
            get_response_json = get_response.json()
            self.assertTrue(deep_compare(get_response_json, data),
                            f"GET response data does not match POST data. POST data: {data}, GET response: {get_response_json}")

            # Verify if can failed
            data['lname'] = 'ccc'
            self.assertFalse(deep_compare(get_response_json, data),
                            f"This should be different. POST data: {data}, GET response: {get_response_json}")


if __name__ == '__main__':
    unittest.main()
