"""TEST Reminder bot"""

import discord
from discord.ext import commands
#import os เปิดos เพื่อเข้าถึงไฟล์

#เอาไว้สำหรับรอรับคำสั่ง
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Run the bot
# always don't forget to remove token
#os.chdir('โฟลเดอร์รูป')
def main():
    """Bot"""
    token = '' #สำหรับรันบอท

    @bot.event #ดูสถานะ
    async def on_ready():
        """standby"""
        print("Hi, This is Yu! I'm here")
        print("<---------------------->")

    #รอคำสั่ง
    @bot.command()
    async def hello(ctx):
        """hi"""
        await ctx.send("Hi, I am here!")

    @bot.command()
    async def test(ctx):
        """test"""
        await ctx.send("arai ja!")

    #@bot.command()
    #async def timeup(ctx): คำสั่งส่งรูป
    #    
    #    #ส่งรูปภาพไปยังช่องข้อความ
    #    await ctx.send('send image', file = discord.File("up.png"))

        

    bot.run(token)

main()
"sssss"
