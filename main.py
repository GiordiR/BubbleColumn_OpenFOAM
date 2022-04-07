from pyBUMP import *


# CASO BASE
xVars, avgVars = readScalar("bubbleColumn", "surfaces", "alphaMean.air_y_63cm.raw")
plot(xVars, avgVars, "surfaces", 63)
