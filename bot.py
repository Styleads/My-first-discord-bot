import discord
from discord.ext import commands, tasks
import random
import colorama
from colorama import Fore, Back, Style
from PIL import Image,ImageFont,ImageDraw
from io import BytesIO
import youtube_dl
import PIL
import asyncio
from PIL import Image
from io import BytesIO
import aiohttp 
from aiohttp import request
from googleapiclient import discovery
import json
import requests
import http.client

API_KEY = Api_for_perspective

perspectiveClient = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)




client = commands.Bot(command_prefix="%")



@client.event
async def on_ready():
    alink = ("https://youtu.be/dQw4w9WgXcQ")
    await client.change_presence(activity=discord.Streaming(name="help", url='alink'))

    print("Hey, me online")
    print("Hey, me online")   

@client.command()
async def hello(ctx):
    async with ctx.typing():
    await ctx.send("Hi")

@client.command(name='text', help="Displays the provided text as a quote by Mahatma Gandhi")
async def text(ctx, *, text = "tf nigg type something"):

    img = Image.open("download.jpg")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("CaviarDreams.ttf", 95)

    draw.text((225,250), text, (0,0,0), font=font )


    img.save("text.png")

    await ctx.send(file = discord.File("text.png"))

@client.command(name='ping', help="Displays the lateny of the bot")
async def ping(ctx):
    await ctx.send(f'**Ping** Latency: {round(client.latency * 1000)}ms')

@client.command(name='adiwho', help='Shows the custom command added by Adi Kamath')
async def adiwho(ctx):
    await ctx.send(f"**A Mighty Legend to ever exist, OG KING**")

@client.command(name='poll', help='Generates a poll with thumbs up and thumbs down emoji')
async def poll(ctx, *, message):
    emb = discord.Embed(title = "Poll", description = f"{message}")
    msg = await ctx.send(embed = emb)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')



@client.command(name='av', help='Shows the avatar of the mentioned user')
async def av(ctx, member: discord.Member = None):
 if not member:
  member = ctx.author
 await ctx.send(member.avatar_url)

@client.command(name='sevouwho', help='Shows the custom command added by sevou')
async def sevouwho(ctx):
  await ctx.send("‏‏‎ ‎")

@client.command(name='benwho', help='Shows a custom command added by Ben')
async def benwho(ctx):
  await ctx.send("just die bruh")



@client.command(name='dm', help='dms the mentioned user')
async def dm(ctx, member: discord.Member=None, *, args=None):
    if member != None and args != None:
        try:
            target = member
            await target.send(args)

            await ctx.channel.send("'" + args + "' sent to: " + target.name)

        except:
            await ctx.channel.send("Couldn't dm the given user.")
        

    else:
        await ctx.channel.send("You didn't provide a user's id and/or a message.")

@client.command(name='wanted', help='generates a wanted poster with the users avatar')
async def wanted(ctx, member: discord.Member=None):
    if  not member:
     member = ctx.author

    poster = Image.open("wanted.png")

    asset = member.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((257,257))

    poster.paste(pfp, (97,201))

    poster.save("generated.png")

    await ctx.send(file = discord.File("generated.png"))

@client.command(name='warn', help='Warns the mentioned user')
async def warn(ctx, member: discord.Member=None, *, args=None):
    if member != None and args != None:
        try:
            target = member
            guild = ctx.guild.name
            await target.send("You have been warned from: " + guild +  " for: " + args)

            await ctx.channel.send("'" + args + "' warned: " + target.name)

        except:
            await ctx.channel.send("Couldn't dm the given user.")
        

    else:
        await ctx.channel.send("You didn't provide a user's id and/or a message.")

@client.command(name='creditz', help='Gives the credits of the bot')
async def creditz(ctx):
    embed=discord.Embed(title="Credits", color=0xFF5733)
    embed.add_field(name="Kruthik", value="Made the bot.", inline=True)
    embed.add_field(name="Vaibhav(CrazyVibes)", value="Helped with codes", inline=False)
    embed.add_field(name="OG King/ButcherBoi_ØG", value="Gave most ideas", inline=False)
    embed.add_field(name="Hazard", value="Also gave ides", inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context=True, name='info', help='Gives the users info')
