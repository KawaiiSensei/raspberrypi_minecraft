'''imports'''
from mcpi.minecraft import Minecraft

''' Init '''
mc = Minecraft.create()

''' Teleport Functions '''


#In development

def tptocords():
	''' Get current self cords '''
        x, y, z = mc.player.getPos()
        ''' Assign each cord to correct axis '''
        a = input("x axis? Left and Right (MAX: -127, 127)| ")
        b = input("y axis? Height | ")
        c = input("z axis? Forward and Backwards (MAX: -127, 127)| ")

        ''' Print which cords you are teleporting to '''
        print("Teleporting to X:", a, "Y:", b, "Z:", c)

        ''' Set specified cords to current cords '''
        mc.player.setPos(a, b, c)
        mc.postToChat("Teleporting to given location...." )


def tptoplayer():
        print("Teleporting self to player.")
        ''' Get self location '''
        x, y, z = mc.player.getPos()

        ''' Get all possible ids of connectec players '''
        eIds = mc.getPlayerEntityIds()

        ''' Start a for loop to go for as many entities in game '''
        for entityId in eIds:
                print(entityId)

def tphere():
        print("Teleporting" + chosenPlayer + "to you")

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
while True:
        ask = raw_input("Do you want to \n1: Teleport to cords. \n2: Teleport to player \n3: Teleport selected player to your location \n4: Teleport everyone to your location \nq: Quit program")
        ''' IF loop checking for the possible outcomes '''
        if ask == '1':
                ''' if chos:en 1 go into single tp function '''
                tptocords()
                print("")
        elif ask == '2':
                ''' if chosen 2 go into tp all function '''
                tptoplayer()
                print("")
        elif ask == '3':
                ''' if chosen 3 go into tp all function '''
                tphere()#
                print("")
        elif ask == '4':
                ''' if chosen 4 go into tp all function '''
                tpall()
                print("")
        else:
                ''' if non entered print exit message '''
                print("Thank you for using my program")
                break



''' if answer in ['y', 'Y', 'yes', 'Yes', 'YES']:
    print("this will do the calculation") '''
