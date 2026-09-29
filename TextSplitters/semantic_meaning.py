from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

load_dotenv()

# Embedding model
# embeddings = OpenAIEmbeddings(
#     model="nomic-embed-text-v2-moe",
#     api_key=os.getenv("OLLAMA_API_KEY"),
#     base_url="https://ollama.com/v1"
# )
embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)

# Semantic text splitter using Standard Deviation
text_splitter = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1.5
)

text = """
Pakistan is located in South Asia. Islamabad is its capital.
Karachi is the largest city.

Artificial Intelligence is changing the world.
Machine Learning is a subset of AI.
Deep Learning uses neural networks.

Cricket is the most popular sport in Pakistan.
The Pakistan cricket team has won the 1992 World Cup.
"""

docs = text_splitter.create_documents([text])
print(len(docs))
print(docs)
