import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

NEW_POST = {"title": "My first post", "body": "Hello API", "userId": 1}
UPDATED_POST = {"title": "Updated title", "body": "Updated post body", "userId": 1}

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

def test_filter_posts_by_user():
    response = requests.get(f"{BASE_URL}/posts", params={"userId": 1})
    assert response.status_code == 200      # ← first
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 10
    for post in posts:
        assert post["userId"] == 1

def test_filter_by_unknown_user_returns_empty_list():
    response = requests.get(f"{BASE_URL}/posts", params={"userId": 999})
    assert response.status_code == 200  
    assert response.json() == []  

def test_unknown_endpoint_returns_404():
    response = requests.get(f"{BASE_URL}/banana")
    assert response.status_code == 404

def test_create_post_returns_201():
    response = requests.post(f"{BASE_URL}/posts", json=NEW_POST)
    assert response.status_code == 201

def test_create_post_returns_sent_data_and_id():
    response = requests.post(f"{BASE_URL}/posts", json=NEW_POST)
    assert response.status_code == 201
    body = response.json()
    for key in NEW_POST:
        assert body[key] == NEW_POST[key]
    assert "id" in body

def test_update_post_returns_200_and_new_title():
    response = requests.put(f"{BASE_URL}/posts/1", json=UPDATED_POST)
    assert response.status_code == 200
    assert response.json()["title"] == UPDATED_POST["title"]

def test_delete_post_returns_200():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
