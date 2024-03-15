import streamlit as st
from datetime import datetime 
import psycopg2
import pandas as pd
import SIGNIN
import functions
import bill_functions

if SIGNIN.variable.login_status==False:
    st.sidebar.title('Shoap Management App')
    selected_option=st.sidebar.selectbox('DATA',['Menu','Login','Signin'])
    if selected_option=='Menu':
        st.title('''HEY FRIEND I AM :red[HARSH] 👋''')
        st.write('''
                  THIS APP DEDICATED TO THE HARSH . THIS APP PERPOSE IS GIVE SOME ANALYTICAL HELP TO SHOP KEEPS TO ANALYSIS HIS CUSTOMER DATA AND SELL DATA :blue[Thank You]''')
        st.write('Please login to access our facilities')
    elif selected_option=='Login':
        SIGNIN.login()
    elif selected_option=='Signin':
        SIGNIN.Signin()
else:
    st.sidebar.title('Shoap Management App')
    selected_option_1=st.sidebar.selectbox('Change Password',['Not Selected','Change Password'])
    if selected_option_1=='Not Selected':
        st.write()
    if selected_option_1=='Change Password':
        SIGNIN.change_password(SIGNIN.variable.email)

# data analysis and management 
    options=['Not Selected','ADD NEW CUTOMER','TOTAL SELL','ADD PRODUCT']
    selected_option_2=st.sidebar.selectbox('DATA',options)
    if selected_option_2=='Not Selected':
        st.write()
    if selected_option_2=='ADD NEW CUTOMER':
        if bill_functions.variable.bill_status==False:
            col1, col2= st.columns(2)
            with col1:
                bill_functions.add_new_order()
            with col2:    
                bill_functions.selected_products()
        else:
            bill_functions.main()
            back=st.button('Back')
            if back:
                bill_functions.variable.bill_status=False
        
    if selected_option_2=='TOTAL SELL':
        obj = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=require&sslrootcert=root.crt")
        cursor=obj.cursor()
        df=pd.DataFrame()
        l=["CUSTOMER_NAME","ORDER_NAME","PRICE","ORDER_ID","DATE","TIME"]
        st.subheader('''Your Total Sell Data''')
        for n in l:
            query = f'SELECT {n} FROM {SIGNIN.variable.username}_ALL_DATA'
            cursor.execute(query)
            result=cursor.fetchall()
            p=[]
            for k in result:
                for m in list(k):
                    p.append(m)
            df[n]=p
        st.table(df)

    if selected_option_2=='ADD PRODUCT':
        functions.add_product()
    
    if selected_option_1=='Not Selected' and selected_option_2=='Not Selected':
        st.title('''HEY FRIEND I AM :red[HARSH] 👋''')
        st.write('''
               THIS APP DEDICATED TO THE HARSH . THIS APP PERPOSE IS GIVE SOME ANALYTICAL HELP TO SHOP KEEPS TO ANALYSIS HIS CUSTOMER DATA AND SELL DATA :blue[Thank You]''')
        st.write('Please login to access our facilities')
