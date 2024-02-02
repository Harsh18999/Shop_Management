import streamlit as st
import pandas as pd
from datetime import datetime
df=pd.read_excel("Book3 (1).xlsx")
current_date_time = datetime.now()
st.title("New custmor")
name=st.text_input("Enter custmor name")
order=st.text_input("Enter order name")
id=int(st.number_input("Enter Order Id"))
price=int(st.number_input("Enter total amount"))
if st.button("Submit"):
    new_data={"Custmor Name":name,"Order":order,"Price":price,"Order ID":id,"Date":str(current_date_time.date()),"Time":datetime.now().strftime("%I")+":"+datetime.now().strftime("%M")+" "+datetime.now().strftime("%p")}
    df.loc[len(df)]=new_data
    df.to_excel("Book3 (1).xlsx",index=False)
    st.success("Succesfully Saved, Thank you")
