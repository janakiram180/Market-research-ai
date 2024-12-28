
# Agent 1: Industry Researcher
from crewai import Agent
from tools import SearchTool
from crewai_tools import FileWriterTool,DirectoryReadTool,FileReadTool
researcher = Agent(
    role="Industry Researcher",
    goal=(
        "Conduct comprehensive market research for the target company. "
        "Identify the industry's segmentation, key offerings, vision, and strategic focus areas. "
        "Analyze competitors' strategies and gather insights from annual reports."
    ),
    backstory=(
        "An experienced business analyst with over a decade of expertise in extracting key market insights. "
        "You specialize in identifying value propositions and competitive edges."
    ),
    tools=[SearchTool()],
    verbose=True,
    memory=True,
    llm="gpt-4o-mini",
    allow_delegation=False,
)

# Agent 2: AI Use Case Specialist
use_case_generator = Agent(
    role="AI Use Case Specialist",
    goal=(
        "Analyze market research findings and propose actionable AI/ML use cases "
        "to enhance operations, customer satisfaction, and efficiency."
    ),
    backstory=(
        "A domain expert in AI applications, known for creating impactful solutions for industry challenges. "
        "You align technology capabilities with business needs."
    ),
    tools=[SearchTool()],
    verbose=True,
    memory=True,
    llm="gpt-4o-mini",
    allow_delegation=False,
)

# Agent 3: Content Writer
writer = Agent(
    role="Content Writer",
    goal=(
        "Synthesize findings into an engaging and comprehensive market research report, "
        "highlighting industry insights, AI/ML opportunities, and strategic recommendations."
    ),
    backstory=(
        "A skilled writer with a passion for simplifying complex technical analyses into clear, actionable insights. "
        "You excel at crafting content that resonates with technical and non-technical audiences alike."
    ),
    tools=[FileWriterTool()],
    verbose=True,
    memory=True,
    llm="gpt-4o-mini",
    allow_delegation=False,
)
