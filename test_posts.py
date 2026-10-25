import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post_returns_200():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_post_has_correct_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.json()["id"] == 1

def test_get_missing_post_returns_404():
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404

def test_get_user_has_email():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.json()["email"] == "Sincere@april.biz"

def test_get_all_posts_returns_100():
    response = requests.get(f"{BASE_URL}/posts")
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100