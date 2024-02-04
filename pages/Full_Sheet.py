import streamlit as st
import pandas as pd
df=pd.read_excel("Book3 (1).xlsx")
st.title("See Your Total Data")
st.dataframe(df)