import requests
import pytest

@pytest.mark.parametrize("user_id, expected_count",[
    (1, 10),
    (2, 10),
    (999, 0),
])
def test_posts_per_user(base_url, user_id, expected_count):
    response = requests.get(f"{base_url}/posts", params={"userId": user_id})
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == expected_count
    for post in posts:
        assert post["userId"] == user_id

def test_get_user_has_email(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    assert response.json()["email"] == "Sincere@april.biz"

def test_get_all_posts_returns_100(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100

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

@pytest.mark.parametrize("post_id",[
    (1),
    (50),
    (100),
])
def test_get_existing_posts_return_200(base_url,post_id):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id


@pytest.mark.parametrize("npost_id",[
    (0),
    (-1),
    (101),
    (9999),
])
def test_get_non_existing_post_returns_404(base_url,npost_id):
    response = requests.get(f"{base_url}/posts/{npost_id}")
    assert response.status_code == 404