#!/usr/bin/env python

from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = False

files = [ 'mandel.msp',
          'mexhat1.msp',
          'mexhat2.msp',
          ]


 
def test(f):
    try:
        im = Image.open(f)
        im.show()
        im.save(f.replace('.msp','.png'), format='PNG')
    except Exception as msg:
        print ("Could not open %s" %f)
   

for f in files:
    test(f)
