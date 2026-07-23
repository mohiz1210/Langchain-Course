from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct"
)

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("What is the capital of Pakistan?")
print(response.content)