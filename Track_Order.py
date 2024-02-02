import streamlit as st
import pandas as pd
df=pd.read_excel("Book3 (1).xlsx")
st.title("Track Your Order")
Track_user_input=st.number_input("Enter Order ID")
if st.button("Submit"):
    l=list(df["Order ID"])
    for n in range(len(df)):
        if l[n] == Track_user_input:
            st.write(df.iloc[n])
    if Track_user_input not in l:
        st.warning("Invalid Order ID")