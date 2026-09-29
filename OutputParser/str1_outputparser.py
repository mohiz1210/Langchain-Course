from langchain_openai import ChatOpenAI
from dotenv  import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import warnings 
import os 

load_dotenv()

model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)
#prompt1
template1=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=['topic']
)
#prompt2
template2=PromptTemplate(

    template="write a 5 line summary on the following text /n {text}",
    input_variables=['text']
)

parser=StrOutputParser()

chain = template1|model|parser|template2|model|parser
result=chain.invoke({'topic':'Milkyway Galaxy'})

print(result)