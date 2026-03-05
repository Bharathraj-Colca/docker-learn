from fastapi import FastAPI
from sqlalchemy import text
from database import engine
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

class Authorsrequest(BaseModel):
    name : str
    phone_no : int
    country : str
    email : str

class Bookrequest(BaseModel):
    author_id : int
    book_name : str
    price : float
    
class Authorresponse(BaseModel):
    message : str

@app.post("/authors" , response_model = Authorresponse)
def create_author(data: Authorsrequest):

    insert_query = text ("""
        INSERT INTO authors (name, phone_no, country, email)
        VALUES (:name, :phone_no, :country, :email)
    """)

    try:
        with engine.begin() as connection:
            connection.execute(insert_query,{
                "name": data.name,
                "phone_no": data.phone_no,
                "country": data.country,
                "email": data.email 
            })

        
        return {"message": "Author created successfully"}
    
    except Exception as e:
       return {"error":str(e)} 
   
   
@app.post("/books")
def create_books(data : Bookrequest):
    
    insert_query = text("""
    INSERT INTO books (author_id, book_name, price)
    VALUES (:author_id, :book_name, :price)
""")
    
    try:
        with engine.begin() as connection :
            connection.execute(insert_query, {
            "author_id": data.author_id,
            "book_name": data.book_name,
            "price": data.price
})
        
        
        return {"message": "Book added successfully"}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/authors")
def list_authors():
    
    fetch_query = text("""
        SELECT * FROM authors"""
        )
    
    try:
        with engine.connect() as connection:
            result = connection.execute(fetch_query)
            rows = result.fetchall()

            return [dict(row._mapping) for row in rows]

    except Exception as e:
        return {"error": str(e)} 
                                         
@app.get("/authors/{author_id}/books")
def get_author_books(author_id: int):

   #check author
    check_author_query = text("""
        SELECT id, name
        FROM authors
        WHERE id = :author_id
    """)

    # check books
    fetch_books_query = text("""
        SELECT id, book_name, price
        FROM books
        WHERE author_id = :author_id
    """)

    try:
        with engine.connect() as connection:

            
            author_result = connection.execute(
                check_author_query,
                {"author_id": author_id}
            )
            author = author_result.fetchone()

            if author is None:
                raise HTTPException(
                    status_code=404,
                    detail="Author not found"
                )

            
            books_result = connection.execute(
                fetch_books_query,
                {"author_id": author_id}
            )
            books = books_result.fetchall()

            return {
                "author_id": author.id,
                "author_name": author.name,
                "books": [dict(row._mapping) for row in books]
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    
    
