import { properties as LLMSpanAttributesObj } from '../schemas/llm_span_attributes.json';
import { properties as DatabaseSpanAttributesObj } from '../schemas/database_span_attributes.json';
import { properties as FrameworkSpanAttributesObj } from '../schemas/framework_span_attributes.json';
import { AnthropicFunctions, AnthropicFunctionNames } from './anthropic';
import { PgFunctionNames, PgFunctions } from './pg';
import { ChromadbFunctionNames, ChromadbFunctions } from './chroma';
import { CohereFunctionNames, CohereFunctions } from './cohere';
import { GroqFunctionNames, GroqFunctions } from './groq';
import { LlamaIndexFunctionNames, LlamaIndexFunctions } from './llamaindex';
import { OpenAIFunctionNames, OpenAIFunctions } from './openai';
import { PineConeFunctionNames, PineConeFunctions } from './pinecone';
import { QdrantFunctionNames, QdrantFunctions } from './qdrant';
import { WeaviateFunctionNames, WeaviateFunctions } from './weaviate';
import { TiktokenModel, TiktokenEncoding } from 'tiktoken';
import { OllamaFunctionNames, OllamaFunctions } from './ollama';
import { VercelAIFunctionNames, VercelAIFunctions } from './ai';

function getTypedKeys<T extends object>(obj: T): Array<keyof T> {
  return Object.keys(obj) as Array<keyof T>;
}

export const LLMSpanAttributeNames = getTypedKeys(LLMSpanAttributesObj);
export const DatabaseSpanAttributeNames = getTypedKeys(DatabaseSpanAttributesObj);
export const FrameworkSpanAttributeNames = getTypedKeys(FrameworkSpanAttributesObj);

export const Vendors = {
  OPENAI: 'openai',
  COHERE: 'cohere',
  ANTHROPIC: 'anthropic',
  GROQ: 'groq',
  PINECONE: 'pinecone',
  LLAMAINDEX: 'llamaindex',
  CHROMADB: 'chromadb',
  QDRANT: 'qdrant',
  WEAVIATE: 'weaviate',
  PG: 'pg',
  VERCEL: 'ai',
  OLLAMA: 'ollama'
} as const;

export enum Event {
  STREAM_START = 'stream.start',
  STREAM_OUTPUT = 'stream.output',
  STREAM_END = 'stream.end',
  RESPONSE = 'response',
  GEN_AI_COMPLETION = 'gen_ai.content.completion',
  GEN_AI_COMPLETION_CHUNK = 'gen_ai.completion.chunk',
  GEN_AI_PROMPT = 'gen_ai.content.prompt',
}
export type Vendor = typeof Vendors[keyof typeof Vendors];

interface VendorInstrumentationFunctions {
  openai: OpenAIFunctions[];
  cohere: CohereFunctions[];
  anthropic: AnthropicFunctions[];
  groq: GroqFunctions[];
  pinecone: PineConeFunctions[];
  llamaindex: LlamaIndexFunctions[];
  chromadb: ChromadbFunctions[];
  qdrant: QdrantFunctions[];
  weaviate: WeaviateFunctions[];
  pg: PgFunctions[];
  ai: VercelAIFunctions[];
  ollama: OllamaFunctions[];
}

export type VendorTracedFunctions = {
  [key in Vendor]: VendorInstrumentationFunctions[key];
}

export const TracedFunctionsByVendor: VendorTracedFunctions = {
  anthropic: AnthropicFunctionNames,
  pg: PgFunctionNames,
  chromadb: ChromadbFunctionNames,
  cohere: CohereFunctionNames,
  groq: GroqFunctionNames,
  llamaindex: LlamaIndexFunctionNames,
  openai: OpenAIFunctionNames,
  pinecone: PineConeFunctionNames,
  qdrant: QdrantFunctionNames,
  weaviate: WeaviateFunctionNames,
  ai: VercelAIFunctionNames,
  ollama: OllamaFunctionNames
} as const;

export const TIKTOKEN_MODEL_MAPPING: Record<TiktokenModel | string, TiktokenEncoding> = {
  'gpt-4': 'cl100k_base',
  'gpt-4-32k': 'cl100k_base',
  'gpt-4-0125-preview': 'cl100k_base',
  'gpt-4-1106-preview': 'cl100k_base',
  'gpt-4-1106-vision-preview': 'cl100k_base',
  'gpt-4o': 'o200k_base',
  'gpt-4o-mini': 'o200k_base',
  'gpt-4o-2024-05-13': 'o200k_base'
} as const;
