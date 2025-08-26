# AI-Powered Financial Document Analyzer

A robust system that leverages AI agents to analyze corporate financial documents (such as quarterly reports) and generate comprehensive investment insights. This API allows users to upload a PDF document and receive a detailed analysis covering financial health, market position, risks, and a final investment recommendation.

---

## System Architecture

This project is built using **CrewAI**, a framework for orchestrating autonomous AI agents. The system follows a sequential process with two specialized agents:

1. **Financial Research Analyst**: Reads the uploaded document, extracts key financial metrics, and creates a concise summary.
2. **Senior Investment Strategist**: Takes the summary, performs in-depth analysis, and formulates a strategic investment recommendation based on the user’s query.

This multi-agent approach ensures a clear separation of concerns and produces more accurate insights.

---

## Bugs Found and Fixes Implemented

The initial codebase had multiple bugs and inconsistencies. Key fixes include:

### 1. Environment & Dependencies (`requirements.txt`)
- **Bug**: Python 3.9 incompatibility due to modern type-hint syntax → caused `TypeError` in CrewAI.
- **Fix**: Migrated environment to **Python 3.11** for full compatibility.
- **Bug**: Missing essential libraries (`python-dotenv`, `uvicorn`, `pypdf`, `langchain-community`, etc.).
- **Fix**: Added a complete and stable `requirements.txt` with compatible versions (`crewai`, `crewai-tools`, `langchain-google-genai`, etc.).

### 2. Agent & Task Prompts (`agents.py`, `task.py`)
- **Bug**: Original prompts were satirical and produced irrelevant output.
- **Fix**: Rewrote agent personas into professional analysts. Redesigned workflow into two steps:
  1. Extraction & Summarization
  2. Analysis & Recommendation

### 3. Core Logic (`main.py`)
- **Bug**: Crew configured with only one agent, ignoring role separation.
- **Bug**: File path of uploaded document was not passed, so it was never analyzed.
- **Fix**: Implemented sequential Crew with both agents. Correctly passed `file_path` and `query` to `crew.kickoff()`.

### 4. Tooling (`tools.py`)
- **Bug**: Used an undefined `Pdf` class → runtime crash.
- **Fix**: Replaced with **`PyPDFLoader`** from `langchain-community`.
- **Bug**: Tool not decorated for CrewAI agents.
- **Fix**: Added `@tool` decorator from `crewai-tools`.

---

## Setup and Usage

Follow these steps to set up and run the project locally.

### Prerequisites
- Python **3.11**  
- A **Google AI API Key**

### 1. Clone the Repository
```sh
git clone https://github.com/Ravishrk124/vwo-genai-assignment.git
cd vwo-genai-assignment
```

### 2. Create and Activate Virtual Environment
```sh
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

### 5. Run the Application
```sh
uvicorn main:app --reload
```
The API will be available at: **http://127.0.0.1:8000**

---

## API Documentation

Interactive docs available at: **http://127.0.0.1:8000/docs**

### Endpoint: `POST /analyze`

Uploads a financial PDF, analyzes it, and returns investment insights.

**Parameters:**
- `query` *(string, optional)* – Custom analysis query  
  Default: `"Analyze this financial document for investment insights and provide a recommendation."`
- `file` *(file upload, required)* – Financial document in PDF format  

**Example curl request:**
```sh
curl -X POST "http://127.0.0.1:8000/analyze"      -H "accept: application/json"      -H "Content-Type: multipart/form-data"      -F "query=What is the outlook for Tesla's energy business based on this report?"      -F "file=@/path/to/your/TSLA-Q2-2025-Update.pdf"
```

**Successful Response (200 OK):**
```json
{
  "status": "success",
  "query": "What is the outlook for Tesla's energy business based on this report?",
  "analysis_result": "...",
  "file_processed": "TSLA-Q2-2025-Update.pdf"
}
```
