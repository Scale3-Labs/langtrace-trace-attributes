# generated by datamodel-codegen:
#   filename:  llm_span_attributes.json
#   timestamp: 2024-03-26T23:35:48+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator


class UserFeedbackRating(Enum):
    integer_1 = 1
    integer__1 = -1


class LLMSpanAttributes(BaseModel):
    class Config:
        extra = Extra.forbid

    langtrace_service_name: str = Field(..., alias='langtrace.service.name')
    langtrace_service_type: str = Field(..., alias='langtrace.service.type')
    langtrace_service_version: str = Field(..., alias='langtrace.service.version')
    langtrace_version: str = Field(..., alias='langtrace.version')
    url_full: str = Field(..., alias='url.full')
    llm_api: str = Field(..., alias='llm.api')
    llm_model: Optional[str] = Field(None, alias='llm.model')
    llm_temperature: Optional[float] = Field(None, alias='llm.temperature')
    llm_top_p: Optional[float] = Field(None, alias='llm.top_p')
    llm_top_k: Optional[float] = Field(None, alias='llm.top_k')
    llm_user: Optional[str] = Field(None, alias='llm.user')
    llm_system_fingerprint: Optional[str] = Field(None, alias='llm.system.fingerprint')
    llm_prompts: str = Field(..., alias='llm.prompts')
    llm_function_prompts: Optional[str] = Field(None, alias='llm.function.prompts')
    llm_responses: Optional[str] = Field(None, alias='llm.responses')
    llm_token_counts: Optional[str] = Field(None, alias='llm.token.counts')
    llm_stream: Optional[bool] = Field(None, alias='llm.stream')
    llm_encoding_format: Optional[str] = Field(None, alias='llm.encoding.format')
    llm_dimensions: Optional[str] = Field(None, alias='llm.dimensions')
    user_id: Optional[str] = Field(None, alias='user.id')
    user_feedback_rating: Optional[int] = Field(
        None, alias='user.feedback.rating'
    )
    http_max_retries: Optional[int] = Field(None, alias='http.max.retries')
    http_timeout: Optional[int] = Field(None, alias='http.timeout')

    @validator('user_feedback_rating')
    def check_rating_values(cls, value):
        if value not in {1, -1}:
            raise ValueError('Rating must be 1 or -1')
        return value
