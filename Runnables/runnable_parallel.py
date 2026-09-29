from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_core.runnables import RunnableSequence,RunnableParallel


load_dotenv()
model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)
prompt1=PromptTemplate(
    template="Generate tweet about  {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="Generate a linked in post about {topic}",
    input_variables=['topic']
)
parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})
result=parallel_chain.invoke({'topic':'AI'})
print(result['tweet'])
print(result['linkedin'])