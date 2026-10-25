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