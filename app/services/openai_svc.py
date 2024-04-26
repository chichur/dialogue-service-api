import time

import requests

from app.core.config import settings


def generate_openai_prompt(prompt: str) -> str:
    """
    Simple client for OpenAi Api request
    """
    # with requests.Session() as session:
    #         },

    with requests.Session() as session:
        response = session.get(url=settings.OPENAI_URL)
        result = response.json()
    return result["message"]
