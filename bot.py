import discord
from discord import app_commands
import responses


async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(file=discord.File(response))

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTE2MzIyOTc5NTIyNDY1MzkyNA.GOYVGA.HrxCu1y1CP5Bo2qs_Hoizng4sOoMU8kHfrvNNU'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    tree = app_commands.CommandTree(client)

    @tree.command(name='blahaj', description='Get an image of a blahaj', nsfw=False, auto_locale_strings=True, extras=None)
    async def blahaj(interaction: discord.Interaction):
        await interaction.response.send_message(file=discord.File(responses.randomblahaj()))
        
    @tree.command(name='blåhaj', description='Get an image of a blåhaj', nsfw=False, auto_locale_strings=True, extras=None)
    async def blåhaj(interaction: discord.Interaction):
        await interaction.response.send_message(file=discord.File(responses.randomblahaj()))



    @client.event
    async def on_ready():
        await tree.sync()
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        #if user_message == '/blahaj' or '/blåhaj':
            #print(f'{username} said "{user_message}" ({channel})')
        await send_message(message, user_message)



    client.run(TOKEN)

