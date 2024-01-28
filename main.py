import discord
from discord.ext import commands
from cats import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


TOKEN = 'MTE4ODA4Njc5OTIzOTc1Nzg2NQ.GY63KP.5ZkpEw6Wwk9c7PjuJo8FeCl7Mc0J6wsH1yZ4rE'

#команды
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./{attachment.filename}')
            await ctx.send(get_class(test_img=f'./{attachment.filename}', model_keras='keras_model.h5', labels='labels.txt'))
    else:
        await ctx.send('Вы забыли прикрепить картинку :(')

bot.run(TOKEN)