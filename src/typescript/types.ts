export enum Event {
  STREAM_START = "stream.start",
  STREAM_OUTPUT = "stream.output",
  STREAM_END = "stream.end",
}

export enum LlamaIndexMethods {
  TASK_LLAMAINDEX_BASEEXTRACTOR_EXTRACT = "task.llamaindex.BaseExtractor.extract",
  TASK_LLAMAINDEX_SIMPLEPROMPT_CALL = "task.llamaindex.SimplePrompt.call",
  TASK_LLAMAINDEX_CHATENGINE_EXTRACT = "task.llamaindex.ChatEngine.chat",
  TASK_LLAMAINDEX_RETRIEVER_RETRIEVE = "task.llamaindex.Retriever.retrieve",
  TASK_LLAMAINDEX_QUERYENGINE_QUERY = "task.llamaindex.QueryEngine.query",
}
