'''imports'''
from mcpi.minecraft import Minecraft

''' Init '''
mc = Minecraft.create()
air = 0

# Allow the user to specify how big the radius

''' Nuker function'''
def nuker():
	while True:
		''' Get the player location '''
		x, y, z = mc.player.getPos()
		''' Sets the block in a radius of 5 to air '''
		mc.setBlocks(x-5, y-5, z-5, x+5, y+5, z+5, air)
		''' Simple wait timer to not overload the program'''
		#sleep(0.1)

''' Question to begin the program '''
ask = input("Do you want to run the Nuker Function?\n")
''' Start of IF statment'''
if ask == 'yes' or 'y':
	''' Instruction message '''
	print("To stop press CTRL + T")
	''' Call function'''
	nuker()
''' if not chosen above simply print an exit command '''
else:
	print("Thanks for using my nuker :)")



