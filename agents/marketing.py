from utils.llm import ask_llm

def marketing(content):

    prompt = f"""
    Based on this startup content:

    {content}

    Generate:
    1. Instagram Post
    2. LinkedIn Post
    3. Marketing Tagline
    4. Email Campaign
    5. Advertisement Copy
    """

    return ask_llm(prompt)