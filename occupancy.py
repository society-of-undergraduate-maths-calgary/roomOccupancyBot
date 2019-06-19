#!/usr/bin/env python3
import discord

import random
import asyncio
import subprocess
import socket

#from pickle import load, dump
import os
from os.path import isfile, getcwd
#from datetime import datetime

TOKEN = os.environ["ROOMBOT_ACCESS_TOKEN"]

client = discord.Client()

ROOT_DIR = getcwd()

channels = []
fChanName = ROOT_DIR + "channels.dat"

log = open(ROOT_DIR + "data.log", "a", encoding="utf8")

async def shouldMessage():
    pass

async def fireMessage(done=False):
    while not done:
        Log("Will I send a message? %s" % shouldp)
        msg = "How many people are there in the room ?"
        await asyncio.esnure_future(client.send_message(targetChan, msg))
        await asyncio.sleep(5)

#Event Handlers
@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_ready():
    Log("Logged in as")
    Log(client.user.name)
    Log(client.user.id)
    Log("-------------")

    for server in client.servers:
        Log(server, end=":\n")
        for chan in server.channels:
            Log("\t", end="")
            Log(chan, end=", ")
            Log(chan.id)


    Log("Sending first message, with room in state: %s" % openp)

    asyncio.ensure_future(fireMessage())


if __name__ == "__main__":
    if isfile(fChanName):
        with open(fChanName, "rb") as f:
            channels = load(f)
    client.run(TOKEN)
