from utils.llm import ask_llm

def business_strategy(startup_idea, research_data):
    prompt = f"""

    You are an expert startup consultant.

    Create a detailed business strategy for the following startup.

    Startup Idea:
    {startup_idea}

    Market Research:
    {research_data}

    Provide:

    1. Revenue Model
    2. Pricing Strategy
    3. Launch Plan
    4. Growth Strategy

    Make the strategy specific to this startup idea.
    Avoid generic advice.
    """

    
    return ask_llm(prompt)
    
