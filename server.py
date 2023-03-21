from flask import Flask, request
from bot import Bot
from ai import Ai
from config import *
import openai

bot = Bot(bot_token=bot_token, webhook_url=webhook_url)
app = Flask(__name__)


def get_prompt(list):
    prompt = ""
    command = list[0]
    for i in list:
        if not i is command:
            prompt += " " + i
    return prompt


@app.route("/", methods=["POST"])
def index():
    update = request.get_json()
    if not "message"  in update or not "text" in update["message"]:
        return "OK"
    command = update["message"]["text"].split(" ")[0]
    splited_command = update["message"]["text"].split(" ")
    chat_id = update["message"]["from"]["id"]
    match command:
        case "/start":
            bot.sendMessage(
                {
                    "chat_id": chat_id,
                    "text": "Hey brother!!\n\nI am an AI that use chatgpt api\n\nUse /ask to ask questions\nUse /image to generate images\n\nNote: I can give some wrong answers , because i am on learning stage!!",
                }
            )
        case "/ask":
            if len(splited_command) == 1:
                return bot.sendMessage(
                    {
                        "chat_id": chat_id,
                        "text": "Use this command like: `/ask who is ceo of google`",
                        "parse_mode": "MARKDOWN",
                    }
                )
            try:
                answer = Ai.generate_answer(get_prompt(splited_command))
                bot.sendMessage(
                    {
                        "chat_id": chat_id,
                        "text": f"`{answer}`",
                        "parse_mode": "MARKDOWN",
                    }
                )
            except openai.InvalidRequestError as e:
                bot.sendMessage(
                    {
                        "chat_id": chat_id,
                        "text": f"`{e}`",
                        "parse_mode": "MARKDOWN",
                    }
                )
        case "/image":
            if len(splited_command) == 1:
                return bot.sendMessage(
                    {
                        "chat_id": chat_id,
                        "text": "Use this command like: `/image A cute dog`",
                        "parse_mode": "MARKDOWN",
                    }
                )
            try:
                photo = Ai.generate_image(get_prompt(splited_command))
                bot.sendPhoto(
                    {
                        "chat_id": chat_id,
                        "photo": photo,
                        "parse_mode": "MARKDOWN",
                    }
                )
            except openai.InvalidRequestError as e:
                bot.sendMessage(
                    {
                        "chat_id": chat_id,
                        "text": f"`{e}`",
                        "parse_mode": "MARKDOWN",
                    }
                )

    return "Hello world"


if __name__ == "__main__":
    bot.start()
    print("Everything is running now")
    from waitress import serve
    serve(app, port=4040)
