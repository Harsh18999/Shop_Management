import sqlite3
conn=sqlite3.connect("Darabase.db")
query = '''
            ALTER TABLE SELL ADD COLUMN
                ORDER_NAME VARCHAR(200)
    '''
conn.execute(query)
conn.commit()
conn.close()