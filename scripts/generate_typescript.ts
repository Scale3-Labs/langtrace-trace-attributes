// Modified convertSchemaToInterface.ts
import * as fs from "fs";
import * as TJS from "json-schema-to-typescript";
import * as path from "path";

// Check for the presence of the command line argument
if (process.argv.length < 3) {
  console.log(
    "Usage: ts-node scripts/schema_to_interface.ts schemas/<vendor>_span_attributes.json"
  );
  process.exit(1);
}

// Take the schema file path from the command line arguments
const schemaFilePath = process.argv[2];
const schemaBaseName = path.basename(
  schemaFilePath,
  path.extname(schemaFilePath)
);

// Define the output TypeScript file path
const outputFilePath = path.join(
  "src/typescript/models",
  `${schemaBaseName}.d.ts`
);

// Read and parse the JSON Schema
const schema = JSON.parse(fs.readFileSync(schemaFilePath, "utf8"));

// Compile the JSON Schema to a TypeScript interface
TJS.compile(schema, schemaBaseName)
  .then((ts) => fs.writeFileSync(outputFilePath, ts))
  .catch((error) => console.error(error));

console.log(`TypeScript definition generated at: ${outputFilePath}`);
