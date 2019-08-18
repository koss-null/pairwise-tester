import math

from predictor.linear_regression_predictor import LinearRegressionPredictor
from predictor.predictor import Predictor


def sum_point_counter(c):
	return sum(c.properties)


class ImprovedVoter:
	def __init__(self, label, winner_delta=0.2, no_competition_border=10, point_counter=sum_point_counter):
		self.votes_done = 0
		self.label = label
		# map contains [wins, wins + losses]
		self.win_map = {}
		self.winner_delta = winner_delta
		self.no_competition_border = no_competition_border
		self.point_conuter = point_counter

		self.predictor = LinearRegressionPredictor(label, [])
		self.results = []

	def _win_map_add(self, c, does_win):
		item = self.win_map.get(c.label)
		if item is None:
			self.win_map[c.label] = [int(does_win), 1]
		else:
			self.win_map[c.label] = [item[0] + int(does_win), item[1] + 1]

	def vote(self, c1, c2):
		if self.win_map.get(c1.label) is not None and \
				self.win_map.get(c2.label) is not None:

			if self.win_map[c1.label][1] > self.no_competition_border and \
					self.win_map[c2.label][1] > self.no_competition_border and \
					math.fabs(self.win_map[c1.label][0] / self.win_map[c1.label][1] - self.win_map[c2.label][0] / self.win_map[c2.label][1]) > self.winner_delta:
				# here we don't change competition amount since it will bury the one who loose
				# print(c1.label, c2.label, self.win_map[c1.label][0] / self.win_map[c1.label][1] - self.win_map[c2.label][0] / self.win_map[c2.label][1] >= 0)
				return self.win_map[c1.label][0] / self.win_map[c1.label][1] - self.win_map[c2.label][0] / self.win_map[c2.label][1] >= 0

			prediction = self.predictor.predict(c1, c2)
			if prediction is not None:
				return prediction

		first_win = self.point_conuter(c1) >= self.point_conuter(c2)

		self._win_map_add(c1, first_win)
		self._win_map_add(c2, not first_win)
		self.results.append([c1, c2, first_win])
		self.votes_done += 1
		# fixme: 50 is a random number
		if self.votes_done == 100:
			self.predictor.voter_results = self.results
			self.predictor.learn_model()
		return first_win
