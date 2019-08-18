from voter.improved_voter import different_cost_point_counter


class SumVoter:
    def __init__(self, label):
        self.votes_done = 0
        self.label = label

    def vote(self, c1 ,c2):
        self.votes_done += 1
        #fixme: this dirty code should be refactored as it done in improved_voter sometimes
        return different_cost_point_counter(c1) >= different_cost_point_counter(c2)
        