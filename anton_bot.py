import discord
import random
import os

TOKEN = os.getenv('DISCORD_TOKEN')

chigurh_quotes = {
    "heads": [
        "What's the most you ever lost on a coin toss?",
        "You have to think about how you came to be here. 'Heads' was always your path.",
        "This coin traveled here the same way I did.",
        "Now, heads... And everything is as it should be."
    ],
    "tails": [
        "The coin don’t have no say. It’s just you.",
        "You think that when you wake up in the morning yesterday don’t count. But yesterday is all that does count.",
        "If it’s tails, then this is the end of the road for that choice.",
        "Everything rides on this moment. And you called tails..."
    ]
}

# Nastavení intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Bot se připojí k serveru
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Funkce pro vyhodnocení hodu
async def handle_coin_toss(message, mentioned_user=None):
    result = random.choice(["heads", "tails"])
    quote = random.choice(chigurh_quotes[result])
    
    if mentioned_user:
        response = f"{message.author.display_name} tossed the coin for {mentioned_user.display_name}.\nThe coin has spoken: **{result}**.\n\n{quote}"
    else:
        response = f"{message.author.display_name}, the coin has spoken: **{result}**.\n\n{quote}"

    await message.channel.send(response)

# Bot zpracuje příkaz od uživatele
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.guild and message.content.startswith('/cointoss'):
        if message.mentions:
            mentioned_user = message.mentions[0]
            await handle_coin_toss(message, mentioned_user)
        else:
            await handle_coin_toss(message)
    else:
        await message.channel.send("This command works only in a server channel.")

client.run(TOKEN)
