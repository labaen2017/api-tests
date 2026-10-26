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

@pytest.mark.smoke
def test_get_user_has_email(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    assert response.json()["email"] == "Sincere@april.biz"

@pytest.mark.smoke
def test_get_all_posts_returns_100(base_url):
    response = requests.get(f"{base_url}/posts")
    assert response.status_code == 200
    posts = response.json()
    assert isinstance(posts, list)
    assert len(posts) == 100

def test_unknown_endpoint_returns_404(base_url):
    response = requests.get(f"{base_url}/banana")
    assert response.status_code == 404

@pytest.mark.smoke
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

@pytest.mark.smoke
def test_post_response_is_json(base_url):
    response = requests.get(f"{base_url}/posts/1", timeout=5)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]


def test_post_response_is_fast(base_url):
    response = requests.get(f"{base_url}/posts/1", timeout=5)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2


def test_post_fields_have_correct_types(base_url):
    response = requests.get(f"{base_url}/posts/1", timeout=5)
    assert response.status_code == 200
    
    post = response.json()
    assert isinstance(post["id"], int)
    assert isinstance(post["userId"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)

@pytest.mark.slow
def test_slow_server_times_out():
    with pytest.raises(requests.exceptions.ReadTimeout):
        requests.get("https://httpbin.org/delay/3", timeout=1)

