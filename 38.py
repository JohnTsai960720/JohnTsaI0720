from mcpi.minecraft import Minecraft
mc = Minecraft.create()

senderID = mc.getPlayerEntityId("JohnTsai0720")
x,y,z = mc.entity.getTilePos(senderID)
blockType = int(input("請輸入你要的方塊ID"))
mc.setBlock(x,y,z,blockType)