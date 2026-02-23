from crewai import Task

class MarketingTasks:
    def intelligence_gathering_task(self, agent, goal, competitors):
        return Task(
            description=f"""Analyze the market and competitors for the goal: '{goal}'.
            1. Identify top 3 trends and audience insights.
            2. Analyze these competitors: {competitors} for their strengths and gaps.
            Provide a concise but data-driven intelligence report.""",
            expected_output="""A report containing both market trends and competitor 
            intelligence with actionable gaps identified.""",
            agent=agent
        )

    def scheduling_task(self, agent, context_tasks):
        return Task(
            description="""Create a chronological marketing execution plan in Markdown.
            1. Break the goal into 5-7 clear steps with resource validation.
            2. Use tables for the execution timeline.
            3. Keep the plan focused and actionable.""",
            expected_output="""A Markdown Marketing Plan with execution tables and 
            resource statuses based on the intelligence report.""",
            agent=agent,
            context=context_tasks
        )
