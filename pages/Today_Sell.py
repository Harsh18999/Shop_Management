import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
df=pd.read_excel("Book3 (1).xlsx")
current_date_time = datetime.now()
st.title("Todays Toatal Sell")
list_date=np.array(df["Date"])
list_price=np.array(df['Price'])
Today_sell=0
for n in range(len(list_date)):
    if list_date[n]==str(current_date_time.date()):
        Today_sell=Today_sell+list_price[n]
st.write("Your Todays sell Is :-",Today_sell,"Rs")