import streamlit as st
import pandas as pd
import pymysql as mq
obj=mq.connect( 
                host="sql6.freesqldatabase.com" ,
                user="sql6684814",
                passwd="auFlpXBzAA",
                database="sql6684814")
cursor=obj.cursor()
df=pd.DataFrame()
l=["CUSTOMER_NAME","PRODUCT_NAME","PRICE","ORDER_ID","DATE","TIME"]
st.title('''HEY FRIEND I AM :blue[HARSH] 👋''')
st.write("THIS IS TODAY SELL DATA")
for n in l:
    query = "SELECT {} FROM TEST1".format(n)
    data=cursor.execute(query)
    result=cursor.fetchall()
    p=[]
    for k in result:
        for m in list(k):
            p.append(m)
    df[n]=p
st.dataframe(df)