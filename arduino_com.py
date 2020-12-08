# Author: Rembie01
# Date: 8 dec 2020
# Source:https://forum.arduino.cc/index.php?topic=225329.msg1810764#msg1810764
import serial


class ArduinoCom:
    def __init__(self, port="COM3", baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
        self._startmarker = 60
        self._endmarker = 62

    def send_to_arduino(self, string):
        self.ser.write(string.encode('utf-8'))

    def recover_from_arduino(self):
        ck = ""
        x = "z"
        bytecount = -1

        while ord(x) != startMarker:
            x = self.ser.read()

        while ord(x) != self._endmarker:
            if ord(x) != self._startmarker:
                ck = ck + x.decode("utf-8")
                bytecount += 1
            x = self.ser.read()
        print(ck)

        return ck

    def wait_for_arduino(self):
        msg = ""
        while msg.find("Arduino is ready") == -1:
            while self.ser.inWaiting() == 0:
                pass
            msg = self.recover_from_arduino()
            print(msg)
            print()

    def send(self, string):
        wait_for_reply = False

        if not wait_for_reply:
            self.send_to_arduino(string)
            print("Sent from PC -- " + string)
            wait_for_reply = True

        if wait_for_reply:
            while self.ser.inWaiting() == 0:
                pass

            received = self.recover_from_arduino()
            print("Reply Received  " + received)
