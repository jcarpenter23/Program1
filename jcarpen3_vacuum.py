from vacuum import VacuumAgent
import random

class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        self.direction = 'Right'
        self.squares_cleaned = set()


    def program(self, percept):
        dirt, status = percept
        
        possible_directions = ['Up', 'Down', 'Right', 'Left']
        
        if dirt == "Dirty":
            return 'Suck'
        
        elif status == 'Bump':
            possible_directions.remove(self.direction)
            self.direction = random.choice(possible_directions)
        
        
        elif status == 'Clean':
            self.direction = random.choice(possible_directions)
            
        return self.direction
            
            
            
    
       
