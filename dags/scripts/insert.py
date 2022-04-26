from datetime import datetime
import psycopg2
import requests
from config import config
from create_table import create_tables


def check_table():
    """Insert statement"""
    commands = "SELECT COUNT(*) = 1 FROM pg_tables WHERE tablename = 'currency';"
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands)
        exists = cur.fetchone()[0]
        if exists is False:
            create_tables()
            print('Table currency created')
        else:
            print('Table currency exists')
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def fetch_data(base, target, fetch_url, param):
    response = requests.get(fetch_url, params=param)
    data = response.json()

    if data['success']:
        rate_dict = data['rates']
        rate = rate_dict[target_currency]
        rate_date = data['date']
        etl_modified_date = datetime.now()
        result_query = (base, target, rate, rate_date, etl_modified_date)

    return result_query


def insert(insert_values):
    """Insert statement"""
    commands = "INSERT INTO currency (base_currency, target_currency, rate, rate_date, etl_modified_date) " \
               "VALUES (%s, %s, %s, %s, %s);"
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands, insert_values)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('Data inserted as of', insert_values[4])
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    base_currency = 'BTC'
    target_currency = 'USD'
    url = 'https://api.exchangerate.host/latest'
    query = {'base': base_currency, 'symbols': target_currency}
    check_table()
    insert(fetch_data(base_currency, target_currency, url, query))
