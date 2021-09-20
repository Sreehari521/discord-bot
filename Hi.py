import discord
import random

TOKEN = "Your Token"

client = discord.Client()

@client.event
async def on_ready():
    print('We have loged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client:
        return
    
    if message.channel.name == "general":
        if user_message.lower() == "hello":
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == "bye":
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == "!random":
            response = f'This is your random number: {random.randrange(10000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == "!important":
            await message.channel.send("@everyone Come here it is important")
            return

client.run(TOKEN)
