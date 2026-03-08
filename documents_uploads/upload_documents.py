import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client import QdrantClient
from langchain_qdrant import QdrantVectorStore
from qdrant_client.http import models
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("documents/Documento_Código Civil_0.pdf")
paginas = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=1000)

chunks = text_splitter.split_documents(paginas)

# print(len(chunks))

embeddings = HuggingFaceEmbeddings(
    model_name=os.environ.get(
        "HUGGINGFACE_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )
)

url_cloud=os.environ.get("Cluster_Endpoint")
api_key=os.environ.get("QDRANT_CLOUD")

client = QdrantClient(
    url=os.environ.get("Cluster_Endpoint"),
    api_key=os.environ.get("QDRANT_CLOUD"),
)



vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings,
    url=url_cloud,
    api_key=api_key,
    collection_name="codigo_civil",
    force_recreate=True
)

print("Done!")
