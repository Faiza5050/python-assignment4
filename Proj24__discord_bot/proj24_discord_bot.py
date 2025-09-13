import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Cheer Up!",
    "Hang in There.",
    "You are a Great Person / Bot!"
]

DB_FILE = "data.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {"encouragements": [], "responding": True}

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

db = load_db()

def get_quote():
    response = requests.get("https://api.quotable.io/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def update_encouragement(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements

@client.event
async def on_ready():
    print(f'Logged in as {client.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    if msg.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))

    if msg.startswith("!new"):
        encouraging_message = msg.split("!new ",1)[1]
        update_encouragement(encouraging_message)
        await message.channel.send("New Encouraging Message Added.")

    if msg.startswith("!!del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("!!del",1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("!list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("!responding"):
        value = msg.split("!responding ",1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is On.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is Off.")

keep_alive()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
client.run(TOKEN)
