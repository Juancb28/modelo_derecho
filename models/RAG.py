from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

model_name = os.environ.get('HUGGINGFACE_MODEL', 'sentence-transformers/all-MiniLM-L6-v2')
embeddings = HuggingFaceEmbeddings(model_name=model_name)

client = QdrantClient(
    url=os.environ.get('Cluster_Endpoint'),
    api_key=os.environ.get('QDRANT_CLOUD')
)

vector_store=QdrantVectorStore(
    client=client,
    collection_name='codigo_civil',
    embedding=embeddings
)

llm = ChatGroq(model='llama-3.3-70b-versatile', temperature=0)
retriever = vector_store.as_retriever(search_kwargs={'k':3})

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=retriever,
    return_source_documents=True
)