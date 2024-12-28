import mysql.connector
from mysql.connector import Error  # Correcting the import for mysql.connector
import os

def create_database():
    connection = None
    try:
        # Get database credentials from environment variables
        db_host = os.environ.get('MYSQL_HOST', 'localhost')
        db_user = os.environ.get('MYSQL_USER', 'root')
        db_password = os.environ.get('MYSQL_PASSWORD')

        if not db_password:
            raise ValueError("Database password not set in environment variables")

        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL server: {e}")
    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if connection:
            try:
                # Close cursor and connection
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
            except Error as e:
                print(f"Error closing MySQL connection: {e}")

if __name__ == "__main__":
    create_database()
