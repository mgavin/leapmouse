# -*- coding: utf-8 -*-
"""

Description:
Main file for this project. This project intends to simulate simple actions with the mouse using the Leap Motion device.

Such as moving the mouse cursor, clicking with it, and moving windows. Secondary intentions
are to try to improve control between the LeapMotion device and desktop interaction.
"""

from pymouse import PyMouse

mouse = PyMouse()
screen_width, screen_height = mouse.screen_size()

def point_with_finger(normalized_pos):
    posx = normalized_pos.x * screen_width
    posy = screen_height - normalized_pos.y * screen_height

    mouse.move(posx, posy)
