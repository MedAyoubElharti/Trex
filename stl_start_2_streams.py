import stl_path
from trex_stl_lib.api import *

import time
import json


# create udp packet

def create_udp_pkt(src_ip):
	
	return STLPktBuilder(
		pkt = Ether() / IP(src=src, dst="10.0.0.10") / UDP(dport=1400) / Raw('x'*20)
	)

def create_udp_pkt(src_ip, teid):

	return STLPktBuilder(
		
		pkt = Ether() / IP(dst="10.0.0.10", src=ip_src) / UDP(sport=2152, dport=2152)
		pkt = pkt / GTP_U_Header(gtp_type=255, E=1, next_ex=0x85, teid= teid)
		pkt = pkt / GTPPDUSessionContainer(type=0, QFI=qfi, NextExtHdr=0)/IP()
	)


def start():
	
	# create client
	c = STLClient()
	
	passed = True
	
	try:	
		# create two streams

		s1 = STLStream(packet=create_udp_pkt("10.0.0.1"),
				mode=STLXCont())

		s1 = STLStream(packet=create_udp_pkt("10.0.0.2"),
				mode=STLXCont())

		# connect to server
		c.connect()

		# reset ports
		c.reset(ports=[0, 1])
		
		# add streams to tx_port (1)
		c.add_streams([s1, s2], ports = [1]) 
		
		# clear stats
		c.clear_stats()

		# set rx_port (0) as promiscuous mode
		c.set_port_attr(ports=[0], promiscuous=True)
		
		# start injecting packets:
		print("Injecting 10 Mpps on ports 1 for 30s .........")
		c.strat(ports=[1], mult="10mpps", duration = 30)

		#
		c.wait_on_traffic(ports=[1])

		# get stats 
		stats = c.get_stats()

		print(json.dumps(stats[1], indent=4,
						separators=(',', ': '), sort_keys=True))
		print(json.dumps(stats[0], indent=4,
						separators=(',', ': '), sort_keys=True))

		lost_a = stats[1]["opackets"] - stats[0]["ipackets"]

		print("packes lost from 1 --> 0: {0} pkts".format(lost_a))

		if (lost_a == 0):
			passed = True
		else:
			passed = False
	
	except STLError as e:
		passed = False
		print(e)

	finally:
		c.disconnect()
		
	if passed:
		print("\nTest has passed \n")
	else:
		print("\nTest has failed ")


start()	