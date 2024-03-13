/* eslint-disable */
/**
 * This file was automatically generated by json-schema-to-typescript.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source JSONSchema file,
 * and run json-schema-to-typescript to regenerate this file.
 */

export interface DatabaseSpanAttributes {
  "langtrace.service.name": string;
  "langtrace.service.type": string;
  "langtrace.service.version": string;
  "langtrace.version": string;
  "server.address"?: string;
  "db.operation"?: string;
  "db.system": string;
  "db.namespace"?: string;
  "db.index"?: string;
  "db.collection.name"?: string;
  "db.pinecone.top_k"?: number;
  "db.chromadb.embedding_model"?: string;
}
