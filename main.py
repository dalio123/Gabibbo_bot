#dipendenze non toccare
import discord
import random
from voti import voto

#token da cambiare se non va
TOKEN = 'token'

client = discord.Client()

@client.event
async def on_ready():
  print('Belandi amici di striscia qui è il {0.user} che vi parla'.format(client))

@client.event
async def on_message(message):
	username = str(message.author).split('#')[0]
	user_message = str(message.content)
	channel = str(message.channel.name)
	print(f'{username}: {user_message} ({channel})')

	if message.author == client.user:
		return

	if user_message.lower() == '!r':
		risposta = random.choice(voto)
		await message.channel.send(risposta)
	return

client.run(TOKEN)