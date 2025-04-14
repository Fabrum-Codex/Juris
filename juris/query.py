from langchain_ollama import OllamaLLM
from langchain_qdrant import QdrantVectorStore
from langchain.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA

from juris.config import EMBED_MODEL, LLM_MODEL, QDRANT_HOST, QDRANT_PORT
from juris.logging import get_logger

logger = get_logger(__name__)


llm = OllamaLLM(model=LLM_MODEL)
embedding = OllamaEmbeddings(model=EMBED_MODEL)
qdrant = QdrantVectorStore.from_existing_collection(
    collection_name="ipc_code",
    url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",
    embedding=embedding
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=qdrant.as_retriever(),
    return_source_documents=True
)

def query(query: str) -> str:
	result = qa_chain.invoke(query)
	logger.info(f"[+] Query: {query}")
	return result