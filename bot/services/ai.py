"""
Интеграция с OpenAI GPT-4
"""

import openai
from bot.config import OPENAI_API_KEY


def get_ai_response(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"]
