import sys
import mysql.connector

class CursorMySql:
    
    DB_USER = "XXXX"
    DB_USER_PASSWD = "XXXX"
    DB_HOST = "XXXXXXX.rds.amazonaws.com"
    DB_PORT = 3306
    DB_SCHEMA = "fap_clinica"


    def create_connection(self):
        try:
            conn = mysql.connector.connect(
                user = self.DB_USER,
                password = self.DB_USER_PASSWD,
                host = self.DB_HOST,
                port = self.DB_PORT,
                database = self.DB_SCHEMA
            )
            print("Connected to MySql Platform!")
        except mysql.connector.Error as e:
            print(f"Error connecting to MySql Platform: {e}")
            sys.exit(1)

        cur = conn.cursor()
        return conn, cur
