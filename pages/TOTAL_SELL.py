import streamlit as st
import pandas as pd
import psycopg2 
obj = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
cursor=obj.cursor()
df=pd.DataFrame()
l=["CUSTOMER_NAME","ORDER_NAME","PRICE","ORDER_ID","DATE","TIME"]
st.title('''HEY FRIEND I AM :blue[HARSH] 👋''')
st.write("THIS IS TODAY SELL DATA")
for n in l:
    query = "SELECT {} FROM SELL_DATA".format(n)
    data=cursor.execute(query)
    result=cursor.fetchall()
    p=[]
    for k in result:
        for m in list(k):
            p.append(m)
    df[n]=p
st.dataframe(df)