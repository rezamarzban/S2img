# Importing Image from PIL package 
from PIL import Image
import math
from random import random
      
# creating a image object
image = Image.open(r'out.png')

width, height = image.size

file = 'out.mp3'

f = open(file, 'wb')

bytex = 0
text = ''

i= 0
  
for x in range(1, width-1, 2):
    print('Progress: ',math.ceil(1000*x/width)/10,'%',end='\r')
    for y in range(1, height-1, 2):
    	rgb= image.getpixel((x,y))
    	r= rgb[0]
    	g= rgb[1]
    	b= rgb[2]
    	rgb1= image.getpixel((x+1,y))
    	r1= rgb1[0]
    	g1= rgb1[1]
    	b1= rgb1[2]
    	bit12= r1 - r
    	bit34= g1 - g
    	bit56= b1 - b
    	rgb2= image.getpixel((x+1,y+1))
    	r2= rgb2[0]
    	g2= rgb2[1]
    	b2= rgb2[2]
    	bit78= r2 - r
    	bit910= g2 - g
    	bit1112= b2 - b
    	rgb3= image.getpixel((x,y+1))
    	r3= rgb3[0]
    	g3= rgb3[1]
    	b3= rgb3[2]
    	bit1314= r3 - r
    	bit1516= g3 - g
    	bit1718= b3 - b
    	
    	if (i - (8 * math.floor(i/8))) == 0:
    		text= text + chr(bytex)
    		bytex = 0
    	bytex = bytex + ((bit1718) * pow(4, int((i - (8 * math.floor(i/8)))/2)))
    	
    	i= i+2
    	
    	byte1= (bit12*64) + (bit34*16) + (bit56*4) + bit78
    	f.write(byte1.to_bytes(1, 'big'))
    	byte2= (bit910*64) + (bit1112*16) + (bit1314*4) + bit1516
    	f.write(byte2.to_bytes(1, 'big'))

print(text)
  
f.close()