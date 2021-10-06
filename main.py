#=====================================================================================
#
# Author: CalmLakes (Fili)
# Date: 10/4/2021
# Project: Apex Bot
# Description:
# ---------------------------------------------
# This file contains the class responsible for apex related information.The 
# parsing of this data is something that can be sorted out later on by the bot.
# It is this file that will need to be updated as each season comes out and the 
# weapons change.
#
#=====================================================================================
import os
from dotenv import load_dotenv
from apex_class import RandomApex as apex
from bot_class import MyClient


TOKEN = os.getenv('DISCORD_TOKEN')
API_TRACKER_KEY = os.getenv('APEX_API_TRACKER_KEY') 
load_dotenv()


if __name__ == "__main__":
	client = MyClient()
	client.run(TOKEN)