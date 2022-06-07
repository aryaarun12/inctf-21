# MAL3FIC3NT

## Challenge Description 

My friend is stuck somewhere. He is trying to communicate something with me. Can you help me figure it out? 

## Challenge file

[Primary link](https://github.com/aryaarun12/inctf-21/blob/main/Finals/MAL3FIC3NT/Admin/mal.pcap)

## Write up

+ Analyse the packets transferred between the ip `172.16.120.5` and `172.16.100.101`
+ Some packets are evil and some are not
+ Extract the reserved bits of those packets i.e 0 and 1
+ [Convert](https://bahamas10.github.io/binary-to-qrcode/) those bits to a QR code  
+ QR code leads to a pastebin link which has the flag

Scapy script to extract the bits.
```
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
```
Converted to QR code:
![](https://github.com/aryaarun12/inctf-quals-21/blob/main/Hash%20Browns/Assets/org%20(1).png?raw=true)
## Flag 

inctf{H3ll_1s_3mpTy_aLL_th3_d3v1ls_ar3_h3r3}

## Author 
[rayst4rk](https://twitter.com/rayst4rk) & [Chetak](https://twitter.com/Sampath53509318)  
