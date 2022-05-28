from PIL import Image
import math
from alive_progress import alive_bar
      
# creating a image object
image = Image.open('/storage/emulated/0/Download/geeks.png')

file = '/storage/emulated/0/Download/out.rar'

f = open(file, 'wb')

width, height = image.size

rgb= image.getpixel((width-1, height-4))
byte1= rgb[0]
byte2= rgb[1]
byte3= rgb[2]

rgb= image.getpixel((width-1, height-3))
byte4= rgb[0]

size= (byte1*256*256*256) + (byte2*256*256) + (byte3*256) + (byte4)

print(size)

end = (math.floor(size/3))*3

print(end)

bytes = 0

with alive_bar(width-1) as bar:
	for x in range(1, width):
	  	bar()
	  	for y in range(1, height):
	  				if bytes < end:
	  					rgb= image.getpixel((x,y))
	  					f.write(rgb[0].to_bytes(1, 'big'))
	  					f.write(rgb[1].to_bytes(1, 'big'))
	  					f.write(rgb[2].to_bytes(1, 'big'))
	  					bytes = bytes + 3

print(bytes)

rgb= image.getpixel((width-1,height-1))

r= rgb[0]
g= rgb[1]
b= rgb[2]

print(r,g,b)

if r == g:
	if g == b:
		if b == 222:
			rgb= image.getpixel((width-1,height-2))
			f.write(rgb[0].to_bytes(1, 'big'))
			f.write(rgb[1].to_bytes(1, 'big'))

if r == g:
	if g == b:
		if b == 111:
			rgb= image.getpixel((width-1,height-2))
			f.write(rgb[0].to_bytes(1, 'big'))

f.close()