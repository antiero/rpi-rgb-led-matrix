#!/usr/bin/env python
from samplebase import SampleBase
import time
import random

class GrayscaleBlock(SampleBase):
    def __init__(self, *args, **kwargs):
        self.width = 32
        self.height = 32
        self.bpm = 120.0
        self.beats = 8
        super(GrayscaleBlock, self).__init__(*args, **kwargs)

    def run(self):


        count = 0

        while count < 1024:
            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            
            count += 1
            self.matrix.SetPixel(x, y, r, g, b)
            time.sleep(60.0/(self.bpm*self.beats))
            
# Main function
if __name__ == "__main__":
    grayscale_block = GrayscaleBlock()
    if (not grayscale_block.process()):
        grayscale_block.print_help()

