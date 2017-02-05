''' Import all modules '''
import buildaship
import nuker
import tp-player

from Tkinter import *
''' Start tkinter project '''

class Start(Frame):
	def __init__(self):
		print("Start entered") # Debug statement

	''' Create a checkbox layout


		[ ] Nuker	(0-100 slider for the radius)
		[ ] Flying Ship
	'''

	def checkbox(self):
		print("Checkbox entered")


	''' Create a button to
		
		Teleport everyone to yourself
	'''
	def teleportations(self):
		print("Entering teleportations")

	''' Create two buttons with one list

		~Player List~	Teleport to selected
						Teleport selected to you
	'''

	''' Create 3 entry boxs

		_X Axis_   _Y Axis_  _Z Axis_   Teleport to
	'''

''' Gui main loop '''
