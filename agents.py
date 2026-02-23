from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from tools import ResourceValidationTool, AdsDatabaseTool, SearchTool

load_dotenv()

# Opt out of CrewAI telemetry and usage metrics to avoid OpenAI dependency
os.environ["CREWAI_TELEMETRY_OPT_OUT"] = "true"
# Forcefully clear any stale OpenAI key that might have been set
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]

# Track where we get the key from for debugging/cloud support
gemini_api_key = os.getenv("GEMINI_API_KEY")
model_id = os.getenv("MODEL_NAME", "gemini-flash-latest")

# 1. Check Streamlit Secrets (Recommended for Cloud Deployment)
try:
    import streamlit as st
    if st.secrets:
        if "GEMINI_API_KEY" in st.secrets:
            gemini_api_key = st.secrets["GEMINI_API_KEY"]
        if "MODEL_NAME" in st.secrets:
            model_id = st.secrets["MODEL_NAME"]
except Exception:
    pass # Not running in Streamlit environment or secrets not set

# 2. Check SETTINGS folder (User-friendly local override)
settings_key_path = os.path.join(os.path.dirname(__file__), "SETTINGS", "GEMINI_KEY.txt")
if os.path.exists(settings_key_path):
    with open(settings_key_path, "r") as f:
        file_key = f.read().strip()
        if file_key:
            gemini_api_key = file_key

llm = ChatGoogleGenerativeAI(
    model=model_id,
    google_api_key=gemini_api_key,
    temperature=0.2
)

# Initialize tools
# Note: Tools might still be plain classes or BaseTool, I'll update tools.py next.
# I'll assume they are restored to BaseTool next.

class MarketingAgents:
    def intelligence_agent(self):
        return Agent(
            role='Marketing Intelligence Analyst',
            goal='Gather market data and analyze competitors to find strategic opportunities.',
            backstory="""You are a dual-specialist in Market Research and Competitor Intelligence. 
            You excel at rapidly finding trends and analyzing rival strategies to provide a 
            consolidated intelligence report.""",
            tools=[SearchTool(), AdsDatabaseTool()],
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3
        )

    def scheduler_agent(self):
        return Agent(
            role='Marketing Strategy Scheduler',
            goal='Create a detailed marketing execution plan based on intelligence.',
            backstory="""You are an expert Project Manager. You take intelligence reports 
            and turn them into actionable, time-bound schedules.""",
            tools=[ResourceValidationTool()],
            llm=llm,
            verbose=True,
            allow_delegation=False,
            max_iter=3
        )
