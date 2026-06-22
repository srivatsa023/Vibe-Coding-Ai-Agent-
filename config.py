from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("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")
)