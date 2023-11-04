from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_item(self):
        self.client.get("/item?id=1")
