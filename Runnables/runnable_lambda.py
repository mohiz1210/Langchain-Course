from langchain_openai import ChatOpenAI
import os
import warnings
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda


load_dotenv()
model = ChatOpenAI(
    model="gpt-oss:120b",
    api_key=os.getenv("OLLAMA_API_KEY"),
    base_url="https://ollama.com/v1",
)


def word_counter(text):
    return len(text.split())

runnnable_word_counter=RunnableLambda(word_counter)


prompt=PromptTemplate(
    template="write a joke about {topic}",
    input_variables=['topic']
)

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_counter)
})

chain=RunnableSequence(joke_gen_chain,parallel_chain)
print(chain.invoke({'topic':'AI'}))