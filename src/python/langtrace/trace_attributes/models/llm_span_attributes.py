# generated by datamodel-codegen:
#   filename:  llm_span_attributes.json
#   timestamp: 2024-06-06T05:12:56+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class LLMSpanAttributes(BaseModel):
    model_config = ConfigDict(extra="allow")

    langtrace_service_name: str = Field(..., alias="langtrace.service.name")
    langtrace_service_type: str = Field(..., alias="langtrace.service.type")
    langtrace_service_version: Optional[str] = Field(
        None, alias="langtrace.service.version"
    )
    langtrace_version: str = Field(..., alias="langtrace.version")
    langtrace_sdk_name: str = Field(..., alias="langtrace.sdk.name")
    url_full: str = Field(..., alias="url.full")
    llm_api: str = Field(..., alias="llm.api")
    llm_model: Optional[str] = Field(None, alias="llm.model")
    llm_temperature: Optional[float] = Field(None, alias="llm.temperature")
    llm_top_p: Optional[float] = Field(None, alias="llm.top_p")
    llm_top_k: Optional[float] = Field(None, alias="llm.top_k")
    llm_user: Optional[str] = Field(None, alias="llm.user")
    llm_system_fingerprint: Optional[str] = Field(None, alias="llm.system.fingerprint")
    llm_prompts: Optional[str] = Field(None, alias="llm.prompts")
    llm_responses: Optional[str] = Field(None, alias="llm.responses")
    llm_token_counts: Optional[str] = Field(None, alias="llm.token.counts")
    llm_stream: Optional[bool] = Field(None, alias="llm.stream")
    llm_encoding_formats: Optional[str] = Field(None, alias="llm.encoding.formats")
    llm_dimensions: Optional[str] = Field(None, alias="llm.dimensions")
    llm_generation_id: Optional[str] = Field(None, alias="llm.generation_id")
    llm_response_id: Optional[str] = Field(None, alias="llm.response_id")
    llm_citations: Optional[str] = Field(None, alias="llm.citations")
    llm_documents: Optional[str] = Field(None, alias="llm.documents")
    llm_is_search_required: Optional[bool] = Field(None, alias="llm.is_search_required")
    llm_search_results: Optional[str] = Field(None, alias="llm.search_results")
    llm_tool_calls: Optional[str] = Field(None, alias="llm.tool_calls")
    llm_max_tokens: Optional[str] = Field(None, alias="llm.max_tokens")
    llm_max_input_tokens: Optional[str] = Field(None, alias="llm.max_input_tokens")
    llm_conversation_id: Optional[str] = Field(None, alias="llm.conversation_id")
    llm_seed: Optional[str] = Field(None, alias="llm.seed")
    llm_frequency_penalty: Optional[str] = Field(None, alias="llm.frequency_penalty")
    llm_presence_penalty: Optional[str] = Field(None, alias="llm.presence_penalty")
    llm_connectors: Optional[str] = Field(None, alias="llm.connectors")
    llm_tools: Optional[str] = Field(None, alias="llm.tools")
    llm_tool_results: Optional[str] = Field(None, alias="llm.tool_results")
    llm_embedding_inputs: Optional[str] = Field(None, alias="llm.embedding_inputs")
    llm_embedding_dataset_id: Optional[str] = Field(
        None, alias="llm.embedding_dataset_id"
    )
    llm_embedding_input_type: Optional[str] = Field(
        None, alias="llm.embedding_input_type"
    )
    llm_embedding_job_name: Optional[str] = Field(None, alias="llm.embedding_job_name")
    llm_retrieval_query: Optional[str] = Field(None, alias="llm.retrieval.query")
    llm_retrieval_results: Optional[str] = Field(None, alias="llm.retrieval.results")
    llm_image_size: Optional[str] = Field(None, alias="llm.image.size")
    llm_response_format: Optional[str] = Field(None, alias="llm.response_format")
    http_max_retries: Optional[int] = Field(None, alias="http.max.retries")
    http_timeout: Optional[int] = Field(None, alias="http.timeout")
    langtrace_testId: Optional[str] = Field(None, alias="langtrace.testId")
