# Juris 🏛️
**Legal Assistant using RAG (Retrieval-Augmented Generation)**  
Powered by [Ollama](https://ollama.com), [Qdrant](https://qdrant.tech), and Python.  
Built to assist with legal queries using locally stored documents and advanced LLM capabilities.

---

## ⚙️ Tech Stack

- **Ollama** – Local Large Language Models  
- **Qdrant** – Vector Database for semantic search  
- **Python** – Backend logic and orchestration

---

## 🚀 Setup

To get started with Juris, use the provided setup in [Fabrum Codex - OllamaLocal](https://github.com/Fabrum-Codex/OllamaLocal).

1. Clone the repo:

```bash
git clone https://github.com/Fabrum-Codex/OllamaLocal.git
cd OllamaLocal
```

2. Spin up the environment using Docker Compose:

```bash
docker compose up
```

This will start **Ollama** and **Qdrant** services.

---

## 📚 Knowledge

To load legal knowledge into the database:

1. Place your **PDF files only** inside the following folder:

```
data/knowledge/
```

2. Run the following command to load them into Qdrant:

```bash
python -m juris --load
```

This command will automatically enumerate through all PDF files in the `data/knowledge/` directory and index them into the vector database.

---

## ❓ Query

To ask a question to the legal assistant:

```bash
python -m juris --query "<your query here>"
```

You’ll receive a generated answer based on the indexed legal documents.

---

## 🧠 Example

```bash
python -m juris --query "What is the punishment for theft under Indian Penal Code?"
```

---

## 📂 Project Structure (Relevant Paths)

```
📁 data/
   └── 📁 knowledge/      # Place your legal PDF documents here
```

---

## 👨‍💻 Maintained by

**Fabrum Codex**  
> "Crafting intelligent systems, one codex at a time."
