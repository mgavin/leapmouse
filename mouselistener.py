# -*- coding: utf-8 -*-
"""
leaplistener.py
should be GPL'd

Set up the class interface to collect the Leap frame data.
"""

#import sys
#import time

import Leap
from Leap import KeyTapGesture, ScreenTapGesture

from leapmouse.leapmouse import do_frame_action

class LeapListener(Leap.Listener):
    def __init__(self):
        super(LeapListener, self).__init__()
        self.should_report = False

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        #gesture enabling?
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);

        for dev in controller.devices:
            if dev.is_valid:
                print "device.horizontal_view_angle: {0}\n" \
                    "device.vertical_view_angle: {1}\n" \
                    "device.range: {2}".format(dev.horizontal_view_angle * Leap.RAD_TO_DEG,
                                               dev.vertical_view_angle * Leap.RAD_TO_DEG,
                                               dev.range)


    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        if not self.should_report:
            return
        
        #finger movement
        frame = controller.frame()

        iBox = frame.interactionBox
        frnt_ptr = frame.pointables.frontmost
        normalized_pos = iBox.normalize_point(frnt_ptr.tip_position)
        
        do_frame_action(normalized_pos = normalized_pos)
         
    def state_to_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"
        elif state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"
        elif state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"
        elif state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"
