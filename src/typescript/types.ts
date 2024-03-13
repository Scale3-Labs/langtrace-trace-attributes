export enum Event {
  STREAM_START = "stream.start",
  STREAM_OUTPUT = "stream.output",
  STREAM_END = "stream.end",
}

export enum OpenAIMethods {
  CHAT_COMPLETION = "openai.chat.completions.create",
  IMAGES_GENERATION = "openai.images.generate",
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
