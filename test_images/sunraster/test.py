#!/usr/bin/env python

from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = False

files = ['32bpp.ras',
         '4bpp.ras',
         'gray.ras',
         'lena-1bit-raw.sun',
         'lena-1bit-rle.sun',
         'lena-24bit-raw.sun',
         'lena-24bit-rle.sun',
         'lena-8bit-raw.sun',
         'lena-8bit-rle.sun',
         'MARBLES.SUN',
         ]


def test(f):
    try:
        im = Image.open(f)
        im.show()
    except Exception as msg:
        print ("Could not open %s" %f)
   

for f in files:
    test(f)
