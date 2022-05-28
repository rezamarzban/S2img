import os
from PIL import Image
import math

file = input('Enter filename that you want to storing in image pixels (max lenght is 2000 chars including path):')

f = open(file, 'rb')

size = os.path.getsize(file)

k = 0

length = len(file)

height = math.floor(math.sqrt((size+2000)/3)) + 2
width = height + 1

image = Image.new('RGB', (width, height), (0, 0, 0))

byte1 = (size >> 24) & 0xFF
byte2 = (size >> 16) & 0xFF
byte3 = (size >> 8) & 0xFF
byte4 = size & 0xFF

#print(byte1,byte2,byte3,byte4)

image.putpixel((width-1, height-4), (byte1, byte2, byte3))
image.putpixel((width-1, height-3), (byte4, 0, 0))

contents = f.read()

i = 0

print('input file size in bytes:', size)

for x in range(1, width):
	  	print('Storing in image pixels: ',math.ceil(100*x/width),'%',end='\r')
  		for y in range(1, height):
   			if i <= (size-3):
   				r= contents[i]
   				g= contents[i+1]
   				b= contents[i+2]
   				i= i+3
   				image.putpixel((x, y), (r, g, b))
   			else:
   				if k < length:
   					r= 0
   					g= ord(file[k])
   					b= 0
   					k= k+1
   					image.putpixel((x, y), (r, g, b))

#print(i)

delta= size - i

if delta == 2:
    	image.putpixel((width-1, height-1), (222,222,222))
    	r= contents[i]
    	g= contents[i+1]
    	b= 0
    	i= i+2
    	image.putpixel((width-1, height-2), (r, g, b))

if delta == 1:
    	image.putpixel((width-1, height-1), (111,111,111))
    	r= contents[i]
    	g= 0
    	b= 0
    	i= i+1
    	image.putpixel((width-1, height-2), (r, g, b))

#print(i)

image.save('out.png')

f.close()
