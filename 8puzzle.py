from algClass import magicBox
import numpy as np

# implementing class algClass for 8puzzle example

# (i, j, initial state matrix, final state matrix)
x = magicBox( 3, 3, [[7,2,4],[5,None,6],[8,3,1]], [[None,1,2],[3,4,5],[6,7,8]])

res = x.chState()

print("Cost: {}".format(res[1]))
