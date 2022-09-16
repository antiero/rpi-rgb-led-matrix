#!/usr/bin/env python
from samplebase import SampleBase
import time

class RowChanger(SampleBase):
    """
    Mimics the IKEA Frekvens changing row pattern
    """
    def __init__(self, *args, **kwargs):
        self.width = 32
        self.height = 32
        self.bpm = 120.0
        self.rowPatterns = self.RowPatterns()
        super(RowChanger, self).__init__(*args, **kwargs)
        
    def RowPatterns(self):
        patterns = ([x for x in range(0,32)],
                    [x for x in range(0,32) if x%2 ==0],
                    [x for x in range(0,32) if x%3 ==0],
                    [x for x in range(0,32) if x%4 ==0],
                    [x for x in range(0,32) if x%5 ==0],
                    [x for x in range(0,32) if x%6 ==0],
                    [x for x in range(0,32) if x%7 ==0],
                    [x for x in range(0,32) if x%8 ==0])
        return patterns
                    
        
    def DrawRow(self, rowIndex, r=255, g=255, b=255):
        for x in range(0, self.width):
            self.matrix.SetPixel(x, rowIndex, r, g, b)        
        
    def DrawColumn(self, colIndex, r=255, g=255, b=255):
        for y in range(0, self.width):
            self.matrix.SetPixel(colIndex, y, r, g, b)
            
    def DrawRows(self, rows, r=255, g=255, b=255):
        """
        rows is a list of integers, defining the row indices to draw
        """
        for row in rows:
            self.DrawRow(row)

    def run(self):
        count = 0
        help(self.matrix)
        m = len(self.rowPatterns)-1
        i=0

        while count < 1024:
            patternIndex = m - abs(i % (2*m) - m)
            rows = self.rowPatterns[patternIndex]
            self.matrix.Clear()
            self.DrawRows(rows)
            count += 1
            time.sleep(60.0/(self.bpm*4))
            i+=1
            
# Main function
if __name__ == "__main__":
    grayscale_block = RowChanger()
    if (not grayscale_block.process()):
        grayscale_block.print_help()

