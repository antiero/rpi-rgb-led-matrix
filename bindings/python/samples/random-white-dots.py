#!/usr/bin/env python
from samplebase import SampleBase
import time
import random

class RandomWhiteDots(SampleBase):
    """
    Mimics the IKEA Frekvens random white dot pattern
    """
    def __init__(self, *args, **kwargs):
        self.width = 32
        self.height = 32
        self.bpm = 120.0
        self.beats = 8
        super(RandomWhiteDots, self).__init__(*args, **kwargs)

    def RandomDots(self, qty=32):
        rangeX = (0, 32)
        rangeY = (0, 32)
        radius = 3

        # Generate a set of all points within 200 of the origin, to be used as offsets later
        # There's probably a more efficient way to do this.
        deltas = set()
        for x in range(-radius, radius+1):
            for y in range(-radius, radius+1):
                if x*x + y*y <= radius*radius:
                    deltas.add((x,y))

        randPoints = []
        excluded = set()
        i = 0
        while i<qty:
            self.matrix.Clear()
            x = random.randrange(*rangeX)
            y = random.randrange(*rangeY)
            if (x,y) in excluded: continue
            randPoints.append((x,y))
            i += 1
            excluded.update((x+dx, y+dy) for (dx,dy) in deltas)
        return randPoints

    def DrawPointsMono(self, pts, r=255, g=255, b=255):
        for pt in pts:
            self.matrix.SetPixel(pt[0], pt[1], r,g,b)

    def run(self):
        count = 0

        while count < 1024:
            pts = self.RandomDots()
            self.DrawPointsMono(pts)
            time.sleep(60.0/(self.bpm*self.beats))
            count+=1

# Main function
if __name__ == "__main__":
    grayscale_block = RandomWhiteDots()
    if (not grayscale_block.process()):
        grayscale_block.print_help()

