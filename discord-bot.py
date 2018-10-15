import discord
import asyncio
import json
import sui
import logging

logging.basicConfig(level=20, format='%(asctime)s: %(name)s | LOG: %(message)s')
log = logging.getLogger(__name__)

client = discord.Client()
secrets = ''

with open('secrets.json') as f:
    secrets = json.load(f)

@client.event
async def on_ready():
    print('Discord server: Start up!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!instance'):
        tag_name = message.content.split()[1]
        value_name = message.content.split()[2]

        instance = sui.InstanceHandler(tag_name, value_name)

        if (instance.find()):
            instance_dic = instance.find()

            em = discord.Embed(title='Instance Information', description='Instance Found', colour=0x00ff00)
            em.add_field(name='Instance State', value=str(instance_dic['InstanceState']), inline=False)
            em.add_field(name='Instance IP', value=str(instance_dic['InstanceIP']), inline=False)
            em.add_field(name='Instance ID', value=str(instance_dic['InstanceID']), inline=False)
            em.add_field(name='Instance Private IP', value=str(instance_dic['InstancePrivateIP']), inline=False)

        else:
            em = discord.Embed(title='Instance Information',description='Instance does not exist.', colour=0xff0000)

        await client.send_message(message.channel, embed=em)

        #FEATURE: Once buttons are added it would be nice to do this via buttons instead of a text action
        em2 = discord.Embed(title='Actions', description='Start, Stop, None', colour=0x42dcf4)
        await client.send_message(message.channel, embed=em2)

        action = await client.wait_for_message(timeout=10.0, author=message.author)
        
        if action.content == "start":
            instance.start()
            em2 = discord.Embed(title='Action Taken', description='Starting', colour=0x42dcf4)
            await client.send_message(message.channel, embed=em2)
        elif action.content == "stop":
            instance.stop()
            em2 = discord.Embed(title='Action Taken', description='Stopping', colour=0x42dcf4)
            await client.send_message(message.channel, embed=em2)
        else:
            return

        return

 

    if message.content.startswith('!ssm'):
        tag_name = message.content.split()[1]
        value_name = message.content.split()[2]

        parameter = sui.ParameterHandler(tag_name, value_name)

        if (parameter.find()):
            ssm_dic = parameter.find()

            em = discord.Embed(title='Paramter Information', description='Parameter Found!', colour=0x00ff00)
            em.add_field(name='Parameter Value', value=str(ssm_dic), inline=False)

        else:
            em = discord.Embed(title='Parameter Information',description='Parameter does not exist.', colour=0xff0000)

        await client.send_message(message.channel, embed=em)

client.run(str(secrets["token"]))