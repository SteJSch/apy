"""
First Blood
"""
from apy.apy_incl import *

class wave_py : 

	def __init__(self) :
		"""
		Initiates WAVE class object with std. WAVE parameters
		b_type sets which b-fields are loaded from file: 'y': By,
		'yz' By and Bz, 'xyz' ... . Each B-field from different file
		"""
		self.my_paras = 5

	def do_things(self) : 
		print("My Paras:\n")
		print(self.my_paras)
		return self.my_paras
