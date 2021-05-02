import discord 
import os
from replit import db
from datetime import datetime, timezone, timedelta 
from alive import alive

d = {'ACDT': 10.5, 'ACST': 9.5, 'ACT': -5, 'ADT': -3, 'AEDT': 11, 'AEST': 10, 'AFT': 4.5, 'AKDT': -8, 'AKST': -9, 'ALMT': 6, 'AMST': -3, 'ANAT': 12, 'AQTT': 5, 'ART': -3, 'AWST': 8, 'AZOST': 0, 'AZOT': -1, 'AZT': 4, 'BNT': 8, 'BIOT': 6, 'BIT': -12, 'BOT': -4, 'BRST': -2, 'BRT': -4, 'BTT': 6, 'CAT': 2, 'CCT': 6.5, 'CEST': 2, 'CET': 1, 'CHADT': 13.75, 'CHAST': 12.75, 'CHOT': 8, 'CHOST': 9, 'CHST': 10, 'CHUT': 10, 'CIST': -8, 'CKT': -10, 'CLST': -3, 'CLT': -4, 'COST': -4, 'COT': -5, 'CVT': -1, 'CWST': 8.75, 'CXT': 7, 'DAVT': 7, 'DDUT': 10, 'DFT': 1, 'EASST': -5, 'EAST': -6, 'EAT': 3, 'EDT': -4, 'EEST': 3, 'EET': 2, 'EGST': 0, 'EGT': -1, 'EST': -5, 'FET': 3, 'FJT': 12, 'FKST': -3, 'FKT': -4, 'FNT': -2, 'GALT': -6, 'GAMT': -9, 'GET': 4, 'GFT': -3, 'GILT': 12, 'GIT': -9, 'GMT': 0, 'GYT': -4, 'HDT': -9, 'HAEC': 2, 'HST': -10, 'HKT': 8, 'HMT': 5, 'HOVST': 8, 'HOVT': 7, 'ICT': 7, 'ILDW': -12, 'IDT': 3, 'IOT': 3, 'IRDT': 4.5, 'IRKT': 8, 'IRST': 3.5, 'JST': 9, 'KALT': 2, 'KGT': 6, 'KOST': 11, 'KRAT': 7, 'KST': 9, 'LINT': 14, 'MAGT': 12, 'MART': -9.5, 'MAWT': 5, 'MDT': -6, 'MET': 1, 'MEST': 2, 'MHT': 12, 'MIST': 11, 'MIT': -9.5, 'MMT': 6.5, 'MSK': 3, 'MUT': 4, 'MVT': 5, 'MYT': 8, 'NCT': 11, 'NDT': -2.5, 'NFT': 11, 'NOVT': 7, 'NPT': 5.75, 'NST': -3.5, 'NT': -3.5, 'NUT': -11, 'NZDT': 13, 'NZST': 12, 'OMST': 6, 'ORAT': 5, 'PDT': -7, 'PET': -5, 'PETT': 12, 'PGT': 10, 'PHOT': 13, 'PHT': 8, 'PKT': 5, 'PMDT': -2, 'PMST': -3, 'PONT': 11, 'PWT': 9, 'PYST': -3, 'PYT': -4, 'RET': 4, 'ROTT': -3, 'SAKT': 11, 'SAMT': 4, 'SAST': 2, 'SBT': 11, 'SCT': 4, 'SDT': -10, 'SGT': 8, 'SLST': 5.5, 'SRET': 11, 'SRT': -3, 'SYOT': 3, 'TAHT': -10, 'THA': 7, 'TFT': 5, 'TJT': 5, 'TKT': 13, 'TLT': 9, 'TMT': 5, 'TRT': 3, 'TOT': 13, 'TVT': 12, 'ULAST': 9, 'ULAT': 8, 'UTC': 0, 'UYST': -2, 'UYT': -3, 'UZT': 5, 'VET': -4, 'VLAT': 10, 'VOLT': 4, 'VOST': 6, 'VUT': 11, 'WAKT': 12, 'WAST': 2, 'WAT': 1, 'WEST': 1, 'WET': 0, 'WIB': 7, 'WIT': 9, 'WITA': 8, 'WGST': -2, 'WGT': -3, 'WST': 8, 'YAKT': 9, 'YEKT': 5}

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("!add"): 
        
        value = message.content.split("!add ", 1)[1].strip().upper()

        if len(message.mentions) == 0:
            idt = message.author.id
            db[str(idt)] = value
            await message.channel.send("Timezone Added!")


    if message.content.startswith("!time"):
        idt = message.author.id
        
        if len(message.mentions) == 0:
            if str(idt) in db:     
                timez = db[str(idt)]
                offset = d[timez] 
                ctime = str(datetime.now(timezone.utc) + timedelta(hours=offset))
                await message.channel.send(f"<@{message.author.id}> {ctime[: 19]}")
            else: 
                await message.channel.send(f"Time Zone Data for <@{message.author.id}> is Unavailable")
        
        else: 
            for mention in message.mentions:

                idt = mention.id

                if str(idt) in db:     
                    timez = db[str(idt)]
                    offset = d[timez] 
                    ctime = str(datetime.now(timezone.utc) + timedelta(hours=offset))
                    await message.channel.send(f"<@{mention.id}> {ctime[ :19]}")
                else: 
                    await message.channel.send(f"Time Zone Data for <@{mention.id}> is Unavailable")   

    if message.content.startswith("!del"):

        if len(message.mentions) == 0:
            idt = message.author.id
            if str(idt) in db: 
                del db[str(idt)]
                await message.channel.send(f"Time Zone Data for <@{message.author.id}> has Been Deleted")
            else: 
                await message.channel.send(f"Time Zone Data for <@{message.author.id}> is Not in Database")

    if message.content.startswith("!tzones"):
        embed = discord.Embed(color=discord.Colour.green())
        embed.set_author(name = 'Timezones')
        embed.add_field(name = 'Unsupported Timezones', value = 'AMT, AST, BST, CDT, CT, ECT, GST, IST, LHST, MST, PST, SST', inline=False)
        embed.add_field(name = 'Timezones Excluding Unsupported Ones', value = 'https://en.wikipedia.org/wiki/List_of_time_zone_abbreviations', inline=False)
        #for key, value in d.items(): 
            #embed.add_field(name = f'{key}', value = f'{value}', inline = False)
        
        await message.channel.send(embed=embed)
        

    if message.content.startswith("!help"):
        embed = discord.Embed(color=discord.Colour.green())
        embed.set_author(name = 'Help Page')
        embed.add_field(name = '!tzones', value = 'list of timezones that are unsupported and link to timezone abbreviation')
        embed.add_field(name = '!add', value = 'allows you to register your timezone with the bot')
        embed.add_field(name = '!del', value = 'allows you to delete saved timezone data saved with bot')
        embed.add_field(name = '!time', value = 'gives time of mentioned users or message author if no users are mentioned')
        await message.channel.send(embed=embed)

alive()
client.run(os.getenv('TOKEN'))
