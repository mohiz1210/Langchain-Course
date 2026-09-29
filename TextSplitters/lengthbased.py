from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader('OEL(OS).pdf')
docs=loader.load()

# text=""""A neural network is a type of artificial intelligence model inspired by the structure and functioning of the human brain. It consists of interconnected nodes, called neurons, which work together to process information and solve complex problems. Neural networks are a fundamental component of machine learning and deep learning, enabling computers to recognize patterns, make predictions, and learn from data without being explicitly programmed for every task.

# A neural network is typically organized into three types of layers: the input layer, one or more hidden layers, and the output layer. The input layer receives data, such as images, text, or numerical values. The hidden layers process this information by applying mathematical operations and learning patterns from the data. Finally, the output layer produces the desired result, such as classifying an image, predicting a value, or translating text.

# The learning process of a neural network involves adjusting the weights of connections between neurons. During training, the model compares its predictions with the correct answers and calculates the error. Using an optimization algorithm such as gradient descent and a technique called backpropagation, the network updates its weights to minimize the error. After many training iterations, the model becomes more accurate and can generalize to new, unseen data.

# Neural networks are widely used in various fields, including healthcare, finance, transportation, and entertainment. They power applications such as facial recognition, speech recognition, recommendation systems, autonomous vehicles, fraud detection, and medical diagnosis. Recent advances in deep learning have significantly improved the performance of neural networks, making them capable of solving highly complex tasks.

# Despite their remarkable capabilities, neural networks also have some limitations. They often require large amounts of training data, significant computational resources, and careful tuning of model parameters. Additionally, understanding how a neural network reaches a particular decision can be challenging. Nevertheless, neural networks continue to drive innovation in artificial intelligence and remain one of the most powerful tools for building intelligent systems that can learn, adapt, and perform tasks with impressive accuracy."""

splitter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)
#result=splitter.split_text(text)
result=splitter.split_documents(docs)
print(result[0].page_content)