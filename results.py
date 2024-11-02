import os


def create_index_html(directory):
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Results</title>
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        h1 {
            text-align: center;
            margin-top: 20px;
            color: #333;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 10px;
        }
        .gallery-item {
            margin: 15px;
            border: 2px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transition: transform 0.3s ease;
            width: 600px;
            text-align: center;
            background-color: #fff;
        }
        .gallery-item img {
            width: 100%;
            height: auto;
            display: block;
        }
        .gallery-item:hover {
            transform: scale(1.05);
        }
        .image-caption {
            padding: 10px;
            font-size: 16px;
            color: #555;
        }
    </style>
</head>
<body>
    <h1>Results</h1>
    <div class="gallery">
    """

    for filename in os.listdir(os.path.join(directory)):
        if filename.endswith(".png"):
            html_content += f"""
        <div class="gallery-item">
            <img src="/{directory}/{filename}" alt="{filename}">
        </div>
        """

    html_content += """
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
</body>
</html>
"""

    index_path = os.path.join(directory, "index.html")
    with open(index_path, "w") as file:
        file.write(html_content)

    print(f"index.html created at {index_path}")
