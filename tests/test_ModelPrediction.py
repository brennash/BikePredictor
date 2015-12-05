import unittest
import math
from bikepredictor.PredictionModel import PredictionModel

class Test(unittest.TestCase):

	def test_Forecast_1(self):
		model = PredictionModel()
		sequence = [1,1,1,1,1,1,1]
		output = model.getPrediction(sequence)
		self.assertEquals(output, 1)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
