import json

# Now for some forecasting/scheduling parameters
alpha = 0.5
beta = 0.5
maxListSize = 30
sigma = 1.0
forecastHorizon = 15
splitVariance = True
LOG_VERBOSE = True

class PredictionModel:

	def __init__(self):
		self.numPredictions = 0			
	
	def getPrediction(self, sequence):
		""" A Holt-Winters Exponential Smoothing Model with a 
		    trend component. Returns the point forecast and trend as 
		    the output of the function. The forecast itself is the 
		    point forecast + (iterations x trend). 
		"""
		# Needs a list of at least two components.
		if len(sequence) < 1:
			return None, None
		elif len(sequence) < 2:
			return sequence[-1]
		# Performs the exp. smoothing list. 
		else:
			estimate = sequence[1]
			bounds = sequence[1]-sequence[0]

			index = 2
			while index < len(sequence):
				currentValue = sequence[index]
				prevEstimate = estimate
				prevBounds = bounds
				estimate = (alpha*currentValue) + ((1-alpha)*(prevEstimate+bounds))
				bounds = (beta*(estimate-prevEstimate)) + ((1-beta)*prevBounds)
				index += 1

			return estimate
