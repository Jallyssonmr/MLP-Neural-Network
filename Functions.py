# coding=UTF-8
import math

class Functions(object):
	def Sigmoid(self, x):
		return 1/(1 + math.exp(-x))

	def HyperbolicTangent(self, x):
		return math.tanh(x)

	def SigmoidDerivative(self, fx):
		return fx * (1 - fx)

	def HyperbolicTangentDerivative(self, fx):
		return  1 - fx**2