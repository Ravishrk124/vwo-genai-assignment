# AI-Powered Financial Document Analyzer

A robust system that leverages AI agents to analyze corporate financial documents (such as quarterly reports) and generate comprehensive investment insights. This API allows users to upload a PDF document and receive a detailed analysis covering financial health, market position, risks, and a final investment recommendation.

## System Architecture

This project is built using **CrewAI**, a framework for orchestrating autonomous AI agents. The system follows a sequential process with two specialized agents:

1.  **Financial Research Analyst**: This agent is responsible for reading the uploaded document, extracting key financial metrics, and creating a concise summary.
2.  **Senior Investment Strategist**: This agent takes the summary from the first agent, performs an in-depth analysis, and formulates a strategic investment recommendation based on the user's query.

This multi-agent approach ensures a clear separation of concerns and produces a more detailed and accurate analysis.

---

## Bugs Found and Fixes Implemented

The initial codebase contained numerous deterministic bugs, inefficient AI prompts, and critical environment incompatibilities. The following is a comprehensive list of the fixes implemented.

### 1. Environment & Dependencies (`requirements.txt`)
* **Bug**: The project was fundamentally incompatible with the common system Python 3.9 due to modern syntax (`|` for type hints) used within the libraries. This caused a `TypeError` deep inside `crewai` even with older versions.
* **Fix**: Re-architected the environment setup to use **Python 3.11**, which is compatible with modern AI libraries. This solved all underlying dependency and syntax conflicts.
* **Bug**: The original `requirements.txt` was missing numerous essential libraries (`python-dotenv`, `uvicorn`, `pypdf`, `langchain-community`, etc.).
* **Fix**: Created a new, stable `requirements.txt` with modern, compatible versions of all necessary libraries (`crewai`, `crewai-tools`, `langchain-google-genai`, etc.) for the Python 3.11 environment.

### 2. Agent & Task Prompts (`agents.py`, `task.py`)
* **Bug**: All agent prompts (role, goal, backstory) and task descriptions were satirical and instructed the AI to produce useless, fabricated output.
* **Fix**: Completely rewrote the agent personas to be professional, expert-level analysts with clear, focused goals. Redefined the tasks into a logical, two-step workflow: (1) Extraction & Summarization, and (2) Analysis & Recommendation. This was the most critical fix for improving output quality.

### 3. Core Logic (`main.py`)
* **Bug**: The Crew was incorrectly configured with only one agent and task, ignoring the specialized roles defined in the codebase.
* **Bug**: The file path for the uploaded document was not passed into the CrewAI workflow, meaning the document was never actually read or analyzed.
* **Fix**: Re-architected the `Crew` to include both the `research_analyst` and `investment_strategist` agents in a sequential process. Correctly passed the `file_path` and `query` into the `crew.kickoff()` method's `inputs` dictionary.

### 4. Tooling (`tools.py`)
* **Bug**: The PDF reading tool used an undefined `Pdf` class and would have crashed.
* **Fix**: Replaced the faulty implementation with the standard and reliable `PyPDFLoader` from `langchain-community`.
* **Bug**: The tool was not properly decorated for use by CrewAI agents.
* **Fix**: Added the `@tool` decorator from `crewai-tools` to ensure the function is discoverable by the agents.

---

## Setup and Usage

Follow these steps to set up and run the project locally.

### Prerequisites
* Python 3.11 (Installation via Homebrew on macOS is recommended: `brew install python@3.11`)
* A Google AI API Key

### 1. Clone the Repository
```sh
git clone [https://github.com/Ravishrk124/vwo-genai-assignment.git](https://github.com/Ravishrk124/vwo-genai-assignment.git)
cd vwo-genai-assignment
