import os
from crewai_tools import tool
from langchain_community.document_loaders import PyPDFLoader

@tool("Financial Document Reader Tool")
def read_data_tool(path: str) -> str:
    """
    Tool to read and extract text content from a PDF file given its path.

    Args:
        path (str): The local file path to the PDF document.

    Returns:
        str: The full text content of the financial document.
    """
    loader = PyPDFLoader(file_path=path)
    docs = loader.load()
    
    full_report = ""
    for page in docs:
        content = page.page_content
        # Clean up excessive newlines
        content = "\n".join(line for line in content.split('\n') if line.strip())
        full_report += content + "\n\n"
        
    return full_report