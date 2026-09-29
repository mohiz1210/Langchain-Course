from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embeddings=HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")

document = [
    "Virat Kohli is one of the greatest batsmen in modern cricket and has scored over 80 international centuries.",
    "Babar Azam is the captain of Pakistan's cricket team and is known for his elegant batting technique.",
    "Jasprit Bumrah is an Indian fast bowler famous for his unique bowling action and deadly yorkers.",
    "Ben Stokes is an English all-rounder who played a match-winning innings in the 2019 Cricket World Cup final.",
    "Kane Williamson is the former captain of New Zealand and is respected for his calm leadership and consistent batting."
]

querry="tell me about virat kholi"

doc_embeddings=embeddings.embed_documents(document)
querry_embeddings=embeddings.embed_query(querry)
scores=cosine_similarity([querry_embeddings],doc_embeddings)[0]

index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]  #enumerate attach index



print(querry)
print(document[index])
print("similarity score is:",score)