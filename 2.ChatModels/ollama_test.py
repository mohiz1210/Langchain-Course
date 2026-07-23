import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import warnings 


load_dotenv()

llm = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

response = llm.invoke("What is the capital of Pakisan?")

print(response.content)