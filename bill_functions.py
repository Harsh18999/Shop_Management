import streamlit as st
import psycopg2
from datetime import datetime
import SIGNIN
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import base64
from io import BytesIO
import variable

@st.cache_resource
def product_list():
        list=[]
        return list
def add_product(list):
    product_list().append(list)

@st.cache_resource
def items():
    items=[]
    return items
def add_item(item):
    items().append(item)


def create_invoice(bill_info, items):
    buffer=BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Header
    c.setFont('Helvetica-Bold', 12)
    c.drawString(50, height - 50, bill_info['header'])
    
    # Address and Contact Info
    c.setFont('Helvetica', 10)
    y_position = height - 70
    for line in bill_info['address']:
        c.drawString(50, y_position, line)
        y_position -= 15
    
    # Bill To Section
    y_position -= 15 
    for line in bill_info['bill_to']:
        c.drawString(50, y_position, line)
        y_position -= 15
    
    # Table Header
    headers = ['DESCRIPTION', 'QUANTITY', 'UNIT PRICE', 'AMOUNT','DISCOUNT']
    x_positions = [50, 150,250, 350, 450]
    y_position -= 30
     
    for x_pos, header in zip(x_positions, headers):
        c.drawString(x_pos, y_position, header)

    # Table Content 
    y_position -= 30 
     
    for item in items:
        x_pos = x_positions[0]
        for value in item.values():
            c.drawString(x_pos, y_position, str(value))
            x_pos += 100 
         
        y_position -= 20 

    # Footer 
    footer_y_position = 100 
    for line in bill_info['footer']:
        c.drawCentredString(width / 2.0, footer_y_position, line)
        footer_y_position -= 15 
    c.save()
    return buffer.getvalue()

bill_information = {
    "header": "SHOAP MANAGEMENT SYSTEM",
    "address": [
        "Near Allahabad Medical Asosiation",
        "Prayagraj,Uttar Pradesh",
        "211001",
        "Con-7897972297"
    ],
    "bill_to": [
        "Customer Name : Harsh Kumar",
        "Email : kumarh18999@gmail.com"
    ],
    "footer": ["THANK YOU FOR YOUR SHOAPING!"]
}
def main():
    st.title("PDF Viewer")

    # Upload PDF file
    

    
        # Read the uploaded PDF file as bytes
    pdf_contents = create_invoice(bill_information,items())

        # Convert binary data to base64
    pdf_base64 = base64.b64encode(pdf_contents).decode("utf-8")

        # Embed base64-encoded PDF content using iframe
    st.markdown(f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="700" height="500"></iframe>',
                    unsafe_allow_html=True)

def add_new_order():
    conn = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=require&sslrootcert=root.crt")
    cursor=conn.cursor()
    current_date_time = datetime.now()
    cursor=conn.cursor()
    cursor.execute(f''' SELECT PRODUCT_NAME FROM {SIGNIN.variable.username}_PRODUCT_LIST''')
    res=cursor.fetchall()
    options=[]
    for n in res:
        for m in list(n):
            options.append(m)
    st.subheader("Add A New Order")
    form=st.form(key='Add Order form')
    customer_name=form.text_input('Enter Customer Name (Optional)',value='N')
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
        if quantity>0:
            try:
                new_data=(str(customer_name),str(select_product),price,str(current_date_time.date()),str(datetime.now().strftime("%I")+":"+datetime.now().strftime("%M")+" "+datetime.now().strftime("%p")))
                cursor.execute(f'''
                             INSERT INTO {SIGNIN.variable.username}_ALL_DATA(CUSTOMER_NAME,ORDER_NAME,PRICE,DATE,TIME) VALUES {new_data}
                      ''')
                conn.commit()
                add_product([select_product,quantity,price,str(current_date_time.date()),str(datetime.now().strftime("%I")+":"+datetime.now().strftime("%M")+" "+datetime.now().strftime("%p"))])
                st.success('Successfully added')
            except:
                st.error('Some error {e}')
        else:
            st.warning('Enter Valid Quantity Of Product')
def selected_products():
    df=pd.DataFrame()
    st.subheader('Selected Product')
    added_product=[]
    quantity_product=[]
    price_product=[]
    dates=[]
    times=[]
    for n in product_list():
        added_product.append(n[0])
        quantity_product.append(n[1])
        price_product.append(n[2])
        dates.append(n[3])
        times.append(n[4])
    df['PRODUCTS']=added_product
    df['QUANTITY']=quantity_product
    df['PRICE']=price_product
    df['DATE']=dates
    df['TIME']=times
    st.table(df)
    col3,col4=st.columns(2)
    with col3:
        reset=st.button('Cancel Order')
        if reset:
            conn = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=require&sslrootcert=root.crt")
            cursor=conn.cursor()
            for n in range (len(dates)):
                cursor.execute(f'''DELETE FROM {SIGNIN.variable.username}_ALL_DATA
                                   WHERE DATE='{str(dates[n])}' AND TIME='{str(times[n])}'
                                ''')
            conn.commit()
            st.cache_resource.clear()
    with col4:
        button=st.button('Reset')
        if button:
            st.cache_resource.clear()
            st.success('Reset Successfully')
    bill=st.button('Generate Your Bill')
    if bill:
        for n in range(len(product_list())):
           p={"description": f"{added_product[n]}", "quantity": quantity_product[n], "unit_price": price_product[n]/quantity_product[n] ,"amount": price_product[n],'discount':'5%'}
           add_item(p)
        variable.bill_status=True
if variable.bill_status==False:
    col1, col2= st.columns(2)
    with col1:
        add_new_order()
    with col2:
        selected_products()
else:
    main()
    back=st.button('Back')
    if back:
        variable.bill_status=False
