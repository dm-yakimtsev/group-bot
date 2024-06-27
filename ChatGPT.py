from openai import OpenAI
from config import GPT_TOKEN

client = OpenAI(api_key=GPT_TOKEN)


def gpt(text: str) -> str:
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": ""},  # В поле content указываем "личность" бота на английском языке
            {'role': 'user', 'content': f'{text}'},  # Здесь передаётся сам запрос
            {'role': 'assistant', 'content': ''}  # Передаём контекст
        ],
        temperature=0.1  # Значение от 0 до 1. Отвечает за количество выразительности
    )

    return completion.choices[0].message.content  # Получаем ответ нейросети на сообщение пользователя
