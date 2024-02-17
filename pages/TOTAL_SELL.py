import sqlite3
import streamlit as st
import pandas as pd
df=pd.DataFrame()
l=["CUSTOMER_NAME","ORDER_NAME","PRICE","ORDER_ID","DATE","TIME"]
conn=sqlite3.connect("Darabase.db")
st.title('''HEY FRIEND I AM HARSH 👋''')
st.write("THIS IS TOTAL SELL DATA")
for n in l:
    query = f'''
            SELECT {n} FROM SELL
    '''
    data=conn.execute(query)
    p=[]
    for k in data:
        for m in list(k):
            p.append(m)
    df[n]=p
    conn.commit()
st.dataframe(df)
conn.close()
