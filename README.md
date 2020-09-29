# Telegram Bot - My IP Please

Sends the bot's server's current IP.
Useful for getting a dynamic IP of a machine over distance.

Fill the chat ids and token on the config.py file 
and use the command **_/where_** to receive the 
server IP.

### How to

~~~~
git clone https://github.com/hmarsolla/telegram-bot-get-ip.git
cd telegram-bot-get-ip
pip install -r requirements.txt
~~~~

Create a telegram bot and add the bot token and chat id to the config.py.
Finally start the bot script with `python my_ip_please.py`.


### Docker usage

To build the image, simply go to your repo folder and run

`docker build -t telegram-my-ip .`

You can change the name of the Docker Tag to whatever you want.

After building the image, you can run it with the following command

`docker run -v <<PATH/TO/YOUR/config.py>>:/app/config.py telegram-my-ip`