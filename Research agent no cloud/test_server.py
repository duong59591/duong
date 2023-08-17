import requests

print(
    requests.post(
            "http://127.0.0.1:10001",
            json={
                    "query": "what is meta's new product Threads?"
            }
    ).json()
)