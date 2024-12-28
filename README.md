# Market Research AI 🤖

## Overview
Market Research AI is a powerful multi-agent system built with CrewAI that automates comprehensive market research and AI/ML use case generation. The system leverages three specialized AI agents to conduct research, identify opportunities, and generate detailed reports for any target company.


## Features
- 🔍 Automated industry and competitor research
- 🤖 AI/ML use case generation with dataset recommendations
- 📊 Comprehensive report generation
- 💾 Downloadable reports in Markdown format
- 🌐 User-friendly Streamlit interface
- 🧠 Powered by GPT-4 and advanced embedding models

## System Architecture
The system consists of three specialized agents:
1. **Industry Researcher**: Conducts comprehensive market research and competitor analysis
2. **AI Use Case Specialist**: Generates actionable AI/ML implementation opportunities
3. **Content Writer**: Synthesizes findings into detailed reports

## Prerequisites
- Python 3.8+
- Tavily API key
- OpenAI API key (for GPT-4)
- Internet connection for real-time research

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/market-research-ai.git
cd market-research-ai
```

2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file in the project root and add your API keys:
```env
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

## Usage

1. Start the Streamlit application
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Enter the company name you want to research

4. Click "Research" and wait for the system to generate the report

5. Download the report in Markdown format

## Project Structure
```
market-research-ai/
├── agent.py           # Agent definitions and configurations
├── Crew.py           # CrewAI setup and orchestration
├── main.py           # Streamlit interface and main application
├── Task.py           # Task definitions for agents
├── tools.py          # Custom tools including search functionality
├── requirements.txt   # Project dependencies
├── .env              # Environment variables (create this)
└── README.md         # Project documentation
```

## Configuration

### Customizing Agent Behavior
Modify `agent.py` to adjust agent roles, goals, and tools:
```python
researcher = Agent(
    role="Industry Researcher",
    goal="Your custom goal here",
    tools=[SearchTool()],
    llm="gpt-4o-mini"
)
```

### Adjusting Task Parameters
Update `Task.py` to modify research parameters and expected outputs:
```python
industry_research_task = Task(
    description="Your custom task description",
    expected_output="Your expected output format"
)
```

## Sample Output
The system generates a comprehensive report including:
- Industry analysis and segmentation
- Company's key offerings and strategic focus
- Competitor analysis
- AI/ML implementation opportunities
- Relevant datasets and resources
- Strategic recommendations

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- CrewAI framework for multi-agent orchestration
- Tavily API for enhanced search capabilities
- Streamlit for the user interface
- OpenAI for GPT-4 integration

## Support
For support, please open an issue in the GitHub repository or contact the maintainers.

## Roadmap
- [ ] Support for multiple report formats (PDF, DOCX)
- [ ] Enhanced data visualization capabilities
- [ ] Integration with additional data sources
- [ ] Real-time progress tracking
- [ ] Custom agent creation interface

## FAQ

**Q: How long does it take to generate a report?**  
A: Report generation typically takes 3-5 minutes depending on the company size and available information.

**Q: Can I customize the research parameters?**  
A: Yes, you can modify the task descriptions and agent goals in the respective Python files.

**Q: What information sources does the system use?**  
A: The system uses Tavily Search API to access publicly available information, annual reports, and industry analyses.


