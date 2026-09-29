from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict
import os


load_dotenv()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

class Review(TypedDict):
    summary:str
    sentiment:str

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.")
print(result)