import streamlit as st
import random 
import psycopg2
import pandas as pd
import re
from datetime import datetime
import random
import smtplib
import variable
alphabet_list = [chr(i) for i in range(ord('a'), ord('z')+1)]
def password_and_username_validator(password,email,username):
    def password_validator(password,email):
        obj = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
        cursor=obj.cursor()
        cursor.execute(f''' SELECT PASSWORD FROM USERS WHERE EMAIL='{email}' ''')
        res=cursor.fetchall()
        for n in res:
            n=list(n)
            if n[0]==password:
                return True
            else:
                False
    def username_validator(username,email):
        obj = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
        cursor=obj.cursor()
        cursor.execute(f''' SELECT USERNAME FROM USERS WHERE EMAIL='{email}' ''')
        res=cursor.fetchall()
        for n in res:
            n=list(n)
            if n[0]==username:
                return True
            else:
                False
    if password_validator(password,email):
        if username_validator(username,email):
            return True
        else:
            st.error('Invalid Username')
            return False
    else:
        st.error('Invalid Password')
        return False


def username_checker(username):
    obj = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
    cursor=obj.cursor()
    cursor.execute(f''' SELECT USERNAME FROM USERS''')
    res=cursor.fetchall()
    users=[]
    for n in res:
        for m in list(n):
            users.append(m)
    if username in users:
        obj.close()
        return False
    else:
        obj.close()
        return True
def data_sender(mail,username,name):
    l=[]
    for n in range(8):
        a=random.choice(alphabet_list)
        l.append(str(a))
    password="".join(l)
    def password_sender(mail):
        subject='Email Varification'
        message=f''' 
                Your password is {password}. 
                Do not share this password to anyone.Thank You.
                '''
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("kumarh18999@gmail.com",password="lnip xkba bauv ctsp")
        server.sendmail("kumarh18999@gmail",{mail},msg=f"Subject: {subject}\n\n{message}")
        server.quit()
    def database(name,user_name,mail,password):
        obj = psycopg2.connect("postgresql://MYPROJECT20.COM:ZNfo9DxeFp-WoNzpTDJPmg@almond-heron-1166.j77.cockroachlabs.cloud:26257/project?sslmode=verify-full")
        cursor=obj.cursor()
        cursor.execute('''INSERT INTO USERS (USERNAME, PASSWORD, NAME, EMAIL) VALUES (%s, %s, %s, %s)''',
                       (user_name, password, name, mail))
        obj.commit()
        obj.close()
        st.success("PASSWORD HAS SEND IN YOUR EMAIL")

    try:
        password_sender(mail)
    except:
        st.warning('ERROR IN PASSWORD SENDING...!')
    
    database(name,username,mail,password)

def valid_email(mail):
    # Define the regular expression pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use re.match to check if the email matches the pattern
    match = re.match(pattern, mail)
    return bool(match)

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
                     if password_and_username_validator(password,email,user_name):
                        try:   
                            st.success("THANK YOU ")
                            variable.login_status=True
                            variable.username=user_name
                            variable.email=email
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

def Signin():
    st.title("Sign In Page")
    form=st.form("Sign In")
    name = form.text_input("Enter Your Name")
    user_name=form.text_input('Enter Your User_Name')
    email = form.text_input("Enter Your Email")
    submitted=form.form_submit_button("Submit")
    if submitted:
        if len(name)!=0:
            if username_checker(user_name):
                if valid_email(email): 
                        try: 
                            data_sender(email,user_name,name=name)
                            variable.username=user_name
                            variable.email=email
                        except:
                            st.error('SOME ERROR ...PLEASE TRY AGAIN')
                else:
                    st.warning('INVALID EMAIL')
            else:
                st.warning("THIS USERNAME ALREADY TAKEN...!")
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