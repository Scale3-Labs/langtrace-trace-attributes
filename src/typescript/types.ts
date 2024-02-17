export enum Event {
  STREAM_START = "stream.start",
  STREAM_OUTPUT = "stream.output",
  STREAM_END = "stream.end",
}

export enum LlamaIndexMethods {
  BASEEXTRACTOR_EXTRACT = "llamaindex.BaseExtractor.extract",
  SIMPLEPROMPT_CALL = "llamaindex.SimplePrompt.call",
  CHATENGINE_EXTRACT = "llamaindex.ChatEngine.chat",
  RETRIEVER_RETRIEVE = "llamaindex.Retriever.retrieve",
  QUERYENGINE_QUERY = "llamaindex.QueryEngine.query",
  BASEREADER_LOADDATA = "llamaindex.BaseReader.loadData",
}

export enum OpenAIMethods {
  CHAT_COMPLETION = "openai.chat.completion.create",
  IMAGES_GENERATION = "openai.images.generation.create",
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
