import psycopg2
from config import host, user, password, db_name

try:
    # connect to exist database
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )

    # the cursor for performing database operations
    # cursor = connection.cursor()

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")

except Exception as _ex:
    print("Error connecting when working with PostgreSQL", _ex)
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("PostgreSQL connectioin closed")