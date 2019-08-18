from voter.sumvoter import *
from voter.secondvoter import *
from voter.improved_voter import *
from candidate.generators.random_generator import Random_generator
from pairwise_tester.pairwise_tester import Pairwiser
from local_utils.utils import *


def main():
	print("Start")
	candidates = Random_generator(3).generate(1000)
	voters = [SumVoter("v1")] #, SecondVoter("v2")]
	pw = Pairwiser(voters, candidates)
	result = pw.elect(False)
	winner = select_condorcet_winner(result)
	print("Winner is: " + winner[0] + " ;total score: " + str(winner[1]) + " ;properties:")
	print(list(filter(lambda x: x.label is winner[0], candidates))[0].properties)
	print("full election results for " + winner[0])
	print(result[winner[0]])
	print(voters[0].votes_done)

	print("--------------------------------")
	voters = [ImprovedVoter("v1", 0.1, 1000)]
	pw = Pairwiser(voters, candidates)
	result = pw.elect(False)
	winner = select_condorcet_winner(result)
	print("Winner is: " + winner[0] + " ;total score: " + str(winner[1]) + " ;properties:")
	print(list(filter(lambda x: x.label is winner[0], candidates))[0].properties)
	print("full election results for " + winner[0])
	print(result[winner[0]])
	print(voters[0].votes_done)


if __name__ == "__main__":
	main()