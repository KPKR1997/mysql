import pandas as pd
import streamlit as st
from config.connection import upload_sql, call_mysql


df = call_mysql('credit_card_fraud_detection', 'creditcard_data', '*')

st.write(df.head(10))

