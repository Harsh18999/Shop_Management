import streamlit as st
import pandas as pd
from datetime import datetime
import pymysql as mq
obj=mq.connect( 
                host="sql6.freesqldatabase.com" ,
                user="sql6684814",
                passwd="auFlpXBzAA",
                database="sql6684814")
cursor=obj.cursor()
current_date_time = datetime.now()
st.title("New custmor")
name=st.text_input("Enter custmor name")
order=st.text_input("Enter order name")
id=int(st.number_input("Enter Order Id"))
price=int(st.number_input("Enter total amount"))
if st.button("Submit"):
    new_data=(str(name),str(order),price,str(id),str(current_date_time.date()),str(datetime.now().strftime("%I")+":"+datetime.now().strftime("%M")+" "+datetime.now().strftime("%p")))
    query=f"INSERT INTO TEST1(CUSTOMER_NAME,PRODUCT_NAME,PRICE,ORDER_ID,DATE,TIME) VALUES {new_data}"
    try:
        cursor.execute(query)
        obj.commit()
        st.success("Succesfully Saved, Thank you")
    except:
        st.warning("SOME ERROR TRY AGAIN")

