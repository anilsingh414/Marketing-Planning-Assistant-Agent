from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchRun
from pydantic import BaseModel, Field

class ResourceValidationTool(BaseTool):
    name: str = "Resource Validation Tool"
    description: str = "Validates the availability of marketing resources like budgets, tools, or team bandwidth."

    def _run(self, resource_name: str) -> str:
        # Mocking resource validation
        resources = {
            "budget": "Available ($5000 allocated)",
            "ads_manager": "Access confirmed",
            "team_bandwidth": "80% available",
            "competitor_data": "Access to mock database available"
        }
        status = resources.get(resource_name.lower(), "Resource status unknown, assuming available for planning.")
        return f"Status for '{resource_name}': {status}"

class AdsDatabaseTool(BaseTool):
    name: str = "Ads Database Tool"
    description: str = "Searches a mock database for competitor advertisements and creative strategies."

    def _run(self, competitor_name: str) -> str:
        # Mocking competitor ads search
        mock_data = {
            "techcorp": "TechCorp is currently running video ads on LinkedIn focusing on 'AI Efficiency'.",
            "gadgethub": "GadgetHub has active search ads for 'Sustainable Electronics'.",
            "softsolutions": "SoftSolutions is focusing on 'Cloud Security' in their latest Facebook campaign."
        }
        result = mock_data.get(competitor_name.lower(), f"No specific high-volume ads found for {competitor_name}, but general industry trends suggest a focus on personalization.")
        return f"Ads Research for '{competitor_name}': {result}"

class SearchTool(BaseTool):
    name: str = "Search Tool"
    description: str = "A tool for performing real-time web searches to gather information about market trends, competitors, and industry news."

    def _run(self, query: str) -> str:
        search = DuckDuckGoSearchRun()
        return search.run(query)
