'''imports'''
from mcpi.minecraft import Minecraft
from mcpi import block

''' Init '''
mc = Minecraft.create()
air = 0
fire = 45

# Allow the user to specify how big the radius

''' Nuker function'''
def nuker():
        size = input("What radius would you like the nuker to be?\n")
        while True:
                ''' Get the player location '''
                x, y, z = mc.player.getPos()
                ''' Sets the block in a radius of 5 to air '''
                a, b, c = x, y, z
                mc.setBlocks(a-size, b-size, c-size, a+size, b+size, c+size, air)
                #mc.setBlocks(a-5, b-5, c-5, a+5, b+5, c+5, air)
                ''' Simple wait timer to not overload the program'''
                #sleep(0.1)

''' Question to begin the program '''
ask = raw_input('Do you want to run the Nuker Function?\n')
''' Start of IF statment'''
if ask == 'yes' or 'y':
        ''' Instruction message '''
        print("To stop press CTRL + C")
        mc.postToChat("nuker Enabled")
        ''' Call function'''
        nuker()

''' ERROR WITH EXITING PROGRAM '''
elif ask not in ("yes"):
        print("Thanks for using my program")
''' if not chosen above simply print an exit command '''



