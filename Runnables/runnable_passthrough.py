from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough


load_dotenv()
model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)
prompt1=PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template="explain the following joke {text}",
    input_variables=['text']
)
parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt1,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

chain=RunnableSequence(joke_gen_chain,parallel_chain)
print(chain.invoke({'topic':'AI'}))