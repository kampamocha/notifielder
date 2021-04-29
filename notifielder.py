#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: kampamocha
"""
import dbus
import gi.repository.GLib
from dbus.mainloop.glib import DBusGMainLoop

from slack_client import SlackClient

slack = SlackClient()

#%%
def notifications(bus, message):

    args_list = message.get_args_list()
    origin = args_list[0]
    # Avoid repeated notification
    if dbus.String('sender-pid') in args_list[6]:
        return

    print('-----------------------------------------------')
    print(f'Notification from {origin}...')

    # Check if notification comes from Clementine
    if origin == 'Clementine' and args_list[4] != 'Paused':
        song = args_list[3]
        print(song)

        #print("SENDING MESSAGE TO CHANNEL")
        #response = slack.send_message(f':headphones: {song}')
        #print(response['ok'])

        print("CHANGING STATUS ON SLACK")
        profile = {
            "status_text": song,
            "status_emoji": ":headphones:"
        }
        response = slack.set_status(profile)
        print(response['ok'], response['username'])
        return

#%%
DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)

mainloop = gi.repository.GLib.MainLoop()
print("Hearing notifications...")
mainloop.run()