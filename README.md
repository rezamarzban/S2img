# S2img
Store data in image pixels color depth without quality change by Python

By compiling f2p.py (file to pixels) with Python3:
Store any file data to a new image pixels RGB color = Out.png;
Each pixel keep 3 bytes data with this method.

By compiling p2f.py (pixels to file) with Python3:
Extract file which stored in an image pixels RGB color with f2p.py method.

f2color.py and color2f.py store in and extract file from a choosed exiting image pixels color depth without quality change.
Each 4 pixels keep 2 bytes data with this method.
f2color.py and color2f.py are under construction ... !

f2p.py and f2color.py differences:

1- f2p.py store file data to a new image pixels RGB color but f2color.py store file data to an existing image pixels color depth.

2- f2p.py store 3 bytes at each pixel but f2color.py store 2 bytes at each 4 pixels.

3- f2p.py has no limit size to storing file data to image but f2color.py has limit size to storing file data to image depends on image resolution.


