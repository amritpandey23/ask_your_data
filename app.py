import os
import uuid
from clean import clean_csv
from save_schema import extract_schema
from prompt import create_prompt
from model import generate_response
from extract_code import extract_code_blocks
from execute import execute_code_in_dir
from results import create_index_html

DATA_FILE = "test_data.csv"
USER_QUESTION = (
    "- How many people have salary more than 40000\n"
    "- How many people are employed with salary more than 20000"
)


def setup_directory():
    dir_name = str(uuid.uuid4())[:8]
    os.makedirs(dir_name)
    return dir_name


def file_path(directory, filename):
    return os.path.join(directory, filename)


def main():
    directory_name = setup_directory()

    clean_csv(DATA_FILE, directory_name)

    cleaned_data_file = file_path(directory_name, "test_data_cleaned.csv")
    extract_schema(cleaned_data_file, save_location=directory_name)

    schema_file = file_path(directory_name, "test_data_cleaned.schema.json")
    with open(schema_file, "r") as file:
        schema = file.read()

    prompt = create_prompt(
        DATA_FILE, schema=schema, questions=USER_QUESTION, results_dir=directory_name
    )

    response = generate_response(prompt)
    output_file = file_path(directory_name, "output.md")
    with open(output_file, "w") as file:
        file.write(response)

    extract_code_blocks(output_file, directory_name)
    execute_code_in_dir(directory_name)

    create_index_html(directory_name)

    return directory_name


if __name__ == "__main__":
    main()
