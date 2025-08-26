import os
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import read_data_tool

# Initialize the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.2,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Agent 1: The Financial Research Analyst
research_analyst = Agent(
    role="Financial Research Analyst",
    goal="Diligently extract and summarize key financial data from documents. Focus on revenue, profits, cash flow, and major operational highlights.",
    verbose=True,
    memory=True,
    backstory=(
        "You are a meticulous Financial Research Analyst with a strong background in"
        " dissecting complex financial reports. Your expertise lies in identifying"
        " the most critical metrics and summarizing them in a clear, concise manner for"
        " strategic review. You are known for your accuracy and attention to detail."
    ),
    tools=[read_data_tool],
    llm=llm,
    allow_delegation=False
)

# Agent 2: The Senior Investment Strategist
investment_strategist = Agent(
    role="Senior Investment Strategist",
    goal=(
        "Analyze the summarized financial data to provide strategic investment insights,"
        " assess market position, and identify potential risks and opportunities."
        " Your final output should be a comprehensive investment recommendation report."
    ),
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned Senior Investment Strategist with over 20 years of experience"
        " in major financial firms. You have a proven track record of making insightful"
        " market predictions and providing clients with sound, data-driven investment advice."
        " You transform raw data into actionable intelligence."
    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)