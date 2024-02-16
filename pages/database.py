import streamlit as st
import sqlite3
conn=sqlite3.connect("Darabase.db")
INS= ''' 
         INSERT INTO SIGNIN(NAME,EMAIL,PASSWORD) VALUES
                ("HARSH","MYGMAIL.","PASSWORD") 
         
'''
data=conn.execute(INS)
conn.commit()
conn.close()
st.title("Harsh")
