import requests

BASE_URL = "http://127.0.0.1:8000"


def test_create_author():
    payload = {
        "name": "Bharath",
        "phone_no": 9876543210,
        "country": "India",
        "email": "bharath@test.com"
    }

    response = requests.post(f"{BASE_URL}/authors", json=payload)

    assert response.status_code == 200


def test_list_authors():
    response = requests.get(f"{BASE_URL}/authors")

    assert response.status_code == 200