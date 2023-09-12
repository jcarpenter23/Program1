from vacuum import VacuumAgent

class Jcarpen3VacuumAgent(VacuumAgent):

    def __init__(self):
        super().__init__()
        # any initialization you want to do here

    def program(self, percept):
        return 'NoOp'
