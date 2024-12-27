
# Task Definitions
from agent import researcher,use_case_generator,writer
from crewai import Task
# Task 1: Industry Research
industry_research_task = Task(
    description="Conduct comprehensive market research for {company}. Include a deep dive into industry trends, competitor strategies, financial benchmarks, and consumer behavior insights. Highlight technological adoption and areas for improvement.",
    expected_output="A report summarizing key findings, competitor analysis, industry benchmarks, and technological trends."
                     "Annual reports of competetor should also be analysed "
                     "Gather all the relavent links",
    agent=researcher,
)


# Task 2: AI Use Case Generation
use_case_task = Task(
    description="Based on market research, propose innovative and practical AI/ML use cases for {company}. Provide relevance to their strategic goals, datasets required, and feasibility analysis.",
    expected_output="A detailed document listing creative AI/ML use cases with feasibility assessments and potential datasets."
                     "Should dataset link",
    agent=use_case_generator,
)

# Task 3: Write Market Research Report
write_report_task = Task(
    description="Write a comprehensive market research report including industry analysis, competitor benchmarks, proposed AI/ML use cases, and strategic recommendations. Each section should provide actionable insights and measurable outcomes.",
    expected_output="A professional report covering in-depth market research, competitor analysis, AI/ML use cases, and actionable recommendations. Include data visualizations and references."
    "The report should be well detailed and should be covering all the usecases."
    "Add relavent links for annual report usecase dataset form platfroms like github,huggingface and kaggle",
    agent=writer,
)
