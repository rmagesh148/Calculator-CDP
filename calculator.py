import math

class Calculator(object):
	
	def __init__(self):
		self._total = 0
		self._inv_value = 0
		self._fact_value = 0
	
	@property
	def total(self):
		return self._total

	@property
	def inv_value(self):
		return self._inv_value

	@property
	def fact_value(self):
		return self._fact_value

	def multiplication(self, mul_value):
		self._total = self._total * mul_value
		
	def division(self, div_value):
		self._total = self._total / div_value
	
	def addition(self, sum):
		self._total = self._total + sum
	
	def subtraction(self, sub_value):
		self._total = self._total - sub_value
	
	def factorial(self, fact_value):
		self._fact_value = math.factorial(fact_value)
	
	def divide_by_x(self, x_value):
		self._inv_value = 1/x_value

