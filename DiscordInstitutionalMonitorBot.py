import discord
from discord.ext import commands
import random

from WhaleMonitor import *

TOKEN = 'ODkwNzQzMzgxMTE2OTgxMjcx.YU0Paw.aw8aXwpcn8ZGiQFmerlsej_QHUg'

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('{0.user} has logged on!'.format(client))

@client.event
async def on_message(message):              #logs messages
    with open('LOG_InstitutionalBot.txt', 'a+') as LOG:
        username = str(message.author).split("#")[0]
        userMessage = str(message.content)
        channel = str(message.channel.name)
        LOG.write(f'{username}: {userMessage} ({channel})' + "\n")
        print(f'{username}: {userMessage} ({channel})')

    if message.author == client.user:          #so the bot doesnt talk to itself
        return 

    #if channel == 'general':       # logic for commands
    if userMessage.lower() == 'hello' or userMessage.lower() == 'hi':
        await message.channel.send(f'Hello {username}!')
        return 
    elif userMessage.lower() == 'bye':
        await message.channel.send(f'Bye {username}! Have a good day!')
        return 
    elif userMessage.lower() == 'random':
        response = f'Random Number: {random.randrange(0,1000)}'
        await message.channel.send(response)
        return 

    # if userMessage.lower() == 'anywhere':
    #     await message.channel.send(f'This message can be seen anywhere!')
    #     return 

    #if str(message.channel.name) != 'general':          # passes it to commands, works 
    
    await client.process_commands(message)                  



########## COMMANDS ##########


##PRICE
@client.command(name ='StockPrice')            # percent share change
async def StockPrice(context, fund: str, lowPrice: float, upperPrice: float): 
    csvLink = getFundCSV(fund)
    findStocksByPrice(csvLink, lowPrice, upperPrice)

    with open("stockPrice.txt", "rb") as file:
        await context.message.channel.send("Screened by stock price:", file=discord.File(file, "stockPrice.txt"))
    return


##QTRs FIRST OWNED
@client.command(name ='FirstOwned')            # percent share change
async def FirstOwned(context, fund: str, lowPrice: float, upperPrice: float, *args: str): 
    csvLink = getFundCSV(fund)
    findByQtrFirstOwned(csvLink, lowPrice, upperPrice, *args)

    with open("QtrFirstOwned.txt", "rb") as file:           
        await context.message.channel.send("Screened by stock price:", file=discord.File(file, "QtrFirstOwned.txt"))
    return


##SHARE PERCENT CHANGE
@client.command(name ='ShareChange')            # percent share change
async def ShareChange(context, fund: str, lowPrice: float, upperPrice: float, incOrDec: str, prcntChng: float):  
    csvLink = getFundCSV(fund)
    findBySharePercentageChange(csvLink, lowPrice, upperPrice, incOrDec, prcntChng)

    with open("share_%_Change.txt", "rb") as file:
        await context.message.channel.send("Screened by percent change in shares this quarter:", file=discord.File(file, "share_%_Change.txt"))
    return


##PERCENT OWNERSHIP
@client.command(name ='Ownership') # name of the command in name 
async def Ownership(context, fund: str, lowPrice: float, upperPrice: float, ownership: float):     #context contains the context that called the command: message that called, keep same name as function above 
    csvLink = getFundCSV(fund)
    findByCompanyOwnership(csvLink, lowPrice, upperPrice, ownership)

    with open("Ownership.txt", "rb") as file:
        await context.message.channel.send("Screened by percent ownership of the company:", file=discord.File(file, "Ownership.txt"))

    return



client.run(TOKEN)


    # myEmbed = discord.Embed(title = "Ticker: CNOBP", color = 0x00000000)
    # myEmbed.add_field(name = "Holding Value: $", value = "84,514,000.0 ", inline = False)
    # myEmbed.add_field(name = "Ownership %:", value = "61.2215217", inline = False)
    # myEmbed.add_field(name = "Quarter first owned:", value = "Q2 2015", inline = False)
    # myEmbed.add_field(name = "Source Date:", value = "09/30/2021", inline = False)
    # #myEmbed.set_footer(text = "this is a footer")
    # #myEmbed.set_author(name = "Author of Embed")
