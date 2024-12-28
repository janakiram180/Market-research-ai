from crewai import Crew
from agent import researcher,use_case_generator,writer
from embedchain import App
from Task import industry_research_task,use_case_task ,write_report_task
from pdf import convert_md_to_pdf
crew = Crew(
    agents=[researcher,use_case_generator,writer],
    tasks=[industry_research_task, use_case_task,write_report_task],
    verbose=True,
    planning=True,  # Enable planning feature
    memory=True,
    embedder={
        "provider": "ollama",
        "config": {
            "model": "mxbai-embed-large"
        }}

)

# Execute tasks
def generator(input):
     app = App.from_config(config_path="config.yaml")
     return crew.kickoff(inputs={'company':input})
    # md_file_path = "reports/final_proposal_report.md"
    # pdf_file_path = "reports/market_research_report.pdf"
    # return convert_md_to_pdf(md_file_path, pdf_file_path)
