# Importing Image from PIL package 
from PIL import Image
import math
from random import random
      
# creating a image object
imagefile = '/storage/emulated/0/DCIM/ReactNative-snapshot-image1255718387.jpg'

image = Image.open(imagefile)

width, height = image.size

img = Image.new('RGB', (width, height), (0, 0, 0))

file = '/storage/1E39-1F00/Download/Yas - Lal.mp3'

f = open(file, 'rb')

contents = f.read()

text = 'file =' + file + ' && ' + 'imagefile =' + imagefile + ' && ' + 'storedbytes =' + 'xxxx'

length = len(text)

#for l in range(length):
#	print(ord(text[l]))

i = 0
j = 0
  
for x in range(1, width-1, 2):
    print('Progress: ',math.ceil(100*x/width),'%',end='\r')
    for y in range(1, height-1, 2):
    	rgb= image.getpixel((x,y))
    	r= rgb[0]
    	g= rgb[1]
    	b= rgb[2]
    	rcplx= abs(r-4)
    	gcplx= abs(g-4)
    	bcplx= abs(b-4)
    	img.putpixel( (x, y), (rcplx, gcplx, bcplx))
    	byte1= contents[i]
    	byte2= contents[i+1]
    	i= i+2
    	bit12= (byte1 >> 6) & 0x3
    	bit34= (byte1 >> 4) & 0x3
    	bit56= (byte1 >> 2) & 0x3
    	bit78= (byte1) & 0x3
    	bit910= (byte2 >> 6) & 0x3
    	bit1112= (byte2 >> 4) & 0x3
    	bit1314= (byte2 >> 2) & 0x3
    	bit1516= (byte2) & 0x3
    	bit1718= 0
    	if j < (length*8):
    		bit1718= (ord(text[math.floor(j/8)]) >> (j - (8 * math.floor(j/8)))) & 0x3
    	j= j+2
    	r1= rcplx+bit12
    	g1= gcplx+bit34
    	b1= bcplx+bit56
    	img.putpixel( (x+1, y), (r1, g1, b1))
    	r2= rcplx+bit78
    	g2= gcplx+bit910
    	b2= bcplx+bit1112
    	img.putpixel( (x+1, y+1), (r2, g2, b2))
    	r3= rcplx+bit1314
    	g3= gcplx+bit1516
    	b3= bcplx+bit1718
    	img.putpixel( (x, y+1), (r3, g3, b3))
  
f.close()

img.save('out.png')
