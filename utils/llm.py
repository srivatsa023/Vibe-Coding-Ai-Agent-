from config import client

def ask_llm(prompt):
    """
    Sends a prompt to Groq and returns the response.
    Used by all agents.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content