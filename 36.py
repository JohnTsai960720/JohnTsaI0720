from mcpi.minecraft import Minecraft
mc = Minecraft.create()

from random import choice

mineral = [14,15,16,56,73,73,129]

r = choice(mineral)

myID = mc.getPlayerEntityId("JohnTsai0720")

x,y,z = mc.entity.getTilePos(myID)

mc.setBlock(x,y,z,r)

