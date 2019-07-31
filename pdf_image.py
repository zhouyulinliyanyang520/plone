from __future__ import print_function
import os, sys
from PIL import Image


k = ["./image/timg.jpg"]
# for infile in sys.argv[1:]:
for infile in k:
    f, e = os.path.splitext(infile)
    print(f)
    outfile = f + ".png"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("cannot convert", infile)


size=(128,128)
for infile in k:
    outfile = os.path.splitext(infile)[0]+".thumbnail"
    if outfile != infile:
          try:
               im  = Image.open(infile)
               im.thumbnail(size)
               im.save(outfile,'JPEG')
          except IOError:
             print("cannot convert", infile)

im = Image.open("./image/timg.jpg")

# print_function(im.format, im.size, im.mode)
print(im.format, im.size, im.mode)
