from discord.ext import commands, tasks
import yaml

with open('./settings.yml') as file:
    settings = yaml.load(file, Loader=yaml.FullLoader)

    try:
        user_token = settings['user_token']
        command = settings['command']
        twitch_bot_channel = settings['twitch_bot_channel']
        twitch_bot_channel = int(twitch_bot_channel)
        followers_per_command = settings['followers_per_command']
        followers_per_command = int(followers_per_command)
        command_cooldown = settings['command_cooldown']
        command_cooldown = int(command_cooldown)

    except Exception as e:
        print(f'Error whilst loading settings: {e}')

# --------- # --------- # --------- # --------- # --------- # --------- # --------- #

followers_to_gain = int(input('How many followers do you want to gain? (More or less) >> '))
print('Starting bot...')
times_to_run = round(followers_to_gain / followers_per_command)
followers_sent = 0

bot = commands.Bot(command_prefix="f5894h474gfgh4884h98", self_bot=True)
# Prefix is random so it's not accidentally triggered. I suggest changing this slightly if you can before running


@bot.event
async def on_ready():
    get_followers.start()


@tasks.loop(minutes=command_cooldown)
async def get_followers():
    global times_to_run, followers_sent, command_cooldown
    if times_to_run > 1:

        channel = bot.get_channel(int(twitch_bot_channel))
        await channel.send(command)
        followers_sent += followers_per_command

        followers_to_go = followers_to_gain - followers_sent
        print('\n\n\n\n\n--------- * * * ---------')
        print(f'Sent {followers_per_command} followers')
        print(f'{followers_sent}/{followers_to_gain} followers sent')
        print(f'{times_to_run} more commands to send')
        print(f'{followers_to_go} followers to go')
        print(f'ETA: {round((followers_to_go / followers_per_command) * command_cooldown)} minutes')
        print('--------- * * * ---------')

        times_to_run += -1

    else:
        print('All followers have been sent!')
        exit()


bot.run(user_token, bot=False)
