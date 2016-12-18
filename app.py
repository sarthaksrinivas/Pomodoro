#!/usr/bin/env python3

from time import sleep

class Pomodoro(object):
    """The main pomodoro timer.

    Attributes:
        secs: Number of seconds since start of session.
        sessions: Number of sessions completed.
    """

    # Instance Variables
    pass

    # Functions
    def __init__(self):
        self.secs = 0
        self.sessions = 0

        print("Welcome to Pomodoro!")

    def __del__(self):
        pass

    def tick(self):
        self.secs += 1
        sleep(1)

timer = Pomodoro()
