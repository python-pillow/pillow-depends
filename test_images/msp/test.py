#!/usr/bin/env python

from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = False

files = ['BLK.MSP',
         'BLU.MSP',
         'FLAG_B24.MSP',
         'GRN.MSP',
         'MARBLES.MSP',
         'RED.MSP',
         'TRU256.MSP',
         'VENUS.MSP',
         'WHT.MSP',
         'YEL.MSP'
         ]

def test(f):
    try:
        im = Image.open(f)
        im.show()
        im.save(f.replace('.MSP','.png'), format='PNG')
    except Exception as msg:
        print ("Could not open %s" %f)
   

for f in files:
    test(f)
