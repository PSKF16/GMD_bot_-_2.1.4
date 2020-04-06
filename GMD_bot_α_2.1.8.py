import os
import time
import math
import pytz
import random
import asyncio
import discord
import datetime
import websockets

client = discord.Client()
gmdkrw = 100
krwgmd = 0.01
a = -5
b = 5

@client.event
async def on_ready():
           await client.change_presence(status=discord.Status.online, activity=discord.Game("환율 알리미 "))
           print("------------------------------")
           print(client.user.name)
           print(client.user.id)
           print("------------------------------")
           time.sleep(3)
           print("------------------------------")
           print("준비완료!")
           print("------------------------------")

@client.event
async def on_message(message):
           
           if message.author.bot:
                      return None

           print(message.content)

           if message.content == "!환율":
                      while True:

                                 global gmdkrw
                                 global krwgmd
                                 global a
                                 global b
                                 global h
                                 global m
                                 global s

                                 from pytz import timezone
                                 from datetime import datetime
                                 now = datetime.now(timezone('Asia/Tokyo'))
                                 
                                 gmdkrw += (random.randrange(a,b))
                                 krwgmd = round(1/gmdkrw,5)
                                 
                                 if (gmdkrw <= 50):
                                            a = -1
                                            b = 5
                                            
                                 if (gmdkrw >= 200):
                                            a = -5
                                            b = 1
                                            
                                 if (gmdkrw >= 70):
                                            if (gmdkrw <= 130):
                                                       a = -5
                                                       b = 5

                                 if ((now.hour == 9) and (now.minute == 00) and (now.second == 00)):
                                            embed = discord.Embed(title="%s년%s월%s일 %s시%s분%s초" % (now.year,now.month,now.day,now.hour,now.minute,now.second), description="환율 시장이 개장되었습니다.", color=0x62c1cc)
                                            embed.set_footer(text="GMD 관련 문의는 稲妻勝廣#3739에 해 주세요.")

                                            await message.channel.send(embed=embed)

                                            time.sleep(1)

                                 if ((now.hour == 15) and (now.minute == 00) and (now.second == 00)):
                                            embed = discord.Embed(title="%s년%s월%s일 %s시%s분%s초" % (now.year,now.month,now.day,now.hour,now.minute,now.second), description="환율 시장이 폐장되었습니다.", color=0x62c1cc)
                                            embed.set_footer(text="GMD 관련 문의는 稲妻勝廣#3739에 해 주세요.")

                                            await message.channel.send(embed=embed)

                                            time.sleep(1)

                                 if ((now.hour >= 9) and (now.hour < 15)):
                                            if (((now.minute == 00) and (now.second == 00)) or ((now.minute == 30) and (now.second == 00))):
                                                       print ("%s년%s월%s일 %s시%s분%s초" % (now.year,now.month,now.day,now.hour,now.minute,now.second))
                                                       print("---------------------------------")
                                                       print("최소변동값:")       
                                                       print(a)
                                                       print(" ")
                                                       print("최대변동값")
                                                       print(b)
                                                       print(" ")                      
                                                       print("1GMD -> KRW")
                                                       print(gmdkrw)
                                                       print(" ")
                                                       print("1KRW -> GMD")
                                                       print(krwgmd)
                                                       print("---------------------------------")

                                                       embed = discord.Embed(title="%s년%s월%s일 %s시%s분%s초" % (now.year,now.month,now.day,now.hour,now.minute,now.second), description="현재 시각 기준 환율", color=0x62c1cc)
                                                       embed.set_footer(text="GMD 관련 문의는 稲妻勝廣#3739에 해 주세요.")
                                                       embed.add_field(name="1GMD -> KRW ", value=("1GMD = " + str(gmdkrw) + "KRW"), inline=False)
                                                       embed.add_field(name="1KRW -> GMD ", value=("1KRW = " + str(krwgmd) + "GMD"), inline=False)
                                                                             
                                                       await message.channel.send(embed=embed)

                                                       time.sleep(1)
                                                       
access_token = os.environ["BOT_TOKEN"]                                
client.run(access_token)
