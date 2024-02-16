import streamlit as st
import sqlite3
conn=sqlite3.connect("Darabase.db")
ins='''
       CREATE TABLE IF NOT EXISTS SIGNIN(
       NAME VARCHAR(70)'
       EMAIL VARCHAR(70) PRIMARY KEY,
       PASSWORD VARCHAR(70}
       )
'''
data=conn.execute(ins)
st.title('Harsh')
for n in data:
    st.write(n)
