export enum Event {
  STREAM_START = "stream.start",
  STREAM_OUTPUT = "stream.output",
  STREAM_END = "stream.end",
  RESPONSE = "response",
}

export enum OpenAIMethods {
  CHAT_COMPLETION = "openai.chat.completions.create",
  IMAGES_GENERATION = "openai.images.generate",
  IMAGES_EDIT = "openai.images.edit",
  EMBEDDINGS_CREATE = "openai.embeddings.create",
}

export enum ChromaDBMethods {
  ADD = "chromadb.collection.add",
  QUERY = "chromadb.collection.query",
  DELETE = "chromadb.collection.delete",
  PEEK = "chromadb.collection.peek",
  UPDATE = "chromadb.collection.update",
  MODIFY = "chromadb.collection.modify",
  COUNT = "chromadb.collection.count",
}

export enum PineconeMethods {
  UPSERT = "pinecone.index.upsert",
  QUERY = "pinecone.index.query",
  DELETE_ONE = "pinecone.index.deleteOne",
  DELETE_MANY = "pinecone.index.deleteMany",
  DELETE_ALL = "pinecone.index.deleteAll",
}

export enum QdrantDBMethods {
  ADD = "qdrantdb.add",
  GET_COLLECTION = "qdrantdb.get_collection",
  GET_COLLECTIONS = "qdrantdb.get_collections",
  QUERY = "qdrantdb.query",
  QUERY_BATCH = "qdrantdb.query_batch",
  DELETE = "qdrantdb.delete",
  DISCOVER = "qdrantdb.discover",
  DISCOVER_BATCH = "qdrantdb.discover_batch",
  RECOMMEND = "qdrantdb.recommend",
  RECOMMEND_BATCH = "qdrantdb.recommend_batch",
  RETRIEVE = "qdrantdb.retrieve",
  SEARCH = "qdrantdb.search",
  SEARCH_BATCH = "qdrantdb.search_batch",
  UPSERT = "qdrantdb.upsert",
  COUNT = "qdrantdb.count",
  UPDATE_COLLECTION = "qdrantdb.update_collection",
  UPDATE_VECTORS = "qdrantdb.update_vectors",
}
