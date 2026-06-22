from groq import Groq

client = Groq(
    api_key="gsk_..."
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "Say hello to Srivatsa"
        }
    ]
)

print(response.choices[0].message.content)