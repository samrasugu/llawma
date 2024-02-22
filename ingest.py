from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

DATA_PATH = "data"
DB_FAISS_PATH = "vectorstore/db_faiss"

# Create a vector database


def create_vector_db():
    # Load documents
    # loader = DirectoryLoader(DATA_PATH, PyPDFLoader())
    loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    # Split documents into sentences
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50)
    sentences = text_splitter.split_documents(documents)
    # sentences = text_splitter.create_documents([documents])

    # Create embeddings
    # embeddings = HuggingFaceEmbeddings("distilbert-base-uncased")
    embeddings = HuggingFaceEmbeddings(
        # TODO: Change the device to GPU if you have one
        model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})

    # Create vector store
    # vector_store = FAISS(DB_FAISS_PATH)
    # vector_store.create(sentences, embeddings)
    vector_db = FAISS.from_documents(sentences, embeddings)
    vector_db.save_local(DB_FAISS_PATH)


if __name__ == "__main__":
    create_vector_db()
