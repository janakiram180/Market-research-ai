# Market Research AI Documentation

## Project Overview
Market Research AI is a multi-agent system built using the CrewAI framework that automates comprehensive market research and AI/ML use case generation. The system employs three specialized agents working in concert to research companies, generate AI use cases, and produce detailed reports.

## System Architecture

### Core Components

1. **Agents** (`agent.py`)
   - Industry Researcher: Conducts market research and competitor analysis
   - AI Use Case Specialist: Generates AI/ML implementation opportunities
   - Content Writer: Synthesizes findings into comprehensive reports

2. **Crew Orchestration** (`Crew.py`)
   - Manages agent collaboration and task execution
   - Integrates with Ollama embeddings for enhanced context understanding
   - Handles task planning and memory management

3. **Task Management** (`Task.py`)
   - Industry Research Task: Gathers market and competitor intelligence
   - Use Case Generation Task: Identifies AI/ML opportunities
   - Report Writing Task: Produces final deliverables

4. **Tools** (`tools.py`)
   - Custom SearchTool using Tavily Search API
   - Integration with file operations tools
   - Environment variable management

5. **User Interface** (`main.py`)
   - Streamlit-based web interface
   - Report generation and download functionality
   - Interactive company research initiation

## Detailed Component Documentation

### Agents Configuration

```python
class IndustryResearcher:
    Role: "Industry Researcher"
    Tools: SearchTool
    LLM: "gpt-4o-mini"
    Features: Memory enabled, Verbose logging

class UseCaseGenerator:
    Role: "AI Use Case Specialist"
    Tools: SearchTool
    LLM: "gpt-4o-mini"
    Features: Memory enabled, Verbose logging

class ContentWriter:
    Role: "Content Writer"
    Tools: FileWriterTool
    LLM: "gpt-4o-mini"
    Features: Memory enabled, Verbose logging
```

### Task Specifications

1. **Industry Research Task**
   - Analyzes company's industry segment
   - Identifies key offerings and strategic focus
   - Performs competitor analysis
   - Gathers relevant documentation and links

2. **Use Case Generation Task**
   - Analyzes industry AI/ML trends
   - Proposes GenAI and LLM implementations
   - Identifies relevant datasets from platforms
   - Provides feasibility assessments

3. **Report Writing Task**
   - Synthesizes research findings
   - Documents AI/ML use cases
   - Includes actionable recommendations
   - Incorporates data visualizations

### System Workflow

1. **Initialization**
   ```python
   # Initialize crew with agents and tasks
   crew = Crew(
       agents=[researcher, use_case_generator, writer],
       tasks=[industry_research_task, use_case_task, write_report_task],
       planning=True,
       memory=True
   )
   ```

2. **Execution Flow**
   - User inputs company name via Streamlit interface
   - Crew orchestrates sequential task execution
   - Agents collaborate using shared memory
   - Final report generated in markdown format

### Integration Features

1. **Embedding Configuration**
   ```python
   embedder={
       "provider": "ollama",
       "config": {
           "model": "mxbai-embed-large"
       }
   }
   ```

2. **Search Tool Integration**
   ```python
   class SearchTool(BaseTool):
       name: str = "Search"
       description: str = "Useful for search-based queries"
       search: TavilySearchResults
   ```

## Setup and Configuration

### Environment Requirements
1. Create `.env` file with required API keys:
   - TAVILY_API_KEY
   - Other necessary API credentials

### Installation Steps
1. Install required packages:
   ```bash
   pip install crewai streamlit embedchain
   ```

2. Configure environment:
   ```python
   load_dotenv(dotenv_path='.env')
   ```

## Usage Guide

1. Start the application:
   ```bash
   streamlit run main.py
   ```

2. Enter company name in the web interface

3. System will generate:
   - Industry analysis
   - Competitor insights
   - AI/ML use cases
   - Downloadable report

## Security Considerations

1. API Key Management
   - Uses environment variables
   - Secure credential handling

2. Data Processing
   - Local processing when possible
   - Secure API interactions

## Error Handling

1. Search Tool Errors:
   ```python
   try:
       return self.search.run(query)
   except Exception as e:
       return f"Error performing search: {str(e)}"
   ```

2. Report Generation:
   - Graceful failure handling
   - User feedback via Streamlit interface

## Future Enhancements

1. Additional Features
   - Support for multiple report formats
   - Enhanced data visualization
   - Real-time progress tracking

2. Potential Improvements
   - Additional search providers
   - Extended agent capabilities
   - Advanced memory management

## Dependencies
- crewai
- streamlit
- embedchain
- tavily-python
- python-dotenv
- markdown
- pydantic

## Best Practices
1. Agent Design
   - Clear role definition
   - Specific tool assignments
   - Memory management

2. Task Management
   - Detailed descriptions
   - Clear expected outputs
   - Sequential dependencies

3. Report Generation
   - Structured format
   - Referenced sources
   - Actionable insights
