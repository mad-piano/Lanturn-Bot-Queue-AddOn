#Multi-use queue-system in Lanturn bot. developed by Dizzy#9275
import discord
from discord.ext import commands
import asyncio
import datetime
from discord.ext.commands import Bot


#The list that holds the users in queue
queue = []

#The size of Lanturn bot's queue; you can change that num to your queue size
queue_size = 20


#The bot will add people in the queue when they send the seed check command
@client.event
async def on_message(message):
    #Two author var: one for an ID num, and one for their @
    author_ID = message.author
    author = message.author.mention
    #This will get the bot's ID so it only counts when the bot sends a message
    user = client.get_user("Your bot's ID")
    #This will insure the bot will start to add users if they say the seed check command and are in a specific channel 
    if message.content == "!CheckMySeed" and message.channel.id == "The channel ID that the bot sends messages in": 
        #This checks the current person being served, and to not re add them in the queue
        for q in queue:
            if author == queue[0]:
                    return
            #If the user is already in queue, remove the extra value in the queue list []
            elif q == str(message.author.mention) in queue:
                queue.remove(f'{message.author.mention}')
        else:
            #This will add them in the queue if they are currently not in the list and the queue is not maxed
            if len(queue) < queue_size:
                queue.append(f'{message.author.mention}')
    #When the bot starts to search for the user, the code will wait 75 sec (aprox time the bot takes to trade) and remove that person from the queue
    if message.content.endswith("My in game name is: Darkrai.") and author_ID == user:
        #You can change the time, I would reccomend at least 70
        await asyncio.sleep(75)
        queue.remove(queue[0])
        print(queue)
    await client.process_commands(message)


#Will check the size of the queue and post the queue list accordingly, a little redundent :-(
@client.command(pass_context=True)
async def List(ctx):
    #This will add the users in the queue list, with additional info
    queue_list = []
    #Loop until every object/user in the queue is grabbed
    for q in queue:
            #Grab the index of all the cuurent objects/users in the queue list [], sliced bewtween 0 and the size of the queue. Add 1 to the index because python starts the index at 0
            content = queue[0:len(queue)].index(q) + 1
            #Convert index to a str, and add the user's @
            content_2 = str(content) + ":" + q
            #Add the user to the new list
            queue_list.append(content_2)
    if len(queue) == 0:
        await ctx.send("`No one is currently in the queue!`")
    else:
        #Format the objects in the new list to look nice
        embed = discord.Embed(
            title = "**Queue List:**",
            description = '\n'.join(queue_list),
            colour = discord.Colour.purple(),
        )
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def MyPlace(ctx):
    author_ctx = ctx.message.author.mention
    #Grab the index of the user, add 1 to the index because python starts the index at 0
    placement = queue.index(author_ctx) + 1
    if len(queue) == 0:
        await ctx.send("`No one is currently in the queue!`")
    else:
        embed = discord.Embed(
            title = f"**Specific Position in Queue:**",
            description = f"{author_ctx}, your placement in the queue is: **{placement}**",
            colour = discord.Colour.purple(),
        )
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def QueueSize(ctx):
    #Takes the size of the queue and reports it back to the user
    embed = discord.Embed(
        title = f"**Queue Size:**",
        description = f"The queue size is: {len(queue)}",
        colour = discord.Colour.purple(),
    )
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)