import math
from __future__ import division

class Calculator(object):
	"""
	Desc: Calculator class - a receiver class which takes the input and returs the evaluated value
	"""
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
	"""
	Desc: Command class - an inteface class
	"""
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

class Application(object):
	"""
	Input : Gets the input from user line by line
	Return: Returns the evaluated total value
	Desc: Application class communicates with the user to get the expression and returns the value
	"""
	user = CalculatorInvoker()
	
	input_commands = []

	clear_list = False

	error_flag = False
	
	while True:
		calc = Calculator()
		
		input_value = raw_input('Enter the expression one by one please: ')
		
		if input_value == 'Q':
			break

		if input_value == '=':

			list_alpha_symbols = ['+', '-', 'A', 'C', '*', '/']
			
			if input_commands:
			
				if input_commands[0] not in list_alpha_symbols: 
					add_object = Addition(calc, input_commands[0])
					user.store_and_execute(add_object)
					input_commands.pop(0)
					 
					for value in range(0, len(input_commands), 2):
						if input_commands[value] == '+':
							if value < len(input_commands):
								if isinstance(input_commands[value + 1], int):
									add_object = Addition(calc, input_commands[value + 1])
									user.store_and_execute(add_object)
								else:
									error_flag = True
									break
								
						if input_commands[value] == '-':
							if value < len(input_commands):
								if isinstance(input_commands[value + 1], int):
									sub_object = Subtraction(calc, input_commands[value + 1])
									user.store_and_execute(sub_object)
								else:
									error_flag = True
									break
								
						if input_commands[value] == '*':
							if value < len(input_commands):
								if isinstance(input_commands[value + 1], int):
									mul_object = Multiplication(calc, input_commands[value + 1])
									user.store_and_execute(mul_object)
								else:
									error_flag = True
									break
								
						if input_commands[value] == '/':
							if value < len(input_commands):
								if isinstance(input_commands[value + 1], int):
									div_object = Division(calc, input_commands[value + 1])
									user.store_and_execute(div_object)
								else:
									error_flag = True
									break
						
						if isinstance(input_commands[value], int) or isinstance(input_commands[value], float):
							error_flag = True
							break
					
					if not error_flag:
						print "************************************************"
						if (isinstance(calc.total, int)):
							print "Total Value Evaluated to {0} ".format(calc.total)
						else:		
							print "Total Value Evaluated to {0:.15f} ".format(calc.total)
						print "************************************************"
						input_commands = []
					else:
						error_flag = False
						print "Something went wrong while inputting the values, please Enter The expressions one after the other, Thank you!"
				
				else:
					print "RaiseError: Type The Number First Always!"
					print "Please enter from Scratch!!"
					del input_commands[:]
			
			else:
				print "No commands entered!"

		else:
			if clear_list:
				clear_list = False
			else:	
				
				list_symbols = ['+', '-', '*', '/']
				
				if input_value.lstrip('-').replace('.','').isdigit(): 
					try:
						if input_value.lstrip('-').isdigit():
							value = int(input_value)
							input_commands.append(value)
						else:
							try:
								value = float(input_value)
								input_commands.append(value)
							except:
								pass
					except:
						pass

				elif input_value.isalpha():
					if input_value == 'C':
						input_commands.pop()
						input_commands.pop()
					elif input_value == 'A':
						del input_commands[:]
						clear_list = True
					else:
						print "Only, A - All Clear, Q- Quit & C- Clear the previous, are allowed"
					
				elif len(input_value.split(' ')) == 2:
					split_values = input_value.split(' ')
					if split_values[1] == '1/X' or split_values[1] == '1/x':
						try:
							split_number = float(split_values[0])
							inv_object = Inverse(calc, split_number)
							user.store_and_execute(inv_object)
							input_commands.append(calc.inv_value)
						except:
							print "ValueError: I didn't get the coefficient; Please correct it"
					else:
						print "Do you mean 1/x? If so please type the coefficient<space>1/x"
				
				elif input_value[len(input_value)-1] == "!":
					if input_value[:len(input_value)-1].isdigit():
						fact_object = Factorial(calc, int(input_value[:len(input_value)-1]))
						user.store_and_execute(fact_object)
						input_commands.append(calc.fact_value)
					else:
						print "Factorial only accepts integral values"
				
				
				
				elif input_value in list_symbols:
					input_commands.append(input_value)
				else:
					print "'+', '-', '*', '/' Only These Symbols Are Allowed and Numbers are allowed"
				
				if len(input_commands) > 0:
					if isinstance(input_commands[0], int) or isinstance(input_commands[0], float):
						pass
					else:
						print "Always Enter the First Value as Number"
						del input_commands[:]
						print "Enter the value from scratch!!"