# generated by datamodel-codegen:
#   filename:  framework_span_attributes.json
#   timestamp: 2024-05-23T16:57:21+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class FrameworkSpanAttributes(BaseModel):
    model_config = ConfigDict(extra="allow")

    langtrace_service_name: str = Field(..., alias="langtrace.service.name")
    langtrace_service_type: str = Field(..., alias="langtrace.service.type")
    langtrace_service_version: Optional[str] = Field(
        None, alias="langtrace.service.version"
    )
    langtrace_sdk_name: str = Field(..., alias="langtrace.sdk.name")
    langtrace_version: str = Field(..., alias="langtrace.version")
    langchain_task_name: Optional[str] = Field(None, alias="langchain.task.name")
    langchain_inputs: Optional[str] = Field(None, alias="langchain.inputs")
    langchain_outputs: Optional[str] = Field(None, alias="langchain.outputs")
    langgraph_entrypoint: Optional[str] = Field(None, alias="langgraph.entrypoint")
    langgraph_node: Optional[str] = Field(None, alias="langgraph.node")
    langgraph_edge: Optional[str] = Field(None, alias="langgraph.edge")
    langgraph_finishpoint: Optional[str] = Field(None, alias="langgraph.finishpoint")
    langgraph_task_name: Optional[str] = Field(None, alias="langgraph.task.name")
    llamaindex_task_name: Optional[str] = Field(None, alias="llamaindex.task.name")
    llamaindex_inputs: Optional[str] = Field(None, alias="llamaindex.inputs")
    llamaindex_outputs: Optional[str] = Field(None, alias="llamaindex.outputs")
    langtrace_testId: Optional[str] = Field(None, alias="langtrace.testId")
    dspy_optimizer: Optional[str] = Field(None, alias="dspy.optimizer")
    dspy_optimizer_module: Optional[str] = Field(None, alias="dspy.optimizer.module")
    dspy_optimizer_module_prog: Optional[str] = Field(
        None, alias="dspy.optimizer.module.prog"
    )
    dspy_optimizer_metric: Optional[str] = Field(None, alias="dspy.optimizer.metric")
    dspy_optimizer_trainset: Optional[str] = Field(
        None, alias="dspy.optimizer.trainset"
    )
    dspy_optimizer_config: Optional[str] = Field(None, alias="dspy.optimizer.config")
    dspy_signature_name: Optional[str] = Field(None, alias="dspy.signature.name")
    dspy_signature: Optional[str] = Field(None, alias="dspy.signature")
    dspy_signature_args: Optional[str] = Field(None, alias="dspy.signature.args")
    dspy_signature_result: Optional[str] = Field(None, alias="dspy.signature.result")
    dspy_evaluate_devset: Optional[str] = Field(None, alias="dspy.evaluate.devset")
    dspy_evaluate_display: Optional[str] = Field(None, alias="dspy.evaluate.display")
    dspy_evaluate_num_threads: Optional[str] = Field(
        None, alias="dspy.evaluate.num_threads"
    )
    dspy_evaluate_return_outputs: Optional[str] = Field(
        None, alias="dspy.evaluate.return_outputs"
    )
    dspy_evaluate_display_table: Optional[str] = Field(
        None, alias="dspy.evaluate.display_table"
    )
    dspy_evaluate_display_progress: Optional[str] = Field(
        None, alias="dspy.evaluate.display_progress"
    )
    dspy_evaluate_metric: Optional[str] = Field(None, alias="dspy.evaluate.metric")
    dspy_evaluate_error_count: Optional[str] = Field(
        None, alias="dspy.evaluate.error_count"
    )
    dspy_evaluate_error_lock: Optional[str] = Field(
        None, alias="dspy.evaluate.error_lock"
    )
    dspy_evaluate_max_errors: Optional[str] = Field(
        None, alias="dspy.evaluate.max_errors"
    )
    dspy_evaluate_args: Optional[str] = Field(None, alias="dspy.evaluate.args")
    dspy_evaluate_result: Optional[str] = Field(None, alias="dspy.evaluate.result")
