
import os
import pytest
from api_client import ApiClient

BASE_URL = os.environ.get("BASE_URL", "https://jsonplaceholder.typicode.com")

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def new_post():
    return {"title": "My first post", "body": "Hello API", "userId": 1}

@pytest.fixture
def updated_post():
    return {"title": "Updated title", "body": "Updated post body", "userId": 1}

@pytest.fixture
def api(base_url):
    return ApiClient(base_url)