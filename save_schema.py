import csv
import os
import json


def infer_type(value):
    """Infers the data type of a given value."""
    try:
        int(value)
        return "int"
    except ValueError:
        try:
            float(value)
            return "float"
        except ValueError:
            if value.lower() in ["true", "false"]:
                return "boolean"
            return "string"


def extract_schema(csv_filename, save_location):
    schema = {}
    csv_filename = os.path.join(save_location, csv_filename)
    with open(csv_filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        sample_data = next(reader)

        for header, value in zip(headers, sample_data):
            schema[header] = infer_type(value)

    schema_filename = f"{os.path.splitext(csv_filename)[0]}.schema.json"

    with open(schema_filename, "w") as schema_file:
        json.dump(schema, schema_file, indent=4)

    print(f"Schema saved to {schema_filename}")
