# notifielder

Python script that catches desktop notifications and let you handling them as you see fit.

## Requirements

- dbus
- gi.repository.GLib

## Clementine - Slack example

As an example we catch Clementine notifications when the song played change and do one or two things:
- Send the song name to a slack channel.
- Change the user status.

For this to work is necessary to create a Slack App https://api.slack.com/start.