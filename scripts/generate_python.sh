#!/bin/bash

# Check if an argument (schema file path) is provided
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <path_to_schema_file.json>"
  exit 1
fi

SCHEMA_FILE="$1"
# Extract filename without extension, and extension
SCHEMA_FILENAME=$(basename -- "$SCHEMA_FILE")
SCHEMA_NAME="${SCHEMA_FILENAME%.*}"

# Define the output file path, using the schema name for the Python model file
OUTPUT_FILE="src/python/langtrace/trace_attributes/models/${SCHEMA_NAME}.py"

# Generate the Python model
datamodel-codegen --input "$SCHEMA_FILE" --input-file-type jsonschema --output "$OUTPUT_FILE" \
  --output-model-type pydantic_v2.BaseModel --allow-extra-fields

echo "Generated Python model at: $OUTPUT_FILE"
