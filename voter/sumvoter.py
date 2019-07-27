class SumVoter:
    def __init__(self, label):
        self.votes_done = 0
        self.label = label

    def vote(self, c1 ,c2):
        self.votes_done += 1
        return sum(c1.properties) >= sum(c2.properties)
        