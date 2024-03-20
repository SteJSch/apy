"""
Contains the import statements for wavepy modules
"""

import unittest
import math

import sys 
import numpy as np
import pdb

sys.path.insert(0,'../')
import apy as apy

class my_lib_test(unittest.TestCase) :
	def setUp(self):
		self.wpy = apy.wm.wave_py()

	def test1(self) :
		self.assertEqual(5,self.wpy.do_things() )

if __name__ == '__main__':
	unittest.main()

