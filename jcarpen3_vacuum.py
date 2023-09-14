from vacuum import VacuumAgent
import random

class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        # any initialization you want to do here

    def program(self, percept):
        bump, status = percept

        current_status = self.location
        self.swuare_achieved.add(current_status)

        if status == 'Dirty':
            return 'Suck'
        else:
            return random.choice(self.possible_actions)
