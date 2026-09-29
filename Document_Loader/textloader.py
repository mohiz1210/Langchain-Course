from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate



load_dotenv()


loader = TextLoader("cricket.txt")
docs = loader.load()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)
prompt=PromptTemplate(
    template="write teh summary of teh poem \n {poem}",
    input_variables=['poem']
)
parser=StrOutputParser()



#print(type(docs))
# print(docs[0].page_content)
# print(len(docs))
# print(type(docs[0]))
# print(docs[0].metadata)

chain=prompt|model|parser
print(chain.invoke({'poem':docs[0].page_content})) 