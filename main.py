from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
from crewai import Crew, Process
from agents import research_analyst, investment_strategist
from task import extract_and_summarize_task, analyze_and_recommend_task

app = FastAPI(
    title="Financial Document Analyzer API",
    description="An AI-powered system to analyze financial documents and provide investment insights.",
    version="1.0.0"
)

def run_financial_crew(query: str, file_path: str):
    """Initializes and runs the financial analysis crew."""
    financial_crew = Crew(
        agents=[research_analyst, investment_strategist],
        tasks=[extract_and_summarize_task, analyze_and_recommend_task],
        process=Process.sequential,
        verbose=2
    )

    # The inputs dictionary must match the placeholders in the task descriptions
    result = financial_crew.kickoff(inputs={
        'query': query,
        'file_path': file_path
    })
    return result

@app.get("/", tags=["Health Check"])
async def root():
    """Health check endpoint to ensure the API is running."""
    return {"message": "Financial Document Analyzer API is operational."}

@app.post("/analyze", tags=["Analysis"])
async def analyze_document_endpoint(
    query: str = Form(default="Analyze this financial document for investment insights and provide a recommendation."),
    file: UploadFile = File(...)
):
    """
    Uploads a financial document (PDF) and analyzes it to provide comprehensive investment recommendations.
    """
    file_id = str(uuid.uuid4())
    file_path = f"data/financial_document_{file_id}.pdf"

    try:
        os.makedirs("data", exist_ok=True)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        if not query or not query.strip():
            query = "Analyze this financial document for investment insights and provide a recommendation."

        response = run_financial_crew(query=query.strip(), file_path=file_path)

        return {
            "status": "success",
            "query": query,
            "analysis_result": str(response),
            "file_processed": file.filename
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during document processing: {str(e)}")

    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error removing file {file_path}: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)