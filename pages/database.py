import sqlite3
conn=sqlite3.connect("Darabase.db")
query = '''
            CREATE TABLE SELL(
            CUSTOMER_NAME VARCHAR(100),
            ORDER_NAME VARCHAR(100),
            PRICE INT,
            ORDER_ID VARCHAR(100) PRIMARY KEY,
            DATE VARCHAR(50),
            TIME VARCHAR(50)
            )
                ORDER_NAME VARCHAR(200)
    '''
conn.execute(query)
conn.commit()
conn.close()
