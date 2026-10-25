import requests

from test_posts import BASE_URL

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("status code:", response.status_code)
print("body:", response.json())

body = response.json()
print(body["title"])

response3 = requests.get("https://jsonplaceholder.typicode.com/posts/9999")
print("Task 3 status:", response3.status_code)
print("Task 3 body:", response3.json())

response4 = requests.get("https://jsonplaceholder.typicode.com/users/1")
print("Email:", response4.json()["email"] )

response5 = requests.get("https://jsonplaceholder.typicode.com/posts")
print("Type", type(response5.json()))
print("Total:", len(response5.json()))


response = requests.get(f"{BASE_URL}/posts", params={"userId": 1})
print(response.url)            # see the URL that requests built!
print(response.status_code)
posts = response.json()
print(len(posts))

response = requests.get(f"{BASE_URL}/posts", params={"userId": 999})
print(response.url)            # see the URL that requests built!
print(response.status_code)
posts = response.json()
print(len(posts))

new_post = {"title": "My first post", "body": "Hello API", "userId": 1}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
print(response.status_code)
print(response.json())


# PUT: replace post 1
updated_post = {"id": 1, "title": "Updated title", "body": "New body", "userId": 1}
response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
print("PUT status:", response.status_code)
print("PUT body:", response.json())

# DELETE: delete post 1
response = requests.delete(f"{BASE_URL}/posts/1")
print("DELETE status:", response.status_code)
print("DELETE body:", response.json())