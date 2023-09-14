from vacuum import VacuumAgent
import random

class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        self.visited_squares = set()

    def program(self, percept):
        bump, status = percept
        
        current_status = self.location
        
    
        if status == 'Dirty':
            return 'Suck'
        
        
        else:
            possible_actions = [action for action in self.possible_actions if self.move_is_valid(action)]
            undiscovered_squares = [action for action in possible_actions if self.get_location_from_action(action) not in self.square_visted]
            
            if undiscovered_squares:
                next_action = random.choice(undiscovered_squares)
                self.visited_squares.add(self.get_location_from_action(next_action))
                return next_action
            else:
                return random.choice(possible_actions)
