import requests


class ApiClient:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, path):
        return requests.get(f"{self.base_url}{path}", timeout=self.timeout)

    def get_post(self, post_id):
        return requests.get(f"{self.base_url}/posts/{post_id}", timeout=self.timeout)

    def get_posts(self, params=None):
        return requests.get(f"{self.base_url}/posts", params=params, timeout=self.timeout)

    def get_user(self, user_id):
        return requests.get(f"{self.base_url}/users/{user_id}", timeout=self.timeout)

    def create_post(self, data):
        return requests.post(f"{self.base_url}/posts", json=data, timeout=self.timeout)

    def update_post(self, post_id, data):
        return requests.put(f"{self.base_url}/posts/{post_id}", json=data, timeout=self.timeout)

    def delete_post(self, post_id):
        return requests.delete(f"{self.base_url}/posts/{post_id}", timeout=self.timeout)