import random
from candidate.candidate import Candidate

class Random_generator:
    def __init__(self, properties_amount):
        self.properties_amount = properties_amount

    def generate(self, candidates_amount):
        candidates = []
        for i in range(0, candidates_amount):
            candidates.append(
                Candidate("cnd" + str(i),
                random.sample(range(100), self.properties_amount)))
        
        return candidates
