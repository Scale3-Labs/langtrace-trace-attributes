import {LLMSpanAttributes as LLMSpanAttributesInternal} from "./models/llm_span_attributes";
import {DatabaseSpanAttributes as DatabaseSpanAttributesInternal} from "./models/database_span_attributes";
import {FrameworkSpanAttributes as FrameworkSpanAttributesInternal} from "./models/framework_span_attributes";
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

export {
  ChromaDBMethods,
  Event,
  LlamaIndexMethods,
  OpenAIMethods,
  PineconeMethods,
} from "./types";
