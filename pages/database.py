import streamlit as st
import sqlite3
conn=sqlite3.connect("Darabase.db")
data=conn.execute("SELECT * FROM SIGNIN")
st.title('Harsh')
for n in data:
    st.write(n)
conn.close()
