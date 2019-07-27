class SecondVoter:
    def __init__(self, label):
        self.votes_done = 0
        self.label = label

    def vote(self, c1 ,c2):
        self.votes_done += 1
        return c1.properties[1] >= c2.properties[1]