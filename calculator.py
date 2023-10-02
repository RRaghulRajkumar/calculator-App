#Importing package
import streamlit as st


st.title("Calculator")
#Create Two Numbers As input
num1=st.number_input("Enter The First Number:")
num2=st.number_input("Enter The Second Number:")
#Selecting the operations
operation=st.selectbox("Select The operations",("+","-","*","/"))

if operation == "+":
    results=num1+num2
elif operation == "-":
    results=num1-num2
elif operation == "*":
    results=num1*num2
elif operation == "/": #3/0 not possible since it will lead to infinite loop
    if num2 !=0:
        results=num1/num2
    else:
        st.error("Divison By Zero is not allowed.")
st.write(f"Results: {results}")                       

