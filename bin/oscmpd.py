#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os.path
import sys
sys.path.insert(0, os.path.normpath(os.path.abspath(__file__) + '/../../src'))
from osc_mpd import OSC_MPD

o = OSC_MPD()
o.serve_forever()
