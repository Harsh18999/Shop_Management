import streamlit as st
import psycopg2
import SIGNIN
from datetime import datetime 
#add new product in shoap by owner
def add_product():
    username=SIGNIN.variable.username
    quantity=None
    st.title("Add A New Product")
    form=st.form('Add Product Form')
    name = form.text_input("Enter Your Product Name")
    select_type=form.selectbox('Type Of Product',['Countable','Weightable'])
    if select_type=='Countable':
        quantity=form.number_input('Enter The Quantity Of Product',value=0,step=1)
    if select_type=='Weightable':
        quantity=form.number_input('Enter The Quantity Of Product ',value=0,step=1,placeholder='Enter Quantity in Kg')
    price=form.number_input('Enter Price Of Product',value=0,step=1)
    submitted=form.form_submit_button("ADD")
    if submitted:
        if len(name)!=0:
            if quantity>0:
                if price>0:
                    try:

                        conn = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
                        cursor=conn.cursor()
                        cursor.execute(" INSERT INTO {}_PRODUCT_LIST (PRODUCT_NAME,QUANTITY,PRODUCT_TYPE,PRICE) VALUES ('{}','{}', '{}','{}')".format(username,name,int(quantity),select_type,int(price)))
                        conn.commit()
                        conn.close()
                        st.success('Product Saved Successfully')
                    except:
                        st.error('This Product Already Exist')
                else:
                    st.error('Enter Valid Price')
            else:
                 st.error('Enter Valid Quantity')
        else:
             st.error('Please Enter Product Name')
        
# take a new order by owner
             
def add_new_order():
    conn = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
    name='N'
    cursor=conn.cursor()
    current_date_time = datetime.now()
    cursor=conn.cursor()
    cursor.execute(f''' SELECT PRODUCT_NAME FROM {SIGNIN.variable.username}_PRODUCT_LIST''')
    res=cursor.fetchall()
    options=[]
    for n in res:
        for m in list(n):
            options.append(m)
    st.title("Add A New Order")
    form=st.form(key='Add Order form')
    select_product=form.selectbox('Select Product',options)
    cursor.execute(f''' SELECT PRICE FROM {SIGNIN.variable.username}_PRODUCT_LIST WHERE PRODUCT_NAME='{select_product}' ''')
    res=cursor.fetchall()
    auto_value=[]
    for n in res:
        for m in list(n):
            auto_value.append(m)
    for n in options:
        if select_product==f'{n}':
            quantity=form.number_input('Enter The Quantity Of Product',value=0,step=1)
    price=form.number_input('Check Price Of Product',value=auto_value[0]*quantity)

    submitted=form.form_submit_button("ADD")
    if submitted:
        new_data=(str(name),str(select_product),price,str(current_date_time.date()),str(datetime.now().strftime("%I")+":"+datetime.now().strftime("%M")+" "+datetime.now().strftime("%p")))
        cursor.execute(f'''
                             INSERT INTO {SIGNIN.variable.username}_ALL_DATA(CUSTOMER_NAME,ORDER_NAME,PRICE,DATE,TIME) VALUES {new_data}
                      ''')
        conn.commit()
        conn.close()
        st.success("THANK YOU NEW ORDER SUCCESSFULLY ADDED")

                