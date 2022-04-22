import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = """CREATE TABLE currency (
                base_currency TEXT NOT NULL,
                target_currency TEXT NOT NULL,
                rate NUMERIC,
                rate_date DATE, 
                etl_modified_date TIMESTAMP,
                PRIMARY KEY (rate_date, etl_modified_date))"""
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()