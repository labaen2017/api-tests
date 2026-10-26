import requests

def test_get_post_has_correct_id(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.json()["id"] == 1

def test_get_missing_post_returns_404(base_url):
    response = requests.get(f"{base_url}/posts/9999")
    assert response.status_code == 404

def test_get_user_has_email(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.json()["email"] == "Sincere@april.biz"

def test_get_all_posts_returns_100(base_url):
    response = requests.get(f"{base_url}/posts")
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100

def test_filter_posts_by_user(base_url):
    response = requests.get(f"{base_url}/posts", params={"userId": 1})
    assert response.status_code == 200      # ← first
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 10
    for post in posts:
        assert post["userId"] == 1

def test_filter_by_unknown_user_returns_empty_list(base_url):
    response = requests.get(f"{base_url}/posts", params={"userId": 999})
    assert response.status_code == 200  
    assert response.json() == []  

def test_unknown_endpoint_returns_404(base_url):
    response = requests.get(f"{base_url}/banana")
    assert response.status_code == 404

def test_create_post_returns_sent_data_and_id(base_url, new_post):
    response = requests.post(f"{base_url}/posts", json=new_post)
    assert response.status_code == 201
    body = response.json()
    for key in new_post:
        assert body[key] == new_post[key]
    assert "id" in body

def test_update_post_returns_200_and_new_title(base_url, updated_post):
    response = requests.put(f"{base_url}/posts/1", json=updated_post)
    assert response.status_code == 200
    assert response.json()["title"] == updated_post["title"]

def test_delete_post_returns_200(base_url):
    response = requests.delete(f"{base_url}/posts/1")
    assert response.status_code == 200

def test_get_post_returns_200(base_url):
    response = requests.get(f"{base_url}/posts/1")
    assert response.status_code == 200

def test_create_post_returns_201(base_url, new_post):
    response = requests.post(f"{base_url}/posts", json=new_post)
    assert response.status_code == 201

