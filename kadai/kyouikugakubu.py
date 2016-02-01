#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create("cv1.progrape.jp")
pos = mc.player.getPos()

pos.x = -2244
pos.y = 4
pos.z = -667

pos.x += 1931
pos.y += -4
pos.z += 899

for i in range(0, 46):
    for j in range(0, 12): 
       for k in range(0, 30):
            mc.setBlock(pos.x+i-2, pos.y+ j, pos.z+k-2, block.STONE.id)


for i in range(0, 44):
    for j in range(0,10): 
        for k in range(0, 28):
            mc.setBlock(pos.x+i-1, pos.y + j+1, pos.z+k-1, block.AIR.id)

for i in range(2, 42):
    for j in range(0, 4): 
#        for k in range(0, 30):
            mc.setBlock(pos.x+i-2, pos.y+j*3+1 , pos.z-2, block.GLASS.id)

for i in range(0, 10):
    for j in range(0, 12): 
#        for k in range(0, 30):
            mc.setBlock(pos.x+i*4, pos.y+j , pos.z-2, block.STONE.id)

for i in range(0, 11):
    for j in range(0, 11): 
#        for k in range(0, 30):
            mc.setBlock(pos.x+i*4, pos.y+j , pos.z-3, block.COBBLESTONE_WALL.id)

for i in range(0, 46):
#    for j in range(0, 4): 
#        for k in range(0, 30):
            mc.setBlock(pos.x+i-2, pos.y+11 , pos.z-3, block.STONE.id)

for i in range(2, 10):
#    for j in range(0, 4): 
        for k in range(0, 3):
            mc.setBlock(pos.x+i-2, pos.y, pos.z-k-3, block.STONE.id)

for i in range(2, 10):
#    for j in range(4, 5): 
        for k in range(3, 4):
            mc.setBlock(pos.x+i-2, pos.y, pos.z-k-3, block.STAIRS_COBBLESTONE.id)
