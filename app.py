from pandasai.llm.local_llm import LocalLLM
import streamlit as st 
from pandasai.connectors import MySQLConnector
from pandasai import SmartDataframe
 
my_connector = MySQLConnector(
    config={
        "host":"localhost",
        "port":3306,
        "database":"customer_behavior",
        "username":"root",
        "password":"Grelb5MPamz113wfuv",
        "table":"customer",
    }
)
 
model = LocalLLM(
    api_base="http://localhost:11434/v1",
    model="llama3"
)
 
df_connector = SmartDataframe(my_connector, config={"llm": model})
 
st.title("Ecommerce-Database-Text-to-SQL")
 
prompt = st.text_input("Enter your prompt:")
 
if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write(df_connector.chat(prompt))