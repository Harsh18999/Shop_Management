import streamlit as st
import sqlite3
conn=sqlite3.connect("Darabase.db")
INS= ''' 
         INSERT INTO SIGNIN(NAME,EMAIL,PASSWORD) VALUES
                ("HARSH","MYGMAIL.COM","PASSWORD") 
         
    '''
data=conn.execute(INS)
st.title('Harsh')
conn.commit()
conn.close()
