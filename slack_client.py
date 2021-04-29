#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kampamocha
"""
import os
from dotenv import load_dotenv
from slack_sdk import WebClient

#%% Load environment variables
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_USER_TOKEN = os.getenv("SLACK_USER_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

class SlackClient():

    def __init__(self, bot_token=SLACK_BOT_TOKEN, user_token=SLACK_USER_TOKEN, channel=SLACK_CHANNEL):
        self.bot_token = bot_token
        self.user_token = user_token
        self.channel = channel
        self.user_client = WebClient(token=self.user_token)
        self.bot_client = WebClient(token=self.bot_token)

    def send_message(self, text):
        response = self.bot_client.chat_postMessage(channel=self.channel, text=text)
        return response

    def set_status(self, profile):
        response = self.user_client.users_profile_set(profile=profile)
        return response
