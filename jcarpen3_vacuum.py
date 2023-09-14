from vacuum import VacuumAgent
import random

class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        self.squares_visited = set()
        self.turn_off = False

    def program(self, percept):
        bump, status = percept

        current_square = (self.x, self.y)
        self.visited_squares.add(current_square)

        if status == 'Dirty':
            self.turn_off = False
            return 'Suck'
        
        else:
            if self.turn_off:
                return 'Turnoff'
            
            else:
                possible_actions = [action for action in self.possible_actions if self.move_is_valid(action)]
                unvisited_squares = [action for action in possible_actions if self.get_location_from_action(action) not in self.visited_squares]
            
            if unvisited_squares:
                next_action = random.choice(unvisited_squares)
                self.visited_squares.add(self.get_location_from_action(next_action))
                return next_action
            else:
                self.turn_off = True
                return 'NoOp'  # Stay in place if all squares are visited
        
       
