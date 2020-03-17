#!/usr/bin/env python3
# Use: ps -ef | grep python
# And then kill <pid> to stop this script.
import sys, socket, sense_hat, time

def IP_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("198.41.0.4", 53))
        answer = s.getsockname()
        s.close()
        return answer[0] if answer else None
    except socket.error:
        return None

def display_IP_address():
    sense.show_message("IPv4: " + str(IP_address()))

sense = sense_hat.SenseHat()

while True:
    sense.clear()
    display_IP_address()
    time.sleep(10)
