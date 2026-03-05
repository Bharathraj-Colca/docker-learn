from sqlalchemy import text
from database import engine

create_authors_table = text("""
CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone_no VARCHAR(20),
    country VARCHAR(100),
    email VARCHAR(100)
);
""")

create_books_table = text("""
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    author_id INTEGER REFERENCES authors(id) ON DELETE CASCADE,
    book_name VARCHAR(200),
    price NUMERIC
);
""")

try:
    with engine.connect() as connection:
        connection.execute(create_authors_table)
        connection.execute(create_books_table)
        connection.commit()
        print("Tables created successfully!")

except Exception as e:
    print("Error creating tables:", e)