from PIL import Image
import math
#from alive_progress import alive_bar
      
# creating a image object
sourcefile = input('Enter image file name that you want to extract stored file from its pixels:')
image = Image.open(sourcefile)

file = input('Enter output filename to saving extracted file to it:')

f = open(file, 'wb')

width, height = image.size

rgb= image.getpixel((width-1, height-4))
byte1= rgb[0]
byte2= rgb[1]
byte3= rgb[2]

rgb= image.getpixel((width-1, height-3))
byte4= rgb[0]

size= (byte1*256*256*256) + (byte2*256*256) + (byte3*256) + (byte4)

print(size, 'bytes are stored in image pixels.')

end = (math.floor(size/3))*3

#print(end)

bytes = 0

filename = ''
k = 1

#with alive_bar(width-1) as bar:
for x in range(1, width):
  	print('Extracting stored file from image pixels: ',math.ceil(100*x/width),'%',end='\r')
  	for y in range(1, height):
  				rgb= image.getpixel((x,y))
  				if bytes < end:
  					f.write(rgb[0].to_bytes(1, 'big'))
  					f.write(rgb[1].to_bytes(1, 'big'))
  					f.write(rgb[2].to_bytes(1, 'big'))
  					bytes = bytes + 3
  				else:
  					if k <= 2048:
  						filename = filename + chr(rgb[1])
  						k = k + 1

print('\n The source file name (including path) which stored in image pixels was:', filename)
print('Manualy rename the "',file,'" output file to the source file name.')
#print(bytes)

rgb= image.getpixel((width-1,height-1))

r= rgb[0]
g= rgb[1]
b= rgb[2]

#print(r,g,b)

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
