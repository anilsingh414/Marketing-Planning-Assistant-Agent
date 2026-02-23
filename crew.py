from crewai import Crew, Process
from agents import MarketingAgents
from tasks import MarketingTasks

class MarketingCrew:
    def __init__(self, goal, competitors):
        self.goal = goal
        self.competitors = competitors
        self.agents = MarketingAgents()
        self.tasks = MarketingTasks()

    def run(self):
        # Initialize Agents
        analyst = self.agents.intelligence_agent()
        scheduler = self.agents.scheduler_agent()

        # Initialize Tasks
        task1 = self.tasks.intelligence_gathering_task(analyst, self.goal, self.competitors)
        task2 = self.tasks.scheduling_task(scheduler, [task1])

        # Assemble Crew
        crew = Crew(
            agents=[analyst, scheduler],
            tasks=[task1, task2],
            process=Process.sequential,
            memory=False,
            verbose=True
        )

        return crew.kickoff()
