import numpy as np

from predictor.predictor import Predictor


class LinearRegressionPredictor(Predictor):
	EPOCHS_AMOUNT = 1000
	ALPHA = 10**-4

	# fixme: tried for an hour to made it with numpy
	def __split_results_by_rows(self):
		c1, c2, vr = [], [], []
		for result in self.voter_results:
			c1.append(result[0].properties)
			c2.append(result[1].properties)
			vr.append(result[2])

		return c1, c2, np.array(vr, dtype=np.float64)

	# is's expected to be self.vote_results a list of tuples: (cnd1, cnd2, boolean_result)
	def _learn_model_impl(self):
		splitted = self.__split_results_by_rows()
		candidate1, candidate2, actual_vote_result = splitted[0], splitted[1], splitted[2]

		props_norm = self.__normalize(candidate1, candidate2)
		# mb it'll be better to use np.random.random() but I don't see the reason
		coefs = np.ones(props_norm.shape[1])

		mean_sq_error = 0
		for epoch in range(0, self.EPOCHS_AMOUNT):
			cur_result = self.__evaluate_result_function(props_norm, coefs)
			error = cur_result - actual_vote_result
			mean_sq_error = np.sum(error**2) / error.size # closer to 0 - better
			for prop_item in props_norm:
				coefs -= self.ALPHA * 2 * np.sum(error) * prop_item / actual_vote_result.shape[0]
			# if (epoch % 100 == 0):
			# 	print("mse: " + str(mean_sq_error))

		print("mean square error is " + str(mean_sq_error))
		self.coefs = coefs
		print("coefs: " + str(coefs))

	def _predict_impl(self, candidate1, candidate2):
		return np.sum(([1] + candidate1.properties) * self.coefs) - np.sum(([1] +candidate2.properties) * self.coefs) > 0

	def __normalize(self, cnd1, cnd2):
		# assuming the length of both candidates properties is equal
		# [1] is for the first element as the function is y= x0*1 + x1*x1 + ...
		concatinated = []
		for i in range(0, len(cnd1)):
			concatinated.append([1] + cnd1[i]) # even
			concatinated.append([1] + cnd2[i]) # not even
		return np.array(concatinated)/np.linalg.norm(np.array(concatinated))

	# this function implements the assumption that function is linear (y = x0 + x1*c1 + ... + xn*cn)
	# TODO: check if other function types fit better
	def __evaluate_result_function(self, props, coefs):
		predicted_results = []
		# fixme: for loop is made with an assumption that len(props)%2 = 0
		for i in range(0, len(props), 2):
			props1, props2 = props[i], props[i+1]
			predicted_results.append(np.sum(props1 * coefs) - np.sum(props2 * coefs))

		return predicted_results

