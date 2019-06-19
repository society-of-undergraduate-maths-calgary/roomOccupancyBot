#!/usr/bin/env python3
import discord

import random
import asyncio
import subprocess
import socket

#from pickle import load, dump
import os
from os.path import isfile
from datetime import datetime

import config

client = discord.Client()

ROOT_DIR = os.getcwd()

channels = []
fChanName = ROOT_DIR + "channels.dat"

log = open(ROOT_DIR + "data.log", "a", encoding="utf8")

def Log(msg):
    print(msg)

async def fireMessage(done=False):
    targetChan = client.get_channel(config.TARGET_SERVER_ID)
    #await asyncio.ensure_future(client.send_message(targetChan, msg))
    await asyncio.ensure_future(targetChan.send("Starting up occupancy checkin"))
    while not done:
        Log("Will I send a message? %s")
        msg = "How many people are there in the room ?"
        Log("Now is: %s with hour %s" % (datetime.now(), datetime.now().hour))
        if 10 <= datetime.now().hour <= 17:
            #await asyncio.ensure_future(client.send_message(targetChan, msg))
            await asyncio.ensure_future(targetChan.send(msg))
        await asyncio.sleep(60*60 - datetime.now().minute * 60 - datetime.now().second) # wait until start of next hour

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

    '''for server in client.servers:
        Log(server, end=":\n")
        for chan in server.channels:
            Log("\t", end="")
            Log(chan, end=", ")
            Log(chan.id)'''


    #Log("Sending first message, with room in state: %s" % openp)

    asyncio.ensure_future(fireMessage())


if __name__ == "__main__":
    if isfile(fChanName):
        with open(fChanName, "rb") as f:
            channels = load(f)
    client.run(config.TOKEN)
