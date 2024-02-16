import sqlite3
import streamlit as st
conn=sqlite3.connect("Darabase.db")
query = '''
            SELECT * FROM SELL
    '''
data=conn.execute(query)
for n in data:
    st.write(n)
conn.commit()
conn.close()
