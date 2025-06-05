from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

from pathlib import Path

def build_index():
    docs_path = Path("data")
    documents = SimpleDirectoryReader(str(docs_path)).load_data()

    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir="storage")

if __name__ == "__main__":
    build_index()
