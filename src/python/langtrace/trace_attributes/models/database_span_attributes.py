# generated by datamodel-codegen:
#   filename:  database_span_attributes.json
#   timestamp: 2024-02-28T05:09:13+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class DatabaseSpanAttributes(BaseModel):
    langtrace_service_name: str = Field(..., alias='langtrace.service.name')
    langtrace_service_type: str = Field(..., alias='langtrace.service.type')
    langtrace_service_version: str = Field(..., alias='langtrace.service.version')
    langtrace_version: str = Field(..., alias='langtrace.version')
    server_address: Optional[str] = Field(None, alias='server.address')
    db_operation: Optional[str] = Field(None, alias='db.operation')
    db_system: str = Field(..., alias='db.system')
    db_namespace: Optional[str] = Field(None, alias='db.namespace')
    db_index: Optional[str] = Field(None, alias='db.index')
    db_collection_name: Optional[str] = Field(None, alias='db.collection.name')
    db_pinecone_top_k: Optional[float] = Field(None, alias='db.pinecone.top_k')
    db_chromadb_embedding_model: Optional[str] = Field(
        None, alias='db.chromadb.embedding_model'
    )
