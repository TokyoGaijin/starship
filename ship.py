import pygame
import os

class Ship(object):
    def __init__(self, surface, startX, startY, shipClass = "scout"):
        self.surface = surface
        self.startX = startX
        self.startY = startY
        self.shipClass = shipClass
        self.name = None
        self.shields = 100
        self.hull = 100
        self.phasers = 100
        self.torpedoes = 0
        self.max_warpSpeed = 0
        self.current_speed = 0
        self.senior_staff = []
        self.officers = 0
        self.enlisted = 0
        self.crew = len(self.senior_staff) + self.officers + self.enlisted



    def build_ship(self):
        pass