import { properties as LLMSpanAttributesObj  } from './schemas/llm_span_attributes.json'
import { properties as DatabaseSpanAttributesObj } from  './schemas/database_span_attributes.json'
import { properties as FrameworkSpanAttributesObj } from './schemas/framework_span_attributes.json'


export const LLMSpanAttributeNames: Array<keyof typeof LLMSpanAttributesObj> = Object.keys(LLMSpanAttributesObj) as Array<keyof typeof LLMSpanAttributesObj>
export const DatabaseSpanAttributeNames: Array<keyof typeof DatabaseSpanAttributesObj> = Object.keys(DatabaseSpanAttributesObj) as Array<keyof typeof DatabaseSpanAttributesObj>
export const FrameworkSpanAttributeNames: Array<keyof typeof FrameworkSpanAttributesObj> = Object.keys(FrameworkSpanAttributesObj) as Array<keyof typeof FrameworkSpanAttributesObj>