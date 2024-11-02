import os
import uuid
from subprocess import CalledProcessError
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    send_from_directory,
    Response,
)
from werkzeug.utils import secure_filename

from clean import clean_csv
from save_schema import extract_schema
from prompt import create_prompt
from model import generate_response
from extract_code import extract_code_blocks
from execute import execute_code_in_dir
from results import create_index_html

app = Flask(__name__)


def setup_directory():
    dir_name = str(uuid.uuid4())[:8]
    full_path = os.path.join(os.getcwd(), dir_name)
    os.makedirs(full_path, exist_ok=True)
    return dir_name, full_path


def process_file(directory_name, user_question):

    clean_csv("sample_data.csv", directory_name)

    extract_schema("sample_data_cleaned.csv", save_location=directory_name)

    schema_file = os.path.join(directory_name, "sample_data_cleaned.schema.json")
    with open(schema_file, "r") as file:
        schema = file.read()

    prompt = create_prompt(
        "sample_data_cleaned.csv",
        schema=schema,
        questions=user_question,
        results_dir=directory_name,
    )
    response = generate_response(prompt)

    output_file = os.path.join(directory_name, "output.md")
    with open(output_file, "w") as file:
        file.write(response)

    extract_code_blocks("output.md", directory_name)

    try:
        execute_code_in_dir(directory_name)
    except CalledProcessError as e:
        print(e)

    create_index_html(directory_name)

    return directory_name


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(url_for("upload_file"))
        file = request.files["file"]
        user_question = request.form.get("user_question")

        if file.filename == "" or not user_question:
            return redirect(url_for("upload_file"))

        if file:
            dir_name, _ = setup_directory()

            sample_data_path = os.path.join(dir_name, "sample_data.csv")

            file.save(sample_data_path)

            process_file(dir_name, user_question)

            return redirect(url_for("result", directory=dir_name))

    return render_template("home.html")


@app.route("/result/<directory>")
def result(directory):
    result_path = os.path.join(directory, "index.html")

    try:
        with open(result_path, "r") as file:
            html_content = file.read()

        return Response(html_content, mimetype="text/html")

    except FileNotFoundError:
        return f"<h1>index.html not found in {directory}</h1>", 404


@app.route("/<directory>/<filename>")
def download_file(directory, filename):
    return send_from_directory(os.path.join(os.getcwd(), directory), filename)


if __name__ == "__main__":
    app.run(debug=True)
