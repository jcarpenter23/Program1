from vacuum import VacuumAgent
import random

class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        self.direction = 'Right'



    def program(self, percept):
        bump, status = percept

        if status == 'Dirty':
            return 'Suck'

        elif bump:
            if self.direction == 'Right':
                self.direction = 'Left'
                return 'Suck'
            elif self.direction == 'Left':
                self.direction = 'Right'
                return 'Suck'
            elif self.direction == 'Up':
                self.direction = 'Down'
                return 'Suck'
            elif self.direction == 'Down':
                self.direction = 'Up'
                return 'Suck'
        
        return self.direction
