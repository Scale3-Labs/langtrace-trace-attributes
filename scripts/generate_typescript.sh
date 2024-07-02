#!/bin/bash

# Function to display usage instructions
usage() {
  echo "Usage: $0 schemas/<vendor>_span_attributes.json"
  exit 1
}

# Check for the presence of the command line argument
if [ "$#" -ne 1 ]; then
  usage
fi

# Take the schema file path from the command line arguments
schemaFilePath="$1"
schemaBaseName=$(basename "$schemaFilePath" .json)

# Define the output TypeScript file path
outputFilePath="models/${schemaBaseName}.d.ts"
outputDir=$(dirname "$outputFilePath")

(
  cd src/typescript
# Create the output directory if it doesn't exist
  mkdir -p "$outputDir"
# Compile the JSON Schema to a TypeScript interface using json-schema-to-typescript
  if ! npx json2ts -i "../../$schemaFilePath" -o "./$outputFilePath"; then
    echo "Error: Failed to generate TypeScript definition."
    cd "$originalDir"
    exit 1
  fi
)

# Copy the schemas directory to the destination, overriding if it exists
rm -rf src/typescript/schemas
cp -r schemas src/typescript/schemas

echo "TypeScript definition generated at: ${outputFilePath}"
