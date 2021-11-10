# AutoTwitchFollowBot
Automatically send commands to send Twitch followers to any Twitch account. You just need to be in a Twitch follow bot Discord server!

> :warning: **This program uses a Discord self bot**: It is against Discord's TOS. Use this at your own risk or for educational purposes only.

### How does it work?
This bot will log into your Discord account and send messages in any typical Twitch follow bot Discord server at set intervals. It will also automatically stop when it has reached the set amount of followers that you set when you run the bot.
You will need to join a Twitch follow bot Discord server to run this bot.

### Screenshots
![Image 1](https://i.ibb.co/rHfnJmf/Screenshot-2021-11-10-180340.png)\
![Image 2](https://i.ibb.co/F3CftWF/Screenshot-2021-11-10-180321.png)

### How do I set this up?
- Download the files [here](https://github.com/thomaskeig/AutoTwitchFollowBot/archive/refs/heads/main.zip) and unzip the folder.
- Open up command prompt (or command line if you're using linux) and install the required packages, `discord` and `pyyaml`. You can do this by using the command `pip install discord && pip install pyyaml` on Windows and `sudo pip install discord && sudo pip install pyyaml` on Linux.
- Open `settings.yml` and change the settings to suit your needs. If you are not in a follow bot server yet, you can find a list below.
- Run the bot by opening up command promt in the folder that `main.py` is located in and type `python main.py`.
- You will be asked how many followers you want approximately. Type in the number you wish for and hit enter. The bot will now give you followers based on the settings you have previously set and show you statistics along the way.

### But, are you going to steal my Discord token
No, once you download the files I cannot see anything you change in the file. If you don't trust me you can always look at the source code!

### Follow bot Discord Servers
These servers are known to work pretty much 100% of the time:
- https://discord.gg/4FPXmQn3c9
- Message me on Twitter if you find any more (@thomaskeig_)

### YouTube Tutorials
If you make a YouTube tutorial on how to set this up, message me on Twitter at @thomaskeig_ and I'll leave a link here!
