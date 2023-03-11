import discord
import random


chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"


TOKEN = 'OTk2MjQ2NzMzNTYwNDgzOTEx.GjLlK7.DXjmqJeP1KluSe8GLQ4GyWdQwXTfGSu620T4Qo'
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}:{user_message} ({channel})')
    if message.author == client.user:
        return
    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'how are you?':
             await message.channel.send(f'I am doing just fine, what about you {username}?')
             return   
        elif user_message.lower() == '!about':
             await message.channel.send("Welcome to MeaVana, the most customizable personal dashboard, We are a brand new fast growing new tab page for Google Chrome, We provide a rich experience through a beautiful daily background visual, streamlined digital desktop basics, and deep, rich functionality")
             return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you Later {username}!')
            return
        elif user_message.lower() == 'imran':
            await message.channel.send(f'Kal ana Imran!')
            return
        elif user_message.lower() == '!random':
            response = f'This is your random number : {random.randrange(1000000)}'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!app':
            hyperlink_format1 = "https://chrome.google.com/webstore/detail/meavana-customize-your-ne/kgbcoelgfffkmkpfnldemdinmcbpjlaa"
            await message.channel.send(hyperlink_format1)
            return
        elif user_message.lower() == '!insta':
            hyperlink_format2 = "https://www.instagram.com/meavana_dash/"
            await message.channel.send(hyperlink_format2)
            return
        elif user_message.lower() == '!fb' :
             hyperlink_format3 = "https://www.facebook.com/meavanadash"
             await message.channel.send(hyperlink_format3)
             return
        elif user_message.lower() == '!twitter':
             hyperlink_format4 = "https://twitter.com/meavanadash"
             await message.channel.send(hyperlink_format4)
             return
        elif user_message.lower() == '!linkedin':
             hyperlink_format5 = "https://www.linkedin.com/company/meavana/"
             await message.channel.send(hyperlink_format5)
             return
        elif user_message.lower() == '!pinterest':
             hyperlink_format6 = "https://in.pinterest.com/meavanadash/"
             await message.channel.send(hyperlink_format6)
             return
        elif user_message.lower() == '!pexels':
             hyperlink_format7 = "https://www.pexels.com/@mea-vana-234745693/"
             await message.channel.send(hyperlink_format7)
             return
        if user_message.lower() == '!anywhere':
            await message.channel.send('This can be used anywhere!')
            return


client.run(TOKEN)
