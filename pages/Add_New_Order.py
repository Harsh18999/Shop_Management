# -*- coding: utf-8 -*-
from sqlalchemy import text
import streamlit as st
import pandas as pd
from datetime import datetime
conn = st.connection('mysql', type='sql')
current_date_time = datetime.now()
st.title("New custmor")
name=st.text_input("Enter custmor name")
order=st.text_input("Enter order name")
id=st.text_input("Enter Order Id")
price=int(st.number_input("Enter total amount"))
if st.button("Submit"):
    new_data=(str(name),str(order),price,str(id),str(current_date_time.date()),str(datetime.now().strftime("%I")+":"+datetime.now().strftime("%M")+" "+datetime.now().strftime("%p")))
    with conn.session as s:
        s.execute(text(f'INSERT INTO TEST1(CUSTOMER_NAME,PRODUCT_NAME,PRICE,ORDER_ID,DATE,TIME) VALUES {new_data}'))
        s.commit()
        st.success("Succesfully Saved, Thank you")