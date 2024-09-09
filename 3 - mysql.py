# Python 3.8.10

import MySQLdb
from datetime import datetime

def connect_to_db(name):
    return MySQLdb.connect(
        host="localhost",
        user="root",
        password="admin",
        database="challenge_meli"
    )

def create_tables(cursor):
    create_customers_statement ="""
    CREATE TABLE IF NOT EXISTS customers (
        id SMALLINT AUTO_INCREMENT PRIMARY KEY COMMENT 'Customer ID',
        first_name VARCHAR(64) COMMENT 'Customer first name',
        last_name VARCHAR(64) COMMENT 'Customer last name'
    )
    """

    create_campaigns_statement = """
    CREATE TABLE IF NOT EXISTS campaigns (
        id SMALLINT AUTO_INCREMENT PRIMARY KEY COMMENT 'Campaign ID',
        customer_id SMALLINT COMMENT 'Customer ID',
        name VARCHAR(64) COMMENT 'Campaign name',
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
    """
 
    create_events_statement = """
    CREATE TABLE IF NOT EXISTS events (
        dt VARCHAR(19) COMMENT 'Event timestamp',
        campaign_id SMALLINT COMMENT 'Campaign ID',
        status VARCHAR(64) COMMENT 'Event status',
        FOREIGN KEY (campaign_id) REFERENCES campaigns(id)
    )
    """

    cursor.execute(create_customers_statement)
    cursor.execute(create_campaigns_statement)
    cursor.execute(create_events_statement)

def add_content_to_tables(db, cursor):
    insert_customers_statement = """
    INSERT INTO customers (first_name, last_name)
    VALUES
        ('Whitney', 'Ferrero'),
        ('Dickie', 'Romera')
    """

    insert_campaigns_statement = """
    INSERT INTO campaigns (customer_id, name)
    VALUES
        (1, 'Upton Group'),
        (1, 'Roob, Hudson and Rippin'),
        (1, 'McCullough, Rempel and Larson'),
        (1, 'Lang and Sons'),
        (2, 'Ruecker, Hand and Haley')
    """

    insert_events_statement = f"""
    INSERT INTO events (dt, campaign_id, status)
    VALUES
        ('{datetime(2021, 12, 2, 13, 52, 0).strftime("%Y-%m-%d %H:%M:%S")}', 1, 'failure'),
        ('{datetime(2021, 12, 2, 8, 17, 48).strftime("%Y-%m-%d %H:%M:%S")}', 2, 'failure'),
        ('{datetime(2021, 12, 2, 8, 18, 17).strftime("%Y-%m-%d %H:%M:%S")}', 2, 'failure'),
        ('{datetime(2021, 12, 1, 11, 55, 32).strftime("%Y-%m-%d %H:%M:%S")}', 3, 'failure'),
        ('{datetime(2021, 12, 1, 6, 53, 16).strftime("%Y-%m-%d %H:%M:%S")}', 4, 'failure'),
        ('{datetime(2021, 12, 2, 4, 51, 9).strftime("%Y-%m-%d %H:%M:%S")}', 4, 'failure'),
        ('{datetime(2021, 12, 1, 6, 34, 4).strftime("%Y-%m-%d %H:%M:%S")}', 5, 'failure'),
        ('{datetime(2021, 12, 2, 3, 21, 18).strftime("%Y-%m-%d %H:%M:%S")}', 5, 'failure'),
        ('{datetime(2021, 12, 1, 3, 18, 24).strftime("%Y-%m-%d %H:%M:%S")}', 5, 'failure'),
        ('{datetime(2021, 12, 2, 15, 32, 37).strftime("%Y-%m-%d %H:%M:%S")}', 1, 'success'),
        ('{datetime(2021, 12, 1, 4, 23, 20).strftime("%Y-%m-%d %H:%M:%S")}', 1, 'success'),
        ('{datetime(2021, 12, 2, 6, 53, 24).strftime("%Y-%m-%d %H:%M:%S")}', 1, 'success'),
        ('{datetime(2021, 12, 2, 8, 1, 2).strftime("%Y-%m-%d %H:%M:%S")}', 2, 'success'),
        ('{datetime(2021, 12, 1, 15, 57, 19).strftime("%Y-%m-%d %H:%M:%S")}', 2, 'success'),
        ('{datetime(2021, 12, 2, 16, 14, 34).strftime("%Y-%m-%d %H:%M:%S")}', 3, 'success'),
        ('{datetime(2021, 12, 2, 21, 56, 38).strftime("%Y-%m-%d %H:%M:%S")}', 3, 'success'),
        ('{datetime(2021, 12, 1, 5, 54, 43).strftime("%Y-%m-%d %H:%M:%S")}', 4, 'success'),
        ('{datetime(2021, 12, 2, 17, 56, 45).strftime("%Y-%m-%d %H:%M:%S")}', 4, 'success'),
        ('{datetime(2021, 12, 2, 11, 56, 50).strftime("%Y-%m-%d %H:%M:%S")}', 4, 'success'),
        ('{datetime(2021, 12, 2, 6, 8, 20).strftime("%Y-%m-%d %H:%M:%S")}', 5, 'success')
    """

    cursor.execute(insert_customers_statement)
    db.commit()
    cursor.execute(insert_campaigns_statement)
    db.commit()
    cursor.execute(insert_events_statement)
    db.commit()

def main():
    db = connect_to_db('challenge_meli')
  
    cursor = db.cursor()
    create_tables(cursor)
    # add_content_to_tables(db, cursor)

    customers_with_more_than_3_failure_events_query = """
    SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer, COUNT(*) AS failures
    FROM customers c
    JOIN campaigns ca ON c.id = ca.customer_id
    JOIN events e ON ca.id = e.campaign_id
    WHERE e.status = 'failure'
    GROUP BY c.id
    HAVING COUNT(*) > 3;
    """

    cursor.execute(customers_with_more_than_3_failure_events_query)
    customers = cursor.fetchall()

    headers = [header[0] for header in cursor.description]

    print(f"{headers[0]:^20} | {headers[1]:^10}")
    print("-" * 35)
    for customer in customers:
        print(f"{customer[0]:^20} | {customer[1]:^10}")

    cursor.close()
    db.close()

main()
