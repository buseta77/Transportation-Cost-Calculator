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
                CREATE TABLE IF NOT EXISTS supplies (
                    id SERIAL PRIMARY KEY,
                    supply_name VARCHAR(255) NOT NULL,
                    supplier VARCHAR(255),
                    order_price FLOAT NOT NULL,
                    resell_price FLOAT NOT NULL
                );
            """)
            conn.commit()
            print("Table 'supplies' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()

def insert_data_from_json(conn, json_data):
    """Insert data from JSON into the 'supplies' table."""
    try:
        with conn.cursor() as cursor:
            for item in json_data:
                supply_name = item['supply_name']
                supplier = item['supplier']
                order_price = item['order_price']
                resell_price = item['resell_price']
                cursor.execute("""
                    INSERT INTO supplies (supply_name, supplier, order_price, resell_price)
                    VALUES (%s, %s, %s, %s)
                """, (supply_name, supplier, order_price, resell_price))
            conn.commit()
            print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

def main():
    db_url = "URL_OF_DB"

    json_file = 'supplies.json'
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
