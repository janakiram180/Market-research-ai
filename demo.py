import streamlit as st
import markdown

with open('reports/detailed_use_cases.md','r') as file:
    text = file.read()
    st.markdown(text)
    st.download_button(label="Download The Report",data=text,file_name='report.pdf')
    # mark = markdown(text)