async def info(ctx, member: discord.Member):
  if not member:
   member = ctx.author
    
  img = Image.open("infoimgimg.png") 
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("Modern_Sans_Light.otf", 100) 
  fontbig = ImageFont.truetype("Fitamint Script.ttf", 400) 
    #    (x,y)::↓ ↓ ↓ (text)::↓ ↓     (r,g,b)::↓ ↓ ↓
  draw.text((200, 0), "Information:", (0,0,0), font=fontbig) 
  draw.text((50, 500), "Username: {}".format(member.name), (0,0,0), font=font) 
  draw.text((50, 700), "ID:  {}".format(member.id), (0,0,0), font=font) 
  draw.text((50, 900), "User Status: {}".format(member.status), (0,0,0), font=font) 
  draw.text((50, 1100), "Account created: {}".format(member.created_at), (0,0,0), font=font) 
  draw.text((50, 1300), "Nickname: {}".format(member.display_name), (0,0,0), font=font)
  draw.text((50, 1500), "Users' Top Role: {}".format(member.top_role), (0,0,0), font=font) 
  draw.text((50, 1700), "User Joined: {}".format(member.joined_at), (0,0,0), font=font) 
  img.save('infoimg2.png') #Change infoimg2.png if needed.
  await ctx.send(file = discord.File("infoimg2.png"))

@client.command(name='abandon', help='Generates a meme with the abandon template')
async def abandon(ctx, *, text = "The user didnt provide any text"):

    img = Image.open("white.png")

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("CaviarDreams.ttf", 15)

    draw.text((2,0), text, (0,0,0), font=font )

    img.save("whitetext.png")

    meme = Image.open("abandon.png")
    textarg = Image.open("whitetext.png")

    meme.paste(textarg, (48,274))

    meme.save("memeaband.png")

    await ctx.send(file = discord.File("memeaband.png"))



@client.command(name='DEVwho', help='Sends the custom command added by Devkeerthi Ideas')
async def DEVwho(ctx):
    a = ("DEVKEERTHI'S IDEAS  -  A YOUTUBER FROM INDIA PLEASE SUBSCRIBE TO HIM")
    embed = discord.Embed(title=a, color=0xFF5733)
    
    embed.add_field(name="Youtube", value="[Click here to redirect to his channel](https://youtube.com/channel/UCrzk85lOksIwHXOgj3QyIgg)", inline=True)
    embed.add_field(name="Twitch", value="[Click here to redirect to his twitch channel](https://www.twitch.tv/devkeerthisidea7)", inline=False)


    await ctx.send(embed=embed)
    
@client.command(name='anishwho', help='Sends the custom command added by Anish Patra')
async def anishwho(ctx):
    a = ("A guy from BLR who says his account is disabled and has good a  YouTube  channel.")
    embed = discord.Embed(title=a, color=0xFF5733)
    embed.description = "[Go subscribe him by clicking this link over here](https://www.youtube.com/channel/UC_voFV0B-rwf0hneI40ZYkw/videos?view_as=subscriber)."
    await ctx.send(embed=embed)

@client.command(name='invite', help='Sends the bot invite link to your server')
async def invite(ctx):
    embed = discord.Embed(title="Invite the bot to your server")
    embed.description = "[Click here](https://discord.com/oauth2/authorize?client_id=813353950194696253&scope=bot&permissions=230162241)"
    await ctx.send(embed=embed)

@client.command(name='slap', help='generates a meme with the slap template')
async def slap(ctx, member: discord.Member = None):
 if not member:
  member = ctx.author

 author = ctx.author

 poster = Image.open("slap.png")

 asset = member.avatar_url_as(size = 128)
 data = BytesIO(await asset.read())
 pfp = Image.open(data)

 pfp = pfp.resize((267,248))

 poster.paste(pfp, (856,356))

 poster.save("slap1.png")

 temp = Image.open("slap1.png")
 

 assetava = author.avatar_url_as(size = 128)
 dataa = BytesIO(await assetava.read())
 pfpaut = Image.open(dataa)

 pfpaut = pfpaut.resize((267,267))

 temp.paste(pfpaut, (501,85))

 temp.save("slap2.png")


 await ctx.send(file = discord.File("slap2.png"))

@client.command(name='purge', help='Deletes the number of messages')
async def purge(ctx, num_messages: int):
     channel = ctx.message.channel
     await ctx.message.delete()
     await channel.purge(limit=num_messages, check=None, before=None)

@client.command(name='achmnt', help='Generates a meme with minecrafts achievement get template')
async def achmnt(ctx, *, text = "tf nigg type something"):

    gudtexts = ["m3.png", "m4.png", "m5.png", "m6.png", "m7.png", "m8.png", "m9.png", "m10.png"]

    random_gudtext = random.choice(gudtexts)

    img = Image.open(random_gudtext)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Minecrafter_3 (2).ttf", 15)

    draw.text((57,34), text, (255,255,255), font=font )

    img.save("achmnt.png")
    
    await ctx.send(file = discord.File("achmnt.png"))
    
@client.command(name='affect', help='Generates a meme with the affect template')
async def affect(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    affect = Image.open("aff.png")

    asset = member.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((197,152))

    affect.paste(pfp, (167,351))

    affect.save("monor.png")

    await ctx.send(file = discord.File("monor.png"))

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")


@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" you have unmuted from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)



@client.command(name="chatbot", help="Chat with a chatbot!")
async def chatbot(ctx, message: str):
    URL = f'https://some-random-api.ml/chatbot?key={SRA_key}&message={message}'

    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data['response'])

        else:
            await ctx.send(f"API returned a {response.status} status.")

