import streamlit as st
import sqlite3
conn=sqlite3.connect("Darabase.db")
ins=''' 
         SELECT * FROM SIGNIN
         
    '''
data=conn.execute(ins)
st.title('Harsh')
for n in data:
    st.write(n)
conn.close()
