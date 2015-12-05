import json
import time
from scipy import stats
from numpy import arange, array, ones

API_URL = "http://api.citybik.es/dublinbikes.json"

# Now for some forecasting/scheduling parameters
alpha = 0.5
beta = 0.5
maxListSize = 30
sigma = 1.0
forecastHorizon = 15
splitVariance = True
LOG_VERBOSE = True

class BikePredictEngine:

	def __init__(self):

	
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
			return dataList[-1], 0.0
		# Performs the exp. smoothing list. 
		else:
			st1 = dataList[1]
			bt1 = dataList[1]-dataList[0]

			index = 2
			while index < len(dataList):
				xt = dataList[index]
				st2 = st1
				bt2 = bt1
				st1 = (alpha*xt) + ((1-alpha)*(st2+bt1))
				bt1 = (beta*(st1-st2)) + ((1-beta)*bt2)
				index += 1

			print st1,bt1

			return st1
	
