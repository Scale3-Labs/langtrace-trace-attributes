# generated by datamodel-codegen:
#   filename:  llm_span_attributes.json
#   timestamp: 2024-07-10T15:09:12+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, ConfigDict, Field


class LLMSpanAttributes(BaseModel):
    model_config = ConfigDict(extra="allow")


    langtrace_service_name: str = Field(
        ...,
        alias='langtrace.service.name',
        description='Name of the service. Includes all supported service providers by langtrace',
    )
    langtrace_service_type: str = Field(
        ...,
        alias='langtrace.service.type',
        description='Type of the service. Allowed values: [llm, vectordb, framework]',
    )
    langtrace_service_version: Optional[str] = Field(
        None,
        alias='langtrace.service.version',
        description='Version of the service provider client',
    )
    langtrace_version: str = Field(..., alias='langtrace.version')
    langtrace_sdk_name: str = Field(..., alias='langtrace.sdk.name')
    url_full: str = Field(..., alias='url.full', description='Full URL of the request')
    url_path: str = Field(..., alias='url.path', description='Path of the request')
    gen_ai_request_model: Optional[str] = Field(
        None,
        alias='gen_ai.request.model',
        description='Model name from the input request',
    )
    gen_ai_response_model: Optional[str] = Field(
        None, alias='gen_ai.response.model', description='Model name from the response'
    )
    gen_ai_request_temperature: Optional[float] = Field(
        None,
        alias='gen_ai.request.temperature',
        description='Temperature value from the input request',
    )
    gen_ai_request_logit_bias: Optional[str] = Field(
        None,
        alias='gen_ai.request.logit_bias',
        description='Likelihood bias of the specified tokens the input request.',
    )
    gen_ai_request_logprobs: Optional[bool] = Field(
        None,
        alias='gen_ai.request.logprobs',
        description='Logprobs flag returns log probabilities.',
    )
    gen_ai_request_top_logprobs: Optional[float] = Field(
        None,
        alias='gen_ai.request.top_logprobs',
        description='Integer between 0 and 5 specifying the number of most likely tokens to return.',
    )
    gen_ai_request_top_p: Optional[float] = Field(
        None,
        alias='gen_ai.request.top_p',
        description='Top P value from the input request',
    )
    gen_ai_request_top_k: Optional[float] = Field(
        None,
        alias='gen_ai.request.top_k',
        description='Top K results to return from the input request',
    )
    gen_ai_user: Optional[str] = Field(
        None, alias='gen_ai.user', description='User ID from the input request'
    )
    gen_ai_prompt: Optional[str] = Field(
        None, alias='gen_ai.prompt', description='Prompt text from the input request'
    )
    gen_ai_completion: Optional[str] = Field(
        None,
        alias='gen_ai.completion',
        description='Completion text from the response. This will be an array of json objects with the following format {"role": "", "content": ""}. Role can be one of the following values: [system, user, assistant, tool]',
    )
    gen_ai_request_stream: Optional[bool] = Field(
        None,
        alias='gen_ai.request.stream',
        description='Stream flag from the input request',
    )
    gen_ai_request_encoding_formats: Optional[List[str]] = Field(
        None,
        alias='gen_ai.request.encoding_formats',
        description="Encoding formats from the input request. Allowed values: ['float', 'int8','uint8', 'binary', 'ubinary', 'base64']",
    )
    gen_ai_request_dimensions: Optional[float] = Field(
        None,
        alias='gen_ai.request.dimensions',
        description='Dimensions from the input request',
    )
    gen_ai_response_id: Optional[str] = Field(
        None,
        alias='gen_ai.response_id',
        description='Response ID from the output response',
    )
    gen_ai_response_finish_reasons: Optional[List[str]] = Field(
        None,
        alias='gen_ai.response.finish_reasons',
        description='Array of reasons the model stopped generating tokens, corresponding to each generation received',
    )
    gen_ai_system_fingerprint: Optional[str] = Field(
        None,
        alias='gen_ai.system_fingerprint',
        description='System fingerprint of the system that generated the response',
    )
    gen_ai_request_documents: Optional[str] = Field(
        None,
        alias='gen_ai.request.documents',
        description='Array of documents from the input request json stringified',
    )
    gen_ai_request_is_search_required: Optional[bool] = Field(
        None,
        alias='gen_ai.request.is_search_required',
        description='Search flag from the input request',
    )
    gen_ai_request_tool_choice: Optional[str] = Field(
        None,
        alias='gen_ai.request.tool_choice',
        description='Tool choice from the input request',
    )
    gen_ai_response_tool_calls: Optional[str] = Field(
        None,
        alias='gen_ai.response.tool_calls',
        description='Array of tool calls from the response json stringified',
    )
    gen_ai_request_max_tokens: Optional[float] = Field(
        None,
        alias='gen_ai.request.max_tokens',
        description='The maximum number of tokens the LLM generates for a request.',
    )
    gen_ai_usage_prompt_tokens: Optional[float] = Field(
        None,
        alias='gen_ai.usage.prompt_tokens',
        description='The number of tokens used in the llm prompt.',
    )
    gen_ai_usage_total_tokens: Optional[float] = Field(
        None,
        alias='gen_ai.usage.total_tokens',
        description='The total number of tokens used in the llm request.',
    )
    gen_ai_usage_completion_tokens: Optional[float] = Field(
        None,
        alias='gen_ai.usage.completion_tokens',
        description='The number of tokens in the llm response.',
    )
    gen_ai_usage_search_units: Optional[float] = Field(
        None,
        alias='gen_ai.usage.search_units',
        description='The number of search units used in the request.',
    )
    gen_ai_request_seed: Optional[str] = Field(
        None, alias='gen_ai.request.seed', description='Seed from the input request'
    )
    gen_ai_request_frequency_penalty: Optional[float] = Field(
        None,
        alias='gen_ai.request.frequency_penalty',
        description='Frequency penalty from the input request',
    )
    gen_ai_request_presence_penalty: Optional[float] = Field(
        None,
        alias='gen_ai.request.presence_penalty',
        description='Presence penalty from the input request',
    )
    gen_ai_request_connectors: Optional[str] = Field(
        None,
        alias='gen_ai.request.connectors',
        description='An array of connectors from the input request json stringified',
    )
    gen_ai_request_tools: Optional[str] = Field(
        None,
        alias='gen_ai.request.tools',
        description='An array of tools from the input request json stringified',
    )
    gen_ai_request_tool_results: Optional[str] = Field(
        None,
        alias='gen_ai.request.tool_results',
        description='An array of tool results from the input request json stringified',
    )
    gen_ai_request_embedding_inputs: Optional[str] = Field(
        None,
        alias='gen_ai.request.embedding_inputs',
        description='An array of embedding inputs from the input request json stringified',
    )
    gen_ai_request_embedding_dataset_id: Optional[str] = Field(
        None,
        alias='gen_ai.request.embedding_dataset_id',
        description='Embedding dataset ID from the input request',
    )
    gen_ai_request_embedding_input_type: Optional[str] = Field(
        None,
        alias='gen_ai.request.embedding_input_type',
        description="Embedding input type from the input request. Allowed values: [ 'search_document', 'search_query', 'classification', 'clustering']",
    )
    gen_ai_request_embedding_job_name: Optional[str] = Field(
        None,
        alias='gen_ai.request.embedding_job_name',
        description='Embedding job name from the input request',
    )
    gen_ai_image_size: Optional[str] = Field(
        None,
        alias='gen_ai.image.size',
        description="Image size from the input request. Allowed values: ['256x256', '512x512', '1024x1024']",
    )
    gen_ai_request_response_format: Optional[str] = Field(
        None,
        alias='gen_ai.request.response_format',
        description="Response format from the input request. Allowed values: ['url', 'b64_json']",
    )
    http_max_retries: Optional[int] = Field(None, alias='http.max.retries')
    http_timeout: Optional[int] = Field(None, alias='http.timeout')
    gen_ai_cohere_rerank_query: Optional[str] = Field(
        None,
        alias='gen_ai.cohere.rerank.query',
        description='Query from the input request for the rerank api',
    )
    gen_ai_cohere_rerank_results: Optional[str] = Field(
        None,
        alias='gen_ai.cohere.rerank.results',
        description='Results from the rerank api',
    )
