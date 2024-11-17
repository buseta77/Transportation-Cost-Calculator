import psycopg2
from psycopg2 import sql

DATABASE_URL = "URL_OF_DB"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connection successful")
    cursor = conn.cursor()

    # Query to list all tables in the public schema
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)

    # Fetch and display all table names
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])

    cursor.close()
    conn.close()

except Exception as e:
    print(f"Error: {e}")
