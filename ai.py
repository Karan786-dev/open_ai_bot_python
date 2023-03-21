import openai
from config import *

openai.api_key = openai_key

class Ai:
    def __init__(self):
        pass

    def generate_answer(question):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{question}/nAnswer:",
            temperature=0,
            max_tokens=800,
            top_p=1,
        )
        answer = response["choices"][0]["text"]
        return answer

    def generate_image(prompt):
        response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
        return response["data"][0]["url"]

