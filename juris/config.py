import os
from dotenv import load_dotenv

load_dotenv()

QDRANT_HOST = os.environ.get("QDRANT_HOST", "localhost")
QDRANT_PORT = os.environ.get("QDRANT_PORT", "6333")
OLLAMA_BASE = os.environ.get("OLLAMA_BASE", "http://localhost:11434")
KNOWLEDGE_PATH = os.environ.get("KNOWLEDGE_PATH", "data/knowledge")