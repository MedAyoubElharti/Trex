import datetime
import json
import pprint
import time

import stl_path
from trex.stl.api import *
from Plotter import Plotter

#ports
tx_port = 1
rx_port = 0

# create client
c = STLClient()

# connect to server
c.connect()

#reset ports
c.reset(ports=[tx_port, rx_port])


#inject packets using console-like command

print(
	"\nInjecting packets on port {0}\n".format(tx_port)
)

c.start_line("-f /opt/trex/v2.97/stl/AGF_stream/gtp_1pkt_simple_2stream.py -m 20.5gbps -p 1")
