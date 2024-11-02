import re
import os

language_extensions = {
    "python": "py",
    "py": "py",
    "java": "java",
    "javascript": "js",
    "js": "js",
    "c++": "cpp",
    "cpp": "cpp",
    "c": "c",
    "html": "html",
    "css": "css",
    "php": "php",
    "ruby": "rb",
    "rb": "rb",
    "sh": "sh",
    "shell": "sh",
    "go": "go",
    "rust": "rs",
}


def extract_code_blocks(markdown_file, save_location):
    markdown_file = os.path.join(save_location, markdown_file)
    with open(markdown_file, "r") as file:
        content = file.read()

    code_block_pattern = re.compile(r"```(\w+)?\n(.*?)```", re.DOTALL)

    code_count = {}

    for match in code_block_pattern.finditer(content):
        language = match.group(1).lower() if match.group(1) else "txt"
        code = match.group(2).strip()

        extension = language_extensions.get(language, "txt")

        if extension in code_count:
            code_count[extension] += 1
        else:
            code_count[extension] = 1

        filename = f"code{code_count[extension]}.{extension}"

        with open(save_location + "/" + filename, "w") as code_file:
            code_file.write(code)

        print(f"Saved: {filename}")
