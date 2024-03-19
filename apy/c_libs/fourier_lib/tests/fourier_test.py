import ctypes
from ctypes import cdll

lib = cdll.LoadLibrary('lib/fourier.so')

class mylib():
	def __init__(self):

		lib.important_class_new.argtypes = []
		lib.important_class_new.restype = ctypes.c_void_p

		lib.important_class_fun.argtypes = [ctypes.c_void_p]
		lib.important_class_fun.restype = ctypes.c_double

		lib.important_class_speak.argtypes = [ctypes.c_void_p]
		lib.important_class_speak.restype = ctypes.c_void_p
				
		self.obj = lib.important_class_new()

	def bar(self):
		val = lib.important_class_fun(self.obj)
		return val
		
	def speak(self) : 
		lib.important_class_speak(self.obj)

mycl = mylib()
mycl.speak()
#val = mycl.bar()
#print(f'val is {val}')
