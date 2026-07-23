from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(
     repo_id="gpt2",
    max_new_tokens=50,
   
)
response = llm.invoke("What is LangChain?")
print(response)