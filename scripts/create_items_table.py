import psycopg2
import json
import os

def connect_to_db(url):
    """Connect to the PostgreSQL database."""
    try:
        # Establish the connection
        conn = psycopg2.connect(url)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    """Create the 'items' table."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id SERIAL PRIMARY KEY,
                    item_name VARCHAR(255) NOT NULL,
                    hidden_value INTEGER NOT NULL,
                    item_tab TEXT NOT NULL
                );
            """)
            conn.commit()
            print("Table 'items' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()

def insert_data_from_json(conn, json_data):
    """Insert data from JSON into the 'items' table."""
    try:
        with conn.cursor() as cursor:
            for item in json_data:
                item_name = item['item_name']
                hidden_value = item['hidden_value']
                item_tab = item['item_tab']
                cursor.execute("""
                    INSERT INTO items (item_name, hidden_value, item_tab)
                    VALUES (%s, %s, %s)
                """, (item_name, hidden_value, item_tab))
            conn.commit()
            print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

def main():
    db_url = "URL_OF_DB"

    json_file = 'items.json'
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found.")
        return

    with open(json_file, 'r') as file:
        data = json.load(file)

    conn = connect_to_db(db_url)
    if conn:
        create_table(conn)
        insert_data_from_json(conn, data)
        conn.close()

if __name__ == "__main__":
    main()
