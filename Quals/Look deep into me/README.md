# Look deep into me

## Challenge Description 

You can fool a person into going to see a movie with a good trailer

## Challenge file

[Primary link](https://github.com/aryaarun12/inctf-quals-21/blob/main/Look%20deep%20into%20me/Assets/deep.pdf)

## Write up
The given pdf is password protected.

By analysing the hexdump of the file, near to the `trailer` of the pdf, we can see the hexdump of a `PNG` embedded in a reverse manner.
![](https://github.com/aryaarun12/inctf-quals-21/blob/main/Look%20deep%20into%20me/Assets/1.png?raw=true)

Extracting this png will give the flag. Here's a simple script to extract the png
```import codecs
with open('deep.pdf', 'rb') as p:
	pp =p.read().hex()
	ppp=codecs.decode(pp,"hex")
	k=ppp[::-1]
with open('deep.png', 'wb') as m:
	m.write(k[203:])
```
![](https://github.com/aryaarun12/inctf-quals-21/blob/main/Look%20deep%20into%20me/Assets/deep.png?raw=true)

Hints: 
With`strings` command we can see b64 string after EOF of the pdf which will decode to `iloveyou3000` which is the password of the pdf. 

On opening the pdf there is poem given. With just googling we can find that it a poem named [The Strings](https://www.poemhunter.com/poem/the-strings/) which is a hint to go back and analyse the strings
## Flag 

inctf{HERE'5_YOUR_FL4G!!}

## Author 
[rayst4rk](https://twitter.com/rayst4rk)
