import os
from dotenv import load_dotenv
from tqdm import tqdm
from juris.config import KNOWLEDGE_PATH, QDRANT_HOST, QDRANT_PORT
from langchain.text_splitter import RecursiveCharacterTextSplitter
import fitz
from langchain.vectorstores import Qdrant
from langchain.embeddings import OllamaEmbeddings
from langchain.schema.document import Document
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

from juris.logging import get_logger

logger = get_logger(__name__)

client = QdrantClient(host=f"{QDRANT_HOST}", port=6333)

def split_text(pages: list[str]) -> list[str]:
	splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
	return splitter.split_text(" ".join(pages))

def extract_text(pdf_path: str) -> list[str]:
	doc = fitz.open(pdf_path)
	return [page.get_text() for page in doc]

def load_knowledge():
	collection_name = "ipc_code"

	if not client.collection_exists(collection_name):
		client.create_collection(
			collection_name=collection_name,
			vectors_config=VectorParams(size=768, distance=Distance.COSINE)
		)

	embedding_model = OllamaEmbeddings(model="nomic-embed-text")
	documents = []
	knowledgePaths = os.listdir(KNOWLEDGE_PATH)
	for i, filePath in enumerate(tqdm(knowledgePaths, desc="Starting")):
		filePath = os.path.join(KNOWLEDGE_PATH, filePath)
		if filePath.endswith(".pdf"):
			tqdm.write(f"Processing {filePath}")
			texts = split_text(extract_text(filePath))

	documents.extend([Document(page_content=txt) for txt in texts])

	qdrant = Qdrant.from_documents(
		documents=documents,
		embedding=embedding_model,
		collection_name=collection_name,
		url=f"http://{QDRANT_HOST}:{QDRANT_PORT}",
	)
