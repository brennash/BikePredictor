from django.test import TestCase
from bikepredictor import PredictionModel

class BikePredictorTestCase(TestCase):

#    def setUp(self):

    def test_prediction_1(self):
	model = PredictionModel()
	sequence = [1,1,1,1,1,1,1,1]
	nextValue = model.getPrediction(sequence)
	self.assertEqual(nextValue, 1)

