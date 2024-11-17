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
                CREATE TABLE IF NOT EXISTS rooms (
                    id SERIAL PRIMARY KEY,
                    room_name VARCHAR(255) NOT NULL,
                    small_box_quantity FLOAT NOT NULL,
                    medium_box_quantity FLOAT NOT NULL,
                    large_box_quantity FLOAT NOT NULL,
                    paper_roll_quantity FLOAT NOT NULL,
                    tape_roll_quantity FLOAT NOT NULL,
                    labor_hours FLOAT NOT NULL
                );
            """)
            conn.commit()
            print("Table 'rooms' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()

def insert_data_from_json(conn, json_data):
    """Insert data from JSON into the 'rooms' table."""
    try:
        with conn.cursor() as cursor:
            for item in json_data:
                room_name = item['room_name']
                small_box_quantity = item['small_box_quantity']
                medium_box_quantity = item['medium_box_quantity']
                large_box_quantity = item['large_box_quantity']
                paper_roll_quantity = item['paper_roll_quantity']
                tape_roll_quantity = item['tape_roll_quantity']
                labor_hours = item['labor_hours']
                cursor.execute("""
                    INSERT INTO rooms (
                        room_name, small_box_quantity, medium_box_quantity, large_box_quantity,
                        paper_roll_quantity, tape_roll_quantity, labor_hours)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                   (room_name, small_box_quantity, medium_box_quantity,
                    large_box_quantity, paper_roll_quantity, tape_roll_quantity, labor_hours)
                )
            conn.commit()
            print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

def main():
    db_url = "URL_OF_DB"

    json_file = 'rooms.json'
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
