import {LLMSpanAttributes as LLMSpanAttributesInternal} from "./models/llm_span_attributes";
import {DatabaseSpanAttributes as DatabaseSpanAttributesInternal} from "./models/database_span_attributes";
import {FrameworkSpanAttributes as FrameworkSpanAttributesInternal} from "./models/framework_span_attributes";
import { LLMSpanAttributeNames, DatabaseSpanAttributeNames, FrameworkSpanAttributeNames, Vendor, Event, TracedFunctionsByVendor, Vendors } from "./constants/common";
import { APIS as AnthropicAPIS } from "./constants/anthropic";
import { APIS as PgAPIS } from "./constants/pg";
import { APIS as ChromadbAPIS } from "./constants/chroma";
import { APIS as CohereAPIS } from "./constants/cohere";
import { APIS as GroqAPIS } from "./constants/groq";
import { APIS as LlamaIndexAPIS } from "./constants/llamaindex";
import { APIS as OpenAIAPIs } from "./constants/openai";
import { APIS as PineConeAPIS } from "./constants/pinecone";
import { APIS as QdrantAPIS } from "./constants/qdrant";
import { APIS as vercelAIAPIS } from "./constants/ai";
import { APIS as ollamaAPIS } from "./constants/ollama";
import { queryTypeToFunctionToProps } from "./constants/weaviate";
import { TIKTOKEN_MODEL_MAPPING } from "./constants/common";

/** Opentelemetry span attributes */

/**
 * Attributes is a map from string to attribute values.
 *
 * Note: only the own enumerable keys are counted as valid attribute keys.
 */
export interface Attributes {
  [attributeKey: string]: AttributeValue | undefined;
}
/**
* Attribute values may be any non-nullish primitive value except an object.
*
* null or undefined attribute values are invalid and will result in undefined behavior.
*/
export declare type AttributeValue = string | number | boolean | Array<null | undefined | string> | Array<null | undefined | number> | Array<null | undefined | boolean>;

export type LLMSpanAttributes = Attributes & ( LLMSpanAttributesInternal);
export type DatabaseSpanAttributes = Attributes & ( DatabaseSpanAttributesInternal);
export type FrameworkSpanAttributes = Attributes & ( FrameworkSpanAttributesInternal);

const APIS = {
  anthropic: AnthropicAPIS,
  pg: PgAPIS,
  chromadb: ChromadbAPIS,
  cohere: CohereAPIS,
  groq: GroqAPIS,
  llamaindex: LlamaIndexAPIS,
  openai: OpenAIAPIs,
  pinecone: PineConeAPIS,
  qdrant: QdrantAPIS,
  ai: vercelAIAPIS,
  ollama: ollamaAPIS
}
export {
  LLMSpanAttributeNames,
  DatabaseSpanAttributeNames,
  FrameworkSpanAttributeNames,
  Vendor,
  Event,
  TracedFunctionsByVendor,
  Vendors
}

export {
  APIS,
  TIKTOKEN_MODEL_MAPPING,
  queryTypeToFunctionToProps
}