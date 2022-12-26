#!/usr/bin/env python
from samplebase import SampleBase
import draw as DRAW
import time
import sys
from rtmidi.midiutil import open_midiinput



class MidiLines(SampleBase):
    """
    Mimics the IKEA Frekvens changing row pattern
    """
    def __init__(self, *args, **kwargs):
        self.width = 32
        self.height = 32
        self.bpm = 75.0
        self.midi_port = 1
        self.midi_offset_led = 65
        self.keys_held = []
        self.midiin, self.port_name = open_midiinput(self.midi_port)
        super(MidiLines, self).__init__(*args, **kwargs)

    def run(self):
        count = 0
        #m = len(self.rowPatterns)-1
        i=0

        print("Entering main loop. Press Control-C to exit.")
        try:
            timer = time.time()
            while True:
                msg = self.midiin.get_message()

                if msg:
                    message, deltatime = msg
                    timer += deltatime
                    if (len(message)>=2):
                        note = int(message[1]) - self.midi_offset_led
                        velocity = int(message[2])
                        #print("[%s] @%0.6f %r" % (port_name, timer, message))
                        #print("Note: %d, Velocity: %d" % (note,velocity))
                        if (velocity > 0):
                            self.matrix.Clear()
                            self.keys_held.append(note)
                            DRAW.DrawColumns(self.matrix, self.keys_held)
                        else:
                            try:
                                self.keys_held.remove(note)
                            except:
                                pass

                #time.sleep(60.0/(self.bpm*4))
                time.sleep(0.01)
        except KeyboardInterrupt:
            print('')
        finally:
            print("Exit.")
            self.midiin.close_port()
            del self.midiin        

        # while count < 1024:
        #     patternIndex = m - abs(i % (2*m) - m)
        #     rows = self.rowPatterns[patternIndex]
        #     
        #     DRAW.DrawRows(self.matrix, rows)
        #     count += 1
        #     time.sleep(60.0/(self.bpm*4))
        #     i+=1
            
# Main function
if __name__ == "__main__":
    grayscale_block = MidiLines()
    if (not grayscale_block.process()):
        grayscale_block.print_help()

