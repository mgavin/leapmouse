# -*- coding: utf-8 -*-
"""
mousemover.py
should be GPL'd

Description:
Main file for this project. This project intends to simulate simple actions with the mouse using the Leap Motion device.

Such as moving the mouse cursor, clicking with it, and moving windows. Secondary intentions
are to try to improve control between the LeapMotion device and desktop interaction.
"""

from __future__ import absolute_import

import sys
import Leap
from leapmouse.mouselistener import LeapListener
from leapmouse.fingerpointer import point_with_finger

def do_frame_action(*args, **kwargs):
    point_with_finger(kwargs.get('normalized_pos'))
    
def main():
    """
    1. Get the Leap controller.
    2. Connect the Listener to the controller.
    3. Set things up
    4. Make simple interaction for exiting.
    5. ???
    6. Profit?
    """
    listener = LeapListener()
    controller = Leap.Controller()
    
    controller.add_listener(listener)

    print "Diag info printing."
    sys.stdin.readline()
    listener.should_report = True
    
    #Listen until a keypress
    print "Press Enter to quit!"
    sys.stdin.readline()

    controller.remove_listener(listener)
    


if __name__ == "__main__":
    main()
