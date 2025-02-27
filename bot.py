import discord
import requests
import json

TOKEN = "MTM0NDA5MjI0ODI5OTUzNjQzMA.G5SDi-.HemuHaGBegM4HSv8mEtbOqG6PYo3YnVBChSe2A"
API_URL = "https://5xbs2ztrxh.execute-api.sa-east-1.amazonaws.com/GrehServMine"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!start"):
        await message.channel.send("🟢 Iniciando o servidor...")

        response = requests.post(API_URL, json={"action": "start"})
        data = response.json()

        if "ip" in data:
            await message.channel.send(f"✅ Servidor iniciado! IP: `{data['ip']}`")
        else:
            await message.channel.send("⚠️ Servidor iniciado, IP: 18.231.28.175:26565.")
    elif message.content.startswith("!status"):
        await message.channel.send("🟢 Iniciando a consulta...")
        response = requests.post(API_URL, json={"action": "status"})
        data = response.json()
        if "ip" in data:
            await message.channel.send(f"✅ Servidor iniciado! IP: `{data['ip']}`")
        else:
            await message.channel.send("⚠️ Servidor iniciado, mas o IP ainda não está disponível.")
    
    elif message.content.startswith("!stop"):
        response = requests.post(API_URL, json={"action": "stop"})
        await message.channel.send("🔴 Parando o servidor...")

client.run(TOKEN)
