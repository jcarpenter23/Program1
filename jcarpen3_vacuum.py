from vacuum import VacuumAgent
import random

class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        self.direction = 'Right'
        self.squares_cleaned = set()
        self.last_square = None


    def program(self, percept):
        dirt, status = percept
        
        possible_directions = ['Up', 'Down', 'Right', 'Left']
        
        if dirt == "Dirty":
            return 'Suck'
        
        
        
        if status == 'Clean':
            new_square = random.choice(possible_directions)
            while new_square == self.last_square:
                new_square = random.choice(possible_directions)
                
            self.direction = new_square
            self.last_square = self.direction
            
            
        
        elif status == 'Bump':
            possible_directions.remove(self.direction)
            
            if self.last_square:
                possible_directions.remove(self.opposite_direction(self.last_square))
           
            self.direction = random.choice(possible_directions)
        
            
        return self.direction
    
    def opposite_direction(self, direction):
        
        if direction == 'Up':
            return 'Down'
        
        if direction == 'Down':
            return 'Up'
        
        if direction == "Left":
            return 'Right'
        
        if direction == "Right":
            return "Left"
                   
