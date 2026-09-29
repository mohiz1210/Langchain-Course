from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
url='https://www.amazon.com/s?k=laptop&crid=1U8DJJBG07SVX&sprefix=laptop%2Caps%2C364&ref=nb_sb_noss_1'

loader=WebBaseLoader(url)
docs=loader.load()






load_dotenv()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)
prompt=PromptTemplate(
    template="Answer the following questions{question} from the following  \n {text}",
    input_variables=['question','text']
)
parser=StrOutputParser()

chain=prompt|model|parser
print(chain.invoke({'question':'products given in this webpage','text':docs[0].page_content}))