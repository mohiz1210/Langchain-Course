from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    temperature=1.4
)


chat = ChatHuggingFace(llm=llm)

response = chat.invoke("Write 5 line poem on Cricket")
print(response.content)