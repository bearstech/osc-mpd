#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import sys
from optparse import OptionParser

sys.path.insert(0, os.path.normpath(os.path.abspath(__file__) + '/../../src'))
from osc_mpd import OSC_MPD

parser = OptionParser()
parser.add_option("-m", "--mpd", dest="mpd", default='127.0.0.1')
parser.add_option("-p", "--port", dest="port", default=8000)

(options, args) = parser.parse_args()

o = OSC_MPD(osc=('0.0.0.0', options.port), mpd=(options.mpd, 6600))
o.serve_forever()
