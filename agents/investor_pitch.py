from utils.llm import ask_llm

def investor_pitch(startup_idea):
    prompt = f"""
    Create an investor pitch for this startup:

    Startup Idea:
    {startup_idea}

    Include:

    1. Elevator Pitch
    2. Problem
    3. Solution
    4. Target Market
    5. Revenue Model
    6. Why Invest
    7. Future Vision

    Make it concise and professional.
    """

    return ask_llm(prompt)