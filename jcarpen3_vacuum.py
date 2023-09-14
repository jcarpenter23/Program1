from vacuum import VacuumAgent
import random

class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        self.direction = 'Right'
        self.squares_cleaned = set()


    def program(self, percept):
        bump, status = percept
        possible_directions = ['Up', 'Down', 'Right', 'Left']
        
        
        if status == 'Dirty':
            self.squares_cleaned.add(self.location)
            return 'Suck'
        
        if bump:
            possible_directions = ['Up', 'Down', 'Right', 'Left']
            possible_directions.remove(self.direction)
            self.direction = random.choice(possible_directions)
            return self.direction

        
        next_square = self.get_next_square()
        if next_square in self.squares_cleaned:
            return self.direction
        else:
            return 'Suck'
            
        return self.direction

    def get_next_square(self):
        x, y = self.location
        if self.direction == 'Up':
            return (x, y + 1)
        elif self.direction == 'Down':
            return (x, y - 1)
        elif self.direction == 'Right':
            return (x + 1, y)
        elif self.direction == 'Left':
            return (x - 1, y)

            
