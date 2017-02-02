'''imports'''
from mcpi.minecraft import Minecraft

''' Init '''
mc = Minecraft.create()

''' Teleport Functions '''

'''
In development

def singletp():
	x, y, z = mc.player.getPos()
'''

def tpall():
	''' Get self location '''
	x, y, z = mc.player.getPos()

	''' Get all possible ids of connectec players '''
	eIds = mc.getPlayerEntityIds()

	''' Start a for loop to go for as many entities in game '''
	for entityId in eIds:
		''' Set each entites location to be the same as yours '''
		mc.player.setPos(entityId, x, y, z)

''' Question to figure out what the user wants to do '''
ask = input("Do you want to 1: Teleport a single person to your location. 2: Teleport everyone to your location\n")
''' IF loop checking for the possible outcomes '''
if ask == 1:
	''' if chosen 1 go into single tp function '''
	singletp()
elif ask == 2:
	''' if chosen 2 go into tp all function '''
	tpall()
else:
	''' if non entered print exit message '''
	print("Thank you for using my program")

