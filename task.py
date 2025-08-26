from crewai import Task
from agents import research_analyst, investment_strategist
from tools import read_data_tool

# Task 1: Data Extraction and Summarization
extract_and_summarize_task = Task(
    description=(
        "Read the financial document located at '{file_path}'. Extract key financial metrics"
        " including total revenues, net income, free cash flow, and operational highlights."
        " Provide a concise summary of the company's performance in the reported quarter."
    ),
    expected_output=(
        "A summarized report containing bullet points of key financial figures (Revenue, Net Income, etc.)"
        " and a brief paragraph on the company's major achievements and challenges during the period."
    ),
    agent=research_analyst,
    tools=[read_data_tool],
)

# Task 2: Investment Analysis and Recommendation
analyze_and_recommend_task = Task(
    description=(
        "Using the summarized financial report, conduct a thorough analysis of the company's"
        " financial health, market position, and future outlook. Based on the user's query '{query}',"
        " formulate a strategic investment recommendation. Identify key risks and potential growth opportunities."
    ),
    expected_output=(
        "A comprehensive investment report structured with the following sections:\n"
        "1. **Executive Summary:** A brief overview of the investment recommendation.\n"
        "2. **Financial Health Analysis:** An assessment of the company's stability and performance.\n"
        "3. **Market Position & Opportunities:** Analysis of competitive advantages and growth potential.\n"
        "4. **Potential Risks:** A breakdown of key risks to consider.\n"
        "5. **Final Recommendation:** A clear 'Buy', 'Hold', or 'Sell' recommendation with a supporting thesis."
    ),
    agent=investment_strategist,
    context=[extract_and_summarize_task], # This task depends on the output of the first one
)