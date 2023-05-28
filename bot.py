import discord as disc
from pep_talk_generation import*
from open_ai import *
import asyncio


def run_discord_bot():
    TOKEN = open("discord_creds.gitignore","r").read().strip()
    
    #intents are a feature of Discord that tells the gateway exactly which events to send your bot.
    intents = disc.Intents.default()
    intents.message_content = True
    #create client pass intents in
    client = disc.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}")
    
    @client.event
    #read messages
    async def on_message(message):
        username = str(message.author)
        user_message = str(message.content).lower().strip()
        channel = str(message.channel)
        server_name = str(message.guild)
        print(f"User: {username}\nSaid: {user_message}\nChannel:{channel}")

        if username==client.user:
            return  
        
        if user_message.startswith("hello peptalk bot"):
            await message.channel.send(f"Hello {username}!")
            return
        
        if user_message.startswith("!help"):
            await message.channel.send(f"""
            Help will always be given at {server_name}\n\n
            
            **Say hi with:** hello pep talk bot\n
            **Get a pep talk with:** !peptalk\n
            **Echo your message with:** !echo\n
            **Speak with AI buy summoning it with:** !SummonAI\n      
            """)       
            return
        
        if user_message.startswith("!echo"):
            echoed_message = user_message.replace("!echo","> ")
            await message.channel.send(echoed_message)
            return
        
        if user_message.startswith("!peptalk"):
            await message.channel.send(pep_talk_generation())
            return

        if user_message.startswith("!summonai"):
            await message.channel.send("How can I help you?")

            def check(new_message):
                #check for user response.
                return message.author == new_message.author
            
            while True:
                try:
                    #wait for message. timeout in 2 min
                    new_message = await client.wait_for("message",timeout=120.0,check=check)
                except asyncio.TimeoutError:
                    await message.channel.send("TIMEOUT")
                    break
                else:
                    if new_message.content.lower()=="conversation over":
                        await message.channel.send("conversation ended")
                        break
                    await message.channel.send (chat(new_message.content))
    
    client.run(TOKEN)
