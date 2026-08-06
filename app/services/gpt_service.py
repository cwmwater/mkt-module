import os
import json
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

DEFAULT_MODEL = "gpt-4o-mini"
_current_model = DEFAULT_MODEL

def get_current_model() -> str:
    return _current_model

def set_current_model(model_name: str) -> None:
    global _current_model
    _current_model = model_name

def request_prompt(msg: list, func: dict) -> dict:
    response = client.chat.completions.create(
        model = _current_model,
        messages = msg,
        functions = [
            func
        ],
        function_call = {"name": func["name"]}
    )

    return json.loads(response.choices[0].message.function_call.arguments)