import operator


# select_condorcet_winner derives the candidate with maximim wins
# vote_result - dictionary, returned by Pairwiser  elect method
# voters_coefs - optional dictionary {voter.label:float}
# returns a list of two elements: label and total score of winner
def select_condorcet_winner(vote_result, voters_coefs=None):
	#todo: add voters coefficients
	if voters_coefs is None:
		voters_coefs = {}
	total_score = {}
	for item in vote_result.keys():
		total_score[item] = len(list(filter(lambda x: x[2], vote_result[item])))
		total_score[item+":v1"] = len(list(filter(lambda x: x[0] is "v1" and x[2], vote_result[item])))
		total_score[item+":v2"] = len(list(filter(lambda x: x[0] is "v2" and x[2], vote_result[item])))

	winner = max(total_score.items(), key=operator.itemgetter(1))[0]
	return (winner, total_score[winner])
