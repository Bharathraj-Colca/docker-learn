from database import engine

def test_db_connection():

    connection = engine.connect()

    assert connection is not None

    connection.close()