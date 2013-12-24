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

class LeapListener(Leap.Listener):
    def __init__(self, on_frame_func):
        super(LeapListener, self).__init__()
        self.should_continue = False
        self.on_frame_do = on_frame_func

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
        """
        Frame details are gathered here and forwarded to other
        areas to react based on that data. You could say that the
        controller drives the application.
        """
        if not self.should_continue:
            return
        
        #finger movement
        frame = controller.frame()
        if frame.pointables.is_empty and frame.gestures().is_empty:
            return
        
        iBox = frame.interaction_box
        frnt_ptr = frame.pointables.frontmost
        normalized_pos = iBox.normalize_point(frnt_ptr.tip_position)
        
        self.on_frame_do(normalized_pos = normalized_pos)
         
    def state_to_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"
        elif state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"
        elif state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"
        elif state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"
