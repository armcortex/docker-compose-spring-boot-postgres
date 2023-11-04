import random
from locust import HttpUser, task, between

DATA_COUNT = 10000


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_item(self):
        item_id = random.randint(1, DATA_COUNT)
        self.client.get(f'/item?id={item_id}')

