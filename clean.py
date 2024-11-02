import csv
import os


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


def clean_value(value, dtype):
    """Cleans a value based on its inferred type."""
    if dtype == "int":
        try:
            return int(value)
        except ValueError:
            return None
    elif dtype == "float":
        try:
            return float(value)
        except ValueError:
            return None
    elif dtype == "boolean":
        return value.lower() == "true"
    elif dtype == "string":
        return value.strip()
    return value


def clean_csv(csv_filename, save_location):
    cleaned_data = []

    csv_filename = os.path.join(save_location, csv_filename)

    with open(csv_filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        sample_data = next(reader)

        schema = {
            header: infer_type(value) for header, value in zip(headers, sample_data)
        }

        cleaned_data.append(headers)

        for row in [sample_data] + list(reader):  # Start from sample row
            cleaned_row = [
                clean_value(value, schema[header])
                for value, header in zip(row, headers)
            ]
            cleaned_data.append(cleaned_row)

    cleaned_filename = f"{os.path.splitext(csv_filename)[0]}_cleaned.csv"
    with open(cleaned_filename, "w", newline="") as cleaned_file:
        writer = csv.writer(cleaned_file)
        writer.writerows(cleaned_data)

    print(f"Cleaned CSV saved as {cleaned_filename}")
