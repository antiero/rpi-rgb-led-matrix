#!/usr/bin/python3
import UdpComms as U
import time

from led_matrix_handler import LEDMatrix

ledMat = LEDMatrix()
if (not ledMat.process()):
    print("Unable to start the LEDMatrix..")
def handleRequestMsg(msg):
    print("Msg: " + msg)
    if (msg == "Clear"):
        ledMat.Clear()
    ledChangeRequest = msg.split(',')
    if (len(ledChangeRequest) < 5):
        return
    x = int(ledChangeRequest[0])
    y = int(ledChangeRequest[1])
    r = int(ledChangeRequest[2])
    g = int(ledChangeRequest[3])
    b = int(ledChangeRequest[4])
    ledMat.SetLED(x,y,r,g,b)
    sock.SendData("LED updated:" + msg)

# Create UDP socket to use for sending (and receiving)
sock = U.UdpComms(udpIP="pizero2.local",portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True, recvbytes=32)

while True:
    data = sock.ReadReceivedData() # read data

    if data != None: # if NEW data has been received since last ReadReceivedData function call
        handleRequestMsg(data) # print new received data

    #time.sleep(1)
