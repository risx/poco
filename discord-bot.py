import discord
import asyncio
import json
import botow

client = discord.Client()
secrets = ''

with open('secrets.json') as f:
    secrets = json.load(f)

@client.event
async def on_ready():
    print('Discord server: Start up!')

@client.event
async def on_message(message):
    if message.content.startswith('!status'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Finding Instance...')
        if (botow.FindInstance('Name','wistful')):
            await client.edit_message(tmp, botow.FindInstance('Name','wistful'))
        else:
            await client.edit_message(tmp, 'Instance not found!')

client.run(str(secrets["token"]))