#! /usr/bin/env python
# -*- coding: utf-8 -*-

from mpd import MPDClient
from OSC import OSCServer
mpc = MPDClient()

server = OSCServer(('0.0.0.0', 8000))
mpc.connect('192.168.69.41', 6600)


def musicManage(addr, tags, data, client_address):
    cmd = addr.strip('/').split('/')[-1]
    mpc.__getattr__(cmd)(*data)

server.addMsgHandler('/bearstech/music/play', musicManage)
server.addMsgHandler('/bearstech/music/pause', musicManage)
server.addMsgHandler('/bearstech/music/next', musicManage)
server.addMsgHandler('/bearstech/music/previous', musicManage)
server.addMsgHandler('/bearstech/music/stop', musicManage)

server.serve_forever()
