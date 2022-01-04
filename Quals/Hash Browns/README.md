# Hash Browns

## Challenge Description 

My friend and me has been playing a game. I am trying to reconstruct an image sent by him. Can you help me? 

## Challenge file

[Primary link](https://github.com/aryaarun12/inctf-quals-21/blob/main/Hash%20Browns/Assets/hash-browns.pcap)

## Write up

We send one byte at a time and compare it with the original image.If they are same then server sends "Matched byte" signal. If the bytes don't match server sends error message including MD5 hash of the received byte and MD5 hash of the original byte.

Scapy script to reconstruct the PNG. If the byte is matched, add it directly, or if its an errored byte, find the original byte using md5 hash of it.
```
from scapy.all import *
import hashlib
r=rdpcap("hahs-browns.pcap")
happy=open("flag.png","wb")
l=[]
for i in range(256):
    l.append(str(hashlib.md5(str(i).encode()).hexdigest()))
for i in range(len(r)):
    b=len(r[i][TCP].payload)
    c=str(r[i][TCP].payload)
    z=c[c.rfind("=")+1:]
    if(b==14 or b==15 or b==16):
        happy.write(chr(int(z)))
    if(b==109):
        happy.write(chr(l.index(z)))
```
Extracted PNG:

![](https://github.com/aryaarun12/inctf-quals-21/blob/main/Hash%20Browns/Assets/org%20(1).png?raw=true)
## Flag 

inctf{g00d_joB_m4te!!}

## Author 
[Chetak](https://twitter.com/Sampath53509318) & [rayst4rk](https://twitter.com/rayst4rk)
