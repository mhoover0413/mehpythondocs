# M. Hoover
# Minecraft Code Example

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

minecraftplayerpos = mc.player.getTilePos()

mc.postToChat(minecraftplayerpos)