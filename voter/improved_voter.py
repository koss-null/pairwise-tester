import math


class ImprovedVoter:
	def __init__(self, label, winner_delta=0.2, no_competition_border=10):
		self.votes_done = 0
		self.label = label
		# map contains [wins, wins + losses]
		self.win_map = {}
		self.winner_delta = winner_delta
		self.no_competition_border = no_competition_border

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

		first_win = sum(c1.properties) >= sum(c2.properties)

		self._win_map_add(c1, first_win)
		self._win_map_add(c2, not first_win)
		self.votes_done += 1
		return first_win
