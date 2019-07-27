
import itertools


class Pairwiser:
    def __init__(self, voters, candidates):
        self.voters = voters
        self.candidates = candidates
        self.comparison_result = {}

    def elect(self, aloud):
        for candidate_pair in itertools.combinations(self.candidates, 2):
            vote_result, backward_vote_result = [], []

            for voter in self.voters:
                does_first_win = voter.vote(candidate_pair[0], candidate_pair[1])
                vote_result.append([voter.label, candidate_pair[1].label, does_first_win])
                backward_vote_result.append([voter.label, candidate_pair[0].label, not does_first_win])
            
            if aloud:
                print(candidate_pair[0].label + ":" + candidate_pair[1].label, vote_result)

            #saving a to b comparison result
            if self.comparison_result.get(candidate_pair[0].label):
                self.comparison_result[candidate_pair[0].label].extend(vote_result)
            else:
                self.comparison_result[candidate_pair[0].label] = vote_result

            #saving b to a compatison result
            if self.comparison_result.get(candidate_pair[1].label):
                self.comparison_result[candidate_pair[1].label].extend(backward_vote_result)
            else:
                self.comparison_result[candidate_pair[1].label] = backward_vote_result
        return self.comparison_result