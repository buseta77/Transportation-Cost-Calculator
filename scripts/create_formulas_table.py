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
    """Create the 'formulas' table."""
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS formulas (
                    id SERIAL PRIMARY KEY,
                    formula_name VARCHAR(255) NOT NULL,
                    formula_numbers TEXT NOT NULL
                );
            """)
            conn.commit()
            print("Table 'formulas' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()

def insert_data_from_json(conn, json_data):
    """Insert data from JSON into the 'formulas' table."""
    try:
        with conn.cursor() as cursor:
            for item in json_data:
                formula_name = item['formula_name']
                formula_numbers = item['formula_numbers']
                cursor.execute("""
                    INSERT INTO formulas (formula_name, formula_numbers)
                    VALUES (%s, %s)
                """, (formula_name, formula_numbers))
            conn.commit()
            print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

def main():
    db_url = "URL_OF_DB"

    json_file = 'formulas.json'
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
