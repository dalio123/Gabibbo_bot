#dipendenze non toccare
import discord
from discord.ext import commands
import random
from voti import voto
from lunghezza import lung
from discord.ext.commands import Bot

client = discord.ext.commands.Bot(command_prefix = "!");
#variabili

#client = Bot("!")


#token da cambiare se non va
TOKEN = 'token'

#client = discord.Client()

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
#stop

	if user_message.lower() == '!r':
		risposta = random.choice(voto)
		
		await message.channel.send(risposta)

	elif user_message.lower() == '!l':
			lunghezz = random.choice(lung)
			await message.channel.send(lunghezz)



	return




#	if user_message.lower() == '!r':
#		risposta = f'Bel cazzo, molto succoso, è proprio rosso come me, si merita un bel {random.randrange(11)}'
#		await message.channel.send(risposta)
#	return



client.run(TOKEN)