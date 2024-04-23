/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

export interface LLMSpanAttributes {
  "langtrace.service.name": string;
  "langtrace.service.type": string;
  "langtrace.service.version"?: string;
  "langtrace.version": string;
  "langtrace.sdk.name": string;
  "url.full": string;
  "llm.api": string;
  "llm.model"?: string;
  "llm.temperature"?: number;
  "llm.top_p"?: number;
  "llm.top_k"?: number;
  "llm.user"?: string;
  "llm.system.fingerprint"?: string;
  "llm.prompts"?: string;
  "llm.function.prompts"?: string;
  "llm.responses"?: string;
  "llm.token.counts"?: string;
  "llm.stream"?: boolean;
  "llm.encoding.format"?: string;
  "llm.dimensions"?: string;
  "llm.generation_id"?: string;
  "llm.response_id"?: string;
  "llm.citations"?: string;
  "llm.documents"?: string;
  "llm.is_search_required"?: boolean;
  "llm.search_results"?: string;
  "llm.tool_calls"?: string;
  "llm.max_tokens"?: string;
  "llm.max_input_tokens"?: string;
  "llm.conversation_id"?: string;
  "llm.seed"?: string;
  "llm.frequency_penalty"?: string;
  "llm.presence_penalty"?: string;
  "llm.connectors"?: string;
  "llm.tools"?: string;
  "llm.tool_results"?: string;
  "llm.embedding_dataset_id"?: string;
  "llm.embedding_input_type"?: string;
  "llm.embedding_job_name"?: string;
  "llm.retrieval.query"?: string;
  "llm.retrieval.results"?: string;
  "user.id"?: string;
  "user.feedback.rating"?: number;
  "http.max.retries"?: number;
  "http.timeout"?: number;
  "langtrace.testId"?: string;
}
