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

class Command(object):
	
	def execute(self):
		raise NotImplementedError()

	def undo(self):
		raise NotImplementedError()

class Addition(Command):
"""
Desc: Addition class invokes the addition method in Calculator to execute
"""
	def __init__(self, calc, value):
		self._calc = calc
		self._value = value
			

	def execute(self):
		self._calc.addition(self._value)

class Subtraction(Command):
"""
Desc: Subtraction class invokes the subtraction method in Calculator to execute
"""
	def __init__(self, calc, value):
		self._value = value
		self._calc = calc
			

	def execute(self):
		self._calc.subtraction(self._value)


class Multiplication(Command):
"""
Desc: Multiplication class invokes the multiplication method in Calculator to execute
"""
	def __init__(self, calc, value):
		self._value = value
		self._calc = calc

	def execute(self):
		self._calc.multiplication(self._value)


class Division(Command):
"""
Desc: Division class invokes the division method in Calculator to execute
"""
	def __init__(self, calc, value):
		self._value = value
		self._calc = calc

	def execute(self):
		self._calc.division(self._value)

class Inverse(Command):
"""
Desc: Inverse class invokes the divide_by_x method in Calculator to execute
"""
	def __init__(self, calc, value):
		self._value = value
		self._calc = calc
			

	def execute(self):
		self._calc.divide_by_x(self._value)

class Factorial(Command):
"""
Desc: Factorial class invokes the factorial method in Calculator to execute
"""
	def __init__(self, calc, value):
		self._value = value
		self._calc = calc
			

	def execute(self):
		self._calc.factorial(self._value)

class CalculatorInvoker(object):
"""
Desc: Invoker class invokes the commands(each expression) to execute
"""
	def __init__(self):
		pass

	def store_and_execute(self, invoker_object):
		invoker_object.execute()