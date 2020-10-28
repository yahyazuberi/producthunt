import mysql.connector as connectSQL
import pickle
import numpy as np 
import pandas as pd
import streamlit as st
from PIL import Image
st.title("WELCOME TO APOCALPSE")
#img= Image.open("https://static-01.daraz.pk/p/fac8bd12cd45410dbbf16c851d24a313.jpg")
#st.markdown("![Alt Text](https://static-01.daraz.pk/p/fac8bd12cd45410dbbf16c851d24a313.jpg)")
mySQL=connectSQL.connect(
    host='us-cdbr-east-02.cleardb.com',
    user='b10d084aa9cfc9',
    password="a7574329",
    database='heroku_1df534c0b5219bd'
)
myCursor=mySQL.cursor()
def get_Category():
    myCursor.execute("SELECT * FROM category")
    myResults=myCursor.fetchall()
    for result in myResults:
        category.append(result)            #try to change in dict
def search():
    stcat=st.multiselect("Selct your categories",category)
    mnprice=st.text_input("Enter Min Price","For e.g 1000")
    mxprice=st.text_input("Enter Max Price","For e.g 5000")
    if st.button("Search"):
        if len(stcat)==0:
            st.warning("Select category")
        else:
            #print(stcat[0][1])
            sql_select_query = """select sku,price,brand from product where price > %s AND price < %s AND category_id=%s"""
            myCursor.execute(sql_select_query, (int(mnprice),int(mxprice),int(stcat[0][0])))
            myResults=myCursor.fetchall()
            for result in myResults:
                #qres.append(result)
                st.success(result)
    #pricemin=5000
    #pricemax=9000
    #c_id=46
    
    #cat=input("Enter your cat")
    #pricemin=input("Min Price")
    #pricemax=input("Max Price")
    #for j in range(0,len(category),1):
     #   if cat==category[j][1]:
      #      c_id=category[j][0]
    
    
if __name__ == "__main__":
 #print("yes")
    category=[]
    qres=[]

    #
    get_Category()
    search()
    print(qres)
    #search()