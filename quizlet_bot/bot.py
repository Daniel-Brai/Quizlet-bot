import os
import requests
import json
import asyncio
import discord

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
token = os.getenv('TOKEN')

def get_random_question():
    question = ""
    idx = 1
    answer = 0

    question_api_uri = os.getenv('QUESTION_API_URI')
    response = requests.get(question_api_uri)
    data = json.loads(response.text)

    points = int(data[0]['points'])
    question += f"Question: \n{data[0]['title']} ({points} points) \n"

    for item in data[0]['answer']:
        question += str(idx) + "." + " " + item['answer'] + "\n"

        if item['is_correct']:
            answer = idx

        idx += 1

    return (question, answer, points)

         

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('H'):
        await message.channel.send(
            'Hello! You are welcome to DannyBrai Server. \nI am a bot that serves you random questions. \nYou have a limit of 5 seconds to answer.'
        )

    if message.content.startswith('$question'):
        total_pts = 0
        q, a, p = get_random_question()
        await message.channel.send(q)

        def check_user_answer(answer):
            return answer.author == message.author and answer.content.isdigit()
        
        try:
            guess = await client.wait_for('message', check=check_user_answer, timeout=5.0)

            if int(guess.content) == a:
                total_pts += p
                return await message.channel.send(f"😁 Hooray! You guessed correctly. Your total points is: {total_pts} ")
            else:
                return await message.channel.send('😔 Oops! Your answer was wrong.')

        except asyncio.TimeoutError:
            return await message.channel.send('Oops! You took too long to respond.')

client.run(token)
