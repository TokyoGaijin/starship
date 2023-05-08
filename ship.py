import pygame
import os
import random

alert_status = ["green", "yellow", "red"]
alert_avatar = [pygame.image.load(os.path.join("sprites", "green.png")),
                pygame.image.load(os.path.join("sprites", "yellow.png")),
                pygame.image.load(os.path.join("sprites", "red.png"))]

class Ship(object):
    def __init__(self, surface, startX, startY, shipClass = "scout"):
        self.surface = surface
        self.startX = startX
        self.startY = startY
        self.shipClass = shipClass
        self.name = None
        self.registry = None
        self.ship_avatar = None
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
        self.alert = alert_status[0]
        self.alert_posX = 495
        self.alert_posY = 39



    def build_ship(self, ship_name):
        if self.shipClass == "oberth":
            self.ship_avatar = pygame.image.load(os.path.join("sprites", "oberth.png"))
            backreg = random.randrange(10, 100)
            self.name = "Grissom" if backreg == 38 else ship_name
            self.registry = f"NCC-6{backreg}"




    def draw_alert(self):
        active_alert = None
        if self.alert == alert_status[0]:
            active_alert = alert_avatar[0]
        if self.alert == alert_status[1]:
            active_alert = alert_avatar[1]
        if self.alert == alert_status[2]:
            active_alert = alert_avatar[2]

        self.surface.blit(active_alert, (self.alert_posX, self.alert_posY))