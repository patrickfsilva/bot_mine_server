import discord
import requests
import json

TOKEN = "f04eeb8bc3a2b458680a28d34002ba6ec75dcbc206be08cfd179e63286d3484d"
API_URL = "https://t1r317vrsg.execute-api.sa-east-1.amazonaws.com/default/MinecraftServerControl"

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
            await message.channel.send("⚠️ Servidor iniciado, mas o IP ainda não está disponível.")

    elif message.content.startswith("!stop"):
        response = requests.post(API_URL, json={"action": "stop"})
        await message.channel.send("🔴 Parando o servidor...")

client.run(TOKEN)
