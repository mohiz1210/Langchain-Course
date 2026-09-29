from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_openai import ChatOpenAI
from dotenv  import load_dotenv
import warnings 
import os 

load_dotenv()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

messages=[
    SystemMessage(content="You are helpfull assistant"),
    HumanMessage(content="What is the Capital of Pakistan")
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages) 