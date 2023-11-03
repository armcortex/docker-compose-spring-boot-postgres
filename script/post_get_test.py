import unittest
import requests

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

post_data2 = [
    {"fname": "Alice", "lname": "Smith", "country": "Canada"},
    {"fname": "Bob", "lname": "Brown", "country": "Australia"},
    {"fname": "Charlie", "lname": "Davis", "country": "UK"},
    {"fname": "Diana", "lname": "Evans", "country": "USA"},
    {"fname": "Edward", "lname": "Fisher", "country": "New Zealand"},
]

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
    # print('Yoooo')