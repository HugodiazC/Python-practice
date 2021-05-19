import sqlite3
from sqlite import Error

def create_connection ( db_file ) :
    :param db_file: database file
    :return:
        conn = None
        try:
            conn = sqlite3 . connect ( db_file )
            return conn
        except Error as e :
            print ( e )
        return conn
def create_table ( conn , create_table_sql ) :
    :param conn: connection object
    :param create_table_sql:
    :return
    try:
        c = conn . cursor ()
        c . execute ( create_table_sql )
    except Error as e :
        print ( e )

def main () :
    database = r"pythonsqlite.db"
    sql_create_projects_table =
    sql_create_tasks_table =
conn = create_connection ( database )
if conn is not None
