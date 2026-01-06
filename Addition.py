import streamlit as st
st.title("ADDITION")
n1=st.number_input("**Enter a number n1:**")
n2=st.number_input("**Enter a number n2:**")
if(st.button("ADD",type="primary")):
    sum=n1+n2
    st.success(f"The Addition of {n1} and {n2} is : {round((sum),2)}")
else:
    st.error("Please enter a number:")