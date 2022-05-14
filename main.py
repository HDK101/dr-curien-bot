import discord
import time
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Curien!':
        await message.channel.send('I must compliment you.')
        time.sleep(3)
        await message.channel.send("I didn't think you could make this far")
        time.sleep(3)
        await message.channel.send("However, this is it!")
        time.sleep(3)
        await message.channel.send("Let's see how good you really are!")
        time.sleep(3)
        await message.channel.send("https://youtu.be/AH636zGQm5Q?t=18")

client.run(os.environ["DISCORD_TOKEN"])
