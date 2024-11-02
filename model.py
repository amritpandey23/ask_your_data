import google.generativeai as genai
from dotenv import load_dotenv
import os


def generate_response(prompt):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    chat_session = model.start_chat()

    response = chat_session.send_message(prompt)
    return response.text


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
