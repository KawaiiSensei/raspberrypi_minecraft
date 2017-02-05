'''imports'''
from mcpi.minecraft import Minecraft
from mcpi import block
import time

sleep = time.sleep
''' Init '''
mc = Minecraft.create()
air = 0
fire = 45
stone = 1
fence = 85
wood = 17
wool = 35

def ship():
        while True:
                ''' Get the player location '''
                x, y, z = mc.player.getPos()
                ''' Sets the block in a radius of 5 to air '''
                a, b, c = x, y, z
                mc.setBlocks(a-2, b-1, c-2, a+2, b-1, c+2, wood)
                mc.setBlocks(a-2, b, c-2, a+2, b+2, c+2, fence)
                mc.setBlocks(a-1, b, c-1, a+1, b+2, c+1, air)
                mc.setBlocks(a-3, b+3, c-3, a+3, b+7, c+3, wool)
                #sleep(0.1)
                mc.setBlocks(a-4, b-4, c-4, a+4, b+8, c+4, air)
                mc.setBlocks(a-2, b-1, c-2, a+2, b-1, c+2, wood)
                mc.setBlocks(a-2, b, c-2, a+2, b+2, c+2, fence)
                mc.setBlocks(a-1, b, c-1, a+1, b+2, c+1, air)
                mc.setBlocks(a-3, b+3, c-3, a+3, b+7, c+3, wool)
                
                
                
                ''' Simple wait timer to not overload the program'''


               
'''  Work in progress !!!
        Get the program to spawn the ship unless there is only air around it
        This will prevent blocks from being destroyed.   
def tship():
        while True:
                # Get the player location =
                x, y, z = mc.player.getPos()
                #Sets the block in a radius of 5 to air
                a, b, c = x, y, z
                if mc.getBlocks(a-4, b-4, c-4, a+4, b+8, c+4) is not 0:
                        mc.postToChat("Blocks in the way")
                else:
                        
                        mc.setBlocks(a-2, b-1, c-2, a+2, b-1, c+2, wood)
                        mc.setBlocks(a-2, b, c-2, a+2, b+2, c+2, fence)
                        mc.setBlocks(a-1, b, c-1, a+1, b+2, c+1, air)
                        mc.setBlocks(a-3, b+3, c-3, a+3, b+7, c+3, wool)
                        #sleep(0.1)
                        mc.setBlocks(a-4, b-4, c-4, a+4, b+8, c+4, air)
                        mc.setBlocks(a-2, b-1, c-2, a+2, b-1, c+2, wood)
                        mc.setBlocks(a-2, b, c-2, a+2, b+2, c+2, fence)
                        mc.setBlocks(a-1, b, c-1, a+1, b+2, c+1, air)
                        mc.setBlocks(a-3, b+3, c-3, a+3, b+7, c+3, wool)
                        '''
