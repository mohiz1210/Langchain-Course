from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are my helpful {domain} assistant."),
    ("human", "Explain in simple terms what is {topic}.")
])

prompt = chat_template.invoke({
    "domain": "Cricket",
    "topic": "Doosra"
})

# Send the prompt to the model
result = model.invoke(prompt)

# Print only the generated response
print(result.content)