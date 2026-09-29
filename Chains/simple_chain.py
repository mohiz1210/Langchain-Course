from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


load_dotenv()
model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)

parser=StrOutputParser()
prompt=PromptTemplate(
    template="Generate 5 facts about {topic}",
    input_variables=['topic']
)

chain=prompt|model|parser
result=chain.invoke({'topic':'Poverty'})
print(result)
chain.get_graph().print_ascii()