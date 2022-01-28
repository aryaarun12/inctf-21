from scapy.all import *
import binascii

b = ''

pkts = rdpcap('e.pcap')
for p in pkts:
    if 'IP' in p and p[IP].src == '172.16.120.5':
        if p[IP].flags == 'evil':
            b+='1'
        else:
            b+='0'
print(b)
