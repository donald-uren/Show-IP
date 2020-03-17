#!/usr/bin/env python3
# Use: ps -ef | grep python
# And then kill <pid> to stop this script.
# Or use joystick in any fashion to exit program
import sys, socket, sense_hat, time


def ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("198.41.0.4", 53))
        answer = s.getsockname()
        s.close()
        return answer[0] if answer else None
    except socket.error:
        return None


def display_ip_address():
    sense.show_message("IPv4: " + str(ip_address()))


sense = sense_hat.SenseHat()

# Updated loop to exit when joystick is used and clear screen on interrupts from keyboard
try:
    joystick_used = False
    while joystick_used is not True:
        sense.clear()
        display_ip_address()
        # Check for events on joystick while message was scrolling
        joystick_event_list = sense.stick.get_events()
        if (len(joystick_event_list)) is not 0:
            joystick_used = True
        else:
            time.sleep(10)

except KeyboardInterrupt:
    sense.clear()
