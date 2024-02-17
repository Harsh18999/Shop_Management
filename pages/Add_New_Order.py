import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3
conn=sqlite3.connect("Darabase.db")
current_date_time = datetime.now()
st.title("New custmor")
name=st.text_input("Enter custmor name")
order=st.text_input("Enter order name")
id=int(st.number_input("Enter Order Id"))
price=int(st.number_input("Enter total amount"))
if st.button("Submit"):
    new_data=(str(name),str(order),price,str(id),str(current_date_time.date()),str(datetime.now().strftime("%I")+":"+datetime.now().strftime("%M")+" "+datetime.now().strftime("%p")))
    query=f"""
               INSERT INTO SELL(CUSTOMER_NAME,ORDER_NAME,PRICE,ORDER_ID,DATE,TIME) VALUES
               {new_data}
        """
    conn.execute(query)
    conn.commit()
    conn.close()
    st.success("Succesfully Saved, Thank you")