@client.command(name='fact')
async def animal_fact(ctx, animal: str):
	if (animal := animal.lower()) in ("dog", "cat", "panda", "fox", "bird", "koala"):
		fact_url = f"https://some-random-api.ml/facts/{animal}"
		image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"

		async with request("GET", image_url, headers={}) as response:
			if response.status == 200:
				data = await response.json()
				image_link = data["link"]

			else:
				image_link = None

		async with request("GET", fact_url, headers={}) as response:
			if response.status == 200:
				data = await response.json()

				embed = discord.Embed(title=f"{animal.title()} fact",
								description=data["fact"],
								colour=ctx.author.colour)
				if image_link is not None:
					embed.set_image(url=image_link)
				await ctx.send(embed=embed)

			else:
				await ctx.send(f"API returned a {response.status} status.")

	else:
		await ctx.send("No facts are available for that animal.")

@client.command()
async def start(ctx):
    async with ctx.typing():
        await asyncio.sleep(100000000000)
    await ctx.send('hi.')

@client.command()
async def wasted(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png')) 

@client.command()
async def triggered(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.gif')) 

@client.command()
async def glass(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/glass?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png')) 

@client.command()
async def greyscale(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/greyscale?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png')) 

@client.command()
async def invert(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/invert?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png')) 

@client.command()
async def invertgreyscale(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/invertgreyscale?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png')) 

@client.command()
async def brightness(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/brightness?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@client.command()
async def threshold(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/threshold?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@client.command()
async def sepia(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/sepia?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@client.command()
async def red(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/red?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@client.command()
async def green(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/green?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@client.command()
async def blue(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/blue?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@client.command()
async def pixelate(ctx, member: discord.Member=None):
    if not member: 
        member = ctx.author 
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/pixelate?avatar={member.avatar_url_as(format="png", size=1024)}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@client.command()
async def comment(ctx, member: discord.Member=None, *, comment = "I didnt type anything lmfao"):
    if not member: 
        member = ctx.author

    name = member.display_name 
    av = member.avatar_url_as(format="png", size=1024)
        
    async with aiohttp.ClientSession() as response:


        async with response.get(f'https://some-random-api.ml/canvas/youtube-comment?comment={comment}&username={name}&avatar={av}') as wantedImage:

            imageData = BytesIO(await wantedImage.read()) 
            await response.close()
            
            await ctx.send(file=discord.File(imageData, 'wasted.png'))

@client.command()
async def toxicity_check(ctx, text = "no text entered"):
    
    userinput = text
    analyze_request = {
      'comment': { 'text': userinput },
      'requestedAttributes': {'TOXICITY': {}}
    }

    response = perspectiveClient.comments().analyze(body=analyze_request).execute()
    finalRespone = response['attributeScores']['TOXICITY']['summaryScore']['value']
    finalFinalRespone = (finalRespone * 100)

    await ctx.send(f'{finalFinalRespone}%')

@client.command()
async def ship(ctx, member: discord.Member = None, user: discord.Member = None):
    if not member:
        member = ctx.author

    if not user:
        user = ctx.author

    url = "https://love-calculator.p.rapidapi.com/getPercentage"

    querystring = {"fname":member,"sname":user}

    headers = {
        'x-rapidapi-key': Rapid_api_key,
        'x-rapidapi-host': "love-calculator.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    percentage = json.loads(response.text)["percentage"]
    result = json.loads(response.text)["result"]

    embed = discord.Embed(title="Ship", description=f"Shipping {member.mention} and {user.mention}... ", colour=discord.Colour.red())
    embed.add_field(name="Percentage:", value=f"{percentage}%", inline=False)
    embed.add_field(name="Statement:", value=result, inline=False)

    await ctx.send(embed=embed)


@client.command()
async def ask(ctx, *, text = None):
    if not text:
        await ctx.send("No question was asked.")

    URL = f'https://8ball.delegator.com/magic/JSON/{text}'

    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            magic = data["magic"]
            answer = magic["answer"]

            embed = discord.Embed(title="8ball")
            await ctx.send(answer)


        else:
            await ctx.send(f"API returned a {response.status} status.")

@client.command()
async def meme(ctx):

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            embed = discord.Embed(title="Meme", description="")
            res = await r.json()
            main = res['data']['children'] [random.randint(0, 25)]['data']
            url = main['url']
            title = main['title']
            embed = discord.Embed(title="Meme", description=f'[{title}]({url})')
            embed.set_image(url=url)
            await ctx.send(embed=embed)



client.run(TOKEN)