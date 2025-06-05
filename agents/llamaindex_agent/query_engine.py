from llama_index.core import StorageContext, load_index_from_storage

def query_index(question: str):
    storage_context = StorageContext.from_defaults(persist_dir="storage")
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()

    response = query_engine.query(question)

    return str(response)
