# Market Research AI - System Architecture Design Document

## 1. High-Level Design (HLD)

### 1.1 System Overview
```mermaid
graph TB
    UI[Streamlit UI Interface] --> Controller[Main Controller]
    Controller --> Crew[CrewAI Orchestrator]
    Crew --> AgentPool[Agent Pool]
    AgentPool --> A1[Industry Researcher]
    AgentPool --> A2[Use Case Generator]
    AgentPool --> A3[Content Writer]
    A1 --> Tools[Tool System]
    A2 --> Tools
    A3 --> Tools
    Tools --> T1[Search Tool]
    Tools --> T2[File Writer]
    Tools --> T3[Directory Reader]
    Tools --> T4[File Reader]
    
    subgraph External Services
        T1 --> SearchAPI[Tavily Search API]
        Crew --> Embedder[Ollama Embedder]
    end
```

### 1.2 Core Components

1. **Frontend Layer**
   - Streamlit Web Interface
   - User Input Processing
   - Report Display & Download

2. **Orchestration Layer**
   - CrewAI Controller
   - Task Scheduler
   - Memory Management
   - Embedding System

3. **Agent Layer**
   - Specialized AI Agents
   - Task Processing
   - Tool Integration

4. **Tool Layer**
   - Search Capabilities
   - File Operations
   - Data Processing

5. **External Services Layer**
   - API Integrations
   - Data Sources
   - Embedding Services

### 1.3 Data Flow
```mermaid
sequenceDiagram
    participant User
    participant UI as Streamlit UI
    participant Crew as CrewAI Orchestrator
    participant Agents as Agent Pool
    participant Tools as Tool System
    participant External as External Services

    User->>UI: Enter Company Name
    UI->>Crew: Initialize Research
    Crew->>Agents: Assign Tasks
    Agents->>Tools: Request Data
    Tools->>External: API Calls
    External->>Tools: Return Data
    Tools->>Agents: Process Results
    Agents->>Crew: Submit Findings
    Crew->>UI: Generate Report
    UI->>User: Display Results
```

## 2. Low-Level Design (LLD)

### 2.1 Component Details

#### 2.1.1 Agent System Architecture
```python
class BaseAgent:
    - role: str
    - goal: str
    - backstory: str
    - tools: List[Tool]
    - verbose: bool
    - memory: bool
    - llm: str
    - allow_delegation: bool
```

#### 2.1.2 Tool System Design
```mermaid
classDiagram
    class BaseTool {
        +name: str
        +description: str
        +_run(query: str): str
    }
    
    class SearchTool {
        +search: TavilySearchResults
        +_run(query: str): str
    }
    
    class FileWriterTool {
        +write_file(content: str, path: str): bool
    }
    
    BaseTool <|-- SearchTool
    BaseTool <|-- FileWriterTool
```

### 2.2 Detailed Component Interactions

#### 2.2.1 Task Execution Flow
```mermaid
graph LR
    A[Task Initialization] --> B[Agent Selection]
    B --> C[Tool Assignment]
    C --> D[Task Execution]
    D --> E[Result Processing]
    E --> F[Report Generation]
    
    subgraph Memory Management
        G[Context Storage]
        H[Embedding Processing]
        I[Memory Retrieval]
    end
    
    D <--> G
    G <--> H
    H <--> I
```

### 2.3 Technical Specifications

#### 2.3.1 Agent Configurations
```yaml
Industry Researcher:
  LLM: gpt-4o-mini
  Memory: Enabled
  Tools:
    - SearchTool
    - DirectoryReadTool
    - FileReadTool

AI Use Case Generator:
  LLM: gpt-4o-mini
  Memory: Enabled
  Tools:
    - SearchTool

Content Writer:
  LLM: gpt-4o-mini
  Memory: Enabled
  Tools:
    - FileWriterTool
```

#### 2.3.2 Task Processing Pipeline
```mermaid
graph TB
    subgraph Task Processing
        A[Task Input] --> B[Validation]
        B --> C[Agent Assignment]
        C --> D[Tool Selection]
        D --> E[Execution]
        E --> F[Result Validation]
        F --> G[Output Generation]
    end
    
    subgraph Error Handling
        E --> H[Error Detection]
        H --> I[Retry Logic]
        I --> E
    end
```

### 2.4 Implementation Details

#### 2.4.1 Memory Management
```python
class MemorySystem:
    def store_context(context: Dict):
        # Store context in embedding space
        pass
    
    def retrieve_context(query: str):
        # Retrieve relevant context
        pass
    
    def update_memory(new_data: Dict):
        # Update existing memory
        pass
```

#### 2.4.2 Report Generation Process
```mermaid
graph TB
    A[Raw Data] --> B[Data Processing]
    B --> C[Template Selection]
    C --> D[Content Organization]
    D --> E[Format Generation]
    E --> F[Final Report]
    
    subgraph Validation
        G[Content Check]
        H[Format Check]
        I[Reference Check]
    end
    
    D --> G
    E --> H
    F --> I
```

### 2.5 Security Considerations

1. **API Security**
   - Key Management
   - Request Authentication
   - Rate Limiting

2. **Data Protection**
   - Input Validation
   - Output Sanitization
   - Secure Storage

3. **Error Handling**
   - Graceful Degradation
   - Error Logging
   - Recovery Mechanisms

### 2.6 Scalability Design

```mermaid
graph TB
    subgraph Load Balancing
        A[Request Distribution]
        B[Agent Pool Management]
        C[Resource Allocation]
    end
    
    subgraph Performance Optimization
        D[Cache Management]
        E[Query Optimization]
        F[Memory Efficiency]
    end
    
    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
```

### 2.7 Monitoring and Logging

1. **System Metrics**
   - Agent Performance
   - Task Completion Rates
   - Error Frequencies

2. **Performance Tracking**
   - Response Times
   - Resource Usage
   - API Latency

## 3. Future Considerations

1. **Scalability Improvements**
   - Agent Pool Expansion
   - Tool Integration Framework
   - Memory Optimization

2. **Feature Enhancements**
   - Advanced Report Formats
   - Real-time Monitoring
   - Custom Agent Creation

3. **Integration Possibilities**
   - Additional Data Sources
   - Enhanced Search Capabilities
   - Advanced Visualization Tools
