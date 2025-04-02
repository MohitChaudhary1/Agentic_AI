from crewai import Agent, Task, Crew, Process
import os


os.environ["OPENAI_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'llama3-70b-8192'
os.environ["OPENAI_API_KEY"] = 'api-key'  

#  Cricket Experts
match_analyst = Agent(
    role="Cricket Match Analyst",
    goal="Analyze past matches and predict outcomes based on stats",
    backstory="""A former statistician for a national cricket board, now an expert in predictive analytics for T20, ODI, and Test matches.""",
    verbose=True
)

bowling_coach = Agent(
    role="Bowling Strategy Coach",
    goal="Develop bowling plans against key batsmen",
    backstory="""Ex-international bowler who specializes in decoding batsmen's weaknesses and setting field placements.""",
    verbose=True
)

batting_consultant = Agent(
    role="Batting Performance Consultant",
    goal="Improve batsmen's techniques using data",
    backstory="""A sports scientist who uses biomechanics and AI to refine batting strategies.""",
    verbose=True
)

commentary_writer = Agent(
    role="AI Commentary Writer",
    goal="Generate engaging match commentary",
    backstory="""A former sports journalist who now creates AI-powered live commentary scripts.""",
    verbose=True
)

#  Tasks
match_prediction_task = Task(
    description="""Analyze the last 5 matches between India and Australia. 
    Predict the likely winner of the next match based on pitch conditions, player form, and historical data.""",
    expected_output="A detailed match prediction report (min 300 words).",
    agent=match_analyst,
    output_file="match_prediction.md"
)

bowling_plan_task = Task(
    description="""Create a bowling strategy to dismiss Virat Kohli in a T20 match. 
    Include field placements, bowler matchups, and ball-by-ball tactics.""",
    expected_output="A tactical bowling plan (min 200 words).",
    agent=bowling_coach,
    output_file="bowling_plan.md"
)

batting_analysis_task = Task(
    description="""Analyze Steve Smith's last 10 innings and identify weaknesses in his technique. 
    Suggest improvements using video analysis and data.""",
    expected_output="A technical batting report (min 250 words).",
    agent=batting_consultant,
    output_file="batting_analysis.md"
)

commentary_task = Task(
    description="""Write a dynamic commentary script for a hypothetical India vs. Pakistan T20 match. 
    Include key moments, player reactions, and expert insights.""",
    expected_output="A lively match commentary (min 400 words).",
    agent=commentary_writer,
    output_file="match_commentary.md"
)

#  Crew
crew = Crew(
    agents=[match_analyst, bowling_coach, batting_consultant, commentary_writer],
    tasks=[match_prediction_task, bowling_plan_task, batting_analysis_task, commentary_task],
    verbose=2,
    process=Process.sequential  
)


print("Starting Cricket Analytics Crew...")
results = crew.kickoff()


with open("cricket_analysis_report.md", "w") as f:
    f.write("# Cricket Strategy Report\n\n")
    f.write("## Match Prediction\n" + match_prediction_task.output.result + "\n\n")
    f.write("## Bowling Plan\n" + bowling_plan_task.output.result + "\n\n")
    f.write("## Batting Analysis\n" + batting_analysis_task.output.result + "\n\n")
    f.write("## Match Commentary\n" + commentary_task.output.result + "\n")

print(" Cricket analysis complete! Check cricket_analysis_report.md")
