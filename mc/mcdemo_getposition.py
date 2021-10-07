#Macarios Hoover
# Minecraft Demo Player Position
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat(pos)
mc.postToChat("Your X position: " + str(pos.x))
mc.postToChat("Your Y position: " + str(pos.y))
mc.postToChat("Your Z position: " + str(pos.z))