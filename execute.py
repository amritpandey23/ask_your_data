import os
import subprocess


def execute_code_in_dir(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            print(f"Executing: {file_path}")

            subprocess.run(["python", file_path], check=True)
