import pygame
import random
import os
import pyttsx3
import threading

def dice(sides):
    return random.randrange(1, sides + 1)

class Officer:
    def __init__(self, race, rank, name, position, gender = "male", surface = None):
        self.race = race
        self.rank = rank
        self.name = name
        self.department = position
        self.gender = gender
        self.surface = surface # for use with Captain Characters
        self.skill = 0
        self.luck = 0
        self.charm = 0
        self.competency = (None, 0)
        self.engine = pyttsx3.init()
        self.voice = self.engine.getProperty('voices')
        self.avatar = pygame.transform.scale(pygame.image.load(os.path.join("avatars", f"capt_{self.race}_{self.gender}.png")), (67, 82))
        self.avatarX = 339
        self.avatarY = 357
        if self.gender == "male":
            self.engine.setProperty('voice', self.voice[0].id)
        else:
            self.engine.setProperty('voice', self.voice[1 if dice(6) > 3 else 2].id)
        self.isAlive = True
        self.avatarVisible = False

    def train_officer(self):
        bonus = 0
        year1, year2, year3, year4 = 0, 0, 0, 0
        if self.race == "human":
            bonus = dice(20)
            self.skill = dice(10) + bonus
            self.luck = bonus
            self.charm = dice(10)
        if self.race == "andorian":
            bonus = dice(10) if dice(6) > 1 else dice(6)
            self.skill = dice(10) + bonus
            self.luck = dice(20) + bonus
            self.charm = 5 if dice(6) > 1 else 2
        if self.race == "vulcan":
            bonus = dice(20) if dice(6) > 3 else dice(10)
            self.skill = dice(20) + bonus
            self.luck = dice(6)
            self.charm = dice(6)
        if self.race == "tellerite":
            bonus = dice(6)
            self.skill = dice(10) + bonus
            self.luck = dice(20) if dice(6) > 3 else dice(10)
            self.charm = 3 if dice(6) > 3 else 1

        self.competency = (self.department, (dice(6) * 4 if dice(6) > 3 else dice(3) * 4))
        if dice(6) > 3:
            year1, year2, year3, year4 = dice(6),dice(6),dice(6),dice(6)
        else:
            year1, year2, year3, year4 = dice(3),dice(3),dice(3),dice(3)

        self.competency = (self.department, (year1 + year2 + year3 + year4))

    def say(self, quote):
        thread1 = threading.Thread(target=self.engine.say(quote))
        thread2 = threading.Thread(target=self.engine.runAndWait())
        thread1.start()
        thread2.start()



    def draw(self):
        if self.avatarVisible:
            self.surface.blit(self.avatar, (self.avatarX, self.avatarY))



    def __str__(self):
        return f"{self.rank} {self.name}, a/an {self.race}. Current Assignment: {self.position}."

