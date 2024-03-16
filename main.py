import streamlit as st
from datetime import datetime 
import psycopg2
import pandas as pd
import SIGNIN
import functions
import bill_functions

def login():
    st.title("Log In Page")
    form=st.form("Log In")
    user_name = form.text_input("Enter Your User_Name")
    email=form.text_input('Enter Your Email')
    password = form.text_input("Enter Your Password")
    submitted=form.form_submit_button("Submit")
    if submitted:
        if len(user_name)!=0:
            if len(email)!=0:
                 if len(password)!=0:
                     if SIGNIN.password_and_username_validator(password,email,user_name):
                        try:   
                            st.success("THANK YOU ")
                            st.session_state.login_status=True
                            st.session_state.username=user_name
                            st.session_state.email=email
                            st.session_state.bill_status=False
                        except:
                            st.error('SOME ERROR ...PLEASE TRY AGAIN')
                 else:
                     st.warning('Please Enter Your Password')
            else :
                st.warning("Please Enter Your Email")
        else:
            st.warning("PLEASE ENTER YOUR NAME")
    else:
        st.write(':blue[PLEASE ENTER DETAILS]')


def change_password(email):
    form=st.form("Change Password")
    form.header('Reset Password')
    ps = form.text_input("Enter Your Password")
    cps = form.text_input("Re-enter Your Password")
    submitted=form.form_submit_button("Submit")
    if submitted:
        if ps==cps:
            try:
                obj = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
                cursor=obj.cursor()
                cursor.execute(f''' UPDATE USERS
                                    SET PASSWORD = '{cps}'
                                    WHERE EMAIL = '{email}'
                                ''')
                obj.commit()
                obj.close()
                st.success('PASSWORD CHANGE SUCCESSFULLY')
            except:
                st.error('THIS USER IS NOT EXIST')
        else:
            st.warning('Password is not same ! Please check')
if 'login_status' not in st.session_state:
    st.sidebar.title('Shoap Management App')
    selected_option=st.sidebar.selectbox('DATA',['Menu','Login','Signin'])
    if selected_option=='Menu':
        st.title('''HEY FRIEND I AM :red[HARSH] 👋''')
        st.write('''
                  THIS APP DEDICATED TO THE HARSH . THIS APP PERPOSE IS GIVE SOME ANALYTICAL HELP TO SHOP KEEPS TO ANALYSIS HIS CUSTOMER DATA AND SELL DATA :blue[Thank You]''')
        st.write('Please login to access our facilities')
    elif selected_option=='Login':
        login()
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
        if st.session_state.bill_status==False:
            col1, col2= st.columns(2)
            with col1:
                bill_functions.add_new_order()
            with col2:    
                bill_functions.selected_products()
                added_product=[]
                quantity_product=[]
                price_product=[]
                dates=[]
                times=[]
                for n in bill_functions.product_list():
                    added_product.append(n[0])
                    quantity_product.append(n[1])
                    price_product.append(n[2])
                    dates.append(n[3])
                    times.append(n[4])
                bill=st.button('Generate Your Bill')
                if bill:
                    for n in range(len(bill_functions.product_list())):
                        p={"description": f"{added_product[n]}", "quantity": quantity_product[n], "unit_price": price_product[n]/quantity_product[n] ,"amount": price_product[n],'discount':'5%'}
                        bill_functions.add_item(p)
                        st.session_state.bill_status=True
                 
                
        else:
            bill_functions.main()
            back=st.button('Back')
            if back:
                st.session_state.bill_status=False
        
    if selected_option_2=='TOTAL SELL':
        obj = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
        cursor=obj.cursor()
        df=pd.DataFrame()
        l=["CUSTOMER_NAME","ORDER_NAME","PRICE","ORDER_ID","DATE","TIME"]
        st.subheader('''Your Total Sell Data''')
        for n in l:
            query = f'SELECT {n} FROM {st.session_state.username}_ALL_DATA'
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
