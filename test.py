import requests

BASE_URL = "http://127.0.0.1:8000"

#create author
def test_create_author():
    url = f"{BASE_URL}/authors"

    payload = {
        "name": "Bharath",
        "phone_no": 9876543210,
        "country": "India",
        "email": "bharath@test.com"
    }

    response = requests.post(url, json=payload)
    print("Create Author Response:")
    print(response.json())
    print("-" * 50)


#create books
def test_create_book(author_id):
    url = f"{BASE_URL}/books"

    payload = {
        "author_id": author_id,
        "book_name": "FastAPI Mastery",
        "price": 499.0
    }

    response = requests.post(url, json=payload)
    print("Create Book Response:")
    print(response.json())
    print("-" * 50)


#list authors
def test_list_authors():
    url = f"{BASE_URL}/authors"

    response = requests.get(url)
    print("Authors List:")
    print(response.json())
    print("-" * 50)


#list author books
def test_author_books(author_id):
    url = f"{BASE_URL}/authors/{author_id}/books"

    response = requests.get(url)
    print("Author Books:")
    print(response.json())
    print("-" * 50)
    
if __name__ == "__main__":
    # Step 1: Create Author
    test_create_author()

    
    author_id = 5

    # Step 2: Create Book
    test_create_book(author_id)

    # Step 3: List Authors
    test_list_authors()

    # Step 4: Get Author Books
    test_author_books(author_id)
   