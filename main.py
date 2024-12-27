import streamlit as st
from Crew import generator
import time
import os
from markdown import markdown
from pdf import convert_md_to_pdf
st.title('Market Researcher.Ai 🤖')
st.markdown("""
### About Market Researcher.Ai
Market Researcher.Ai is a cutting-edge multi-agent system designed to automate in-depth market research and AI/ML use case generation. Built using CrewAI, this solution leverages industry research, competitor analysis, and feasibility assessments to produce actionable insights. The system streamlines the entire workflow—from data gathering to report generation—ensuring depth, accuracy, and relevance in its outputs.
""")


company_input = st.text_input('Enter the company you want to research')

if st.button("Research"):
    with st.spinner('Generating Report...'):
            output = generator(company_input)
         
            time.sleep(2)  # Simulate processing time (adjust as needed)

            st.header("Here's the Market Research and AI/ML Use Case")
            st.download_button(
            label="Download Research Report",
            data=output.raw,
            file_name=company_input+'_Research_summary.md'
        )
            st.markdown(output.raw)
            



        # Save report to PDF (assuming `pdf` library can handle report generation)
       

    