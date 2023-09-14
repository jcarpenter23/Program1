from vacuum import VacuumAgent
import random


class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        self.squares_visited = set()
        self.current_square = (0, 0)
        self.turn_off = False

    def program(self, percept):
        bumped, status = percept

        if action_reach:
            x, y = self.current_square
            dx, dy = square[0] - x, square[1] - y

            if dx == 1:
                return 'Right'
            elif dx == -1:
                return 'Left'
            elif dy == 1:
                return 'Up'
            elif dy == -1:
                return 'Down'

        if get_adjacent_squares:
            x, y = square
            return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        if choose_next_action:
            next_square = self.get_adjacent_ squares(self.current_square)
            for square in next_square:
                if square not in self.square_visited:
                    self.squares_visited.add(square)
                    return self.action_reach(square)

            

            if status == 'Dirty':
                self.turn_off = False
                return 'Suck'

            if not self.turn_off:
                next_action = self.choose_next_action()
                if next_action:
                    return next_action

        return random.choice(self.possible_actions)
