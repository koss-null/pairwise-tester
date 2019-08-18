# predictor takes voter results and trying to predict the next vote result
# it assumes that there are some list of numeric properties on which voters relies
# also, it should only use the final prediction results (which of the two candidates won)
# and not the intermediate quantitative measures a voter generates while it makes decision


class Predictor:
	def __init__(self, voter_label, voter_results):
		self.is_model_ready = False

		self.voter_label = voter_label
		self.voter_results = voter_results

	def learn_model(self):
		try:
			self.is_model_ready = True
			return self._learn_model_impl()
		except Exception as detail:
			self.is_model_ready = False
			print("error:", detail)
		return None

	# to be implemented for each child
	def _learn_model_impl(self):
		raise Exception("the function is not implemented by this child")

	def predict(self, candidate1, candidate2):
		if not self.is_model_ready:
			return None

		try:
			return self._predict_impl(candidate1, candidate2)
		except Exception as detail:
			print("error:", detail)
			return None

	def _predict_impl(self, candidate1, candidate2):
		raise Exception("the function is not implemented by this child")
