from pyBUMP import *


# CASO BASE
xVars, avgVars = readScalar("bubbleColumn", "surfaces", "alphaMean.air_y_8cm.raw")

plot(xVars, avgVars)
