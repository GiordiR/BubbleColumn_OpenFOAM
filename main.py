from pyBUMP import *


# CASO BASE
xVars, avgVars = readScalar("bubbleColumnDegass", "surfaces", "alphaMean.air_y_63cm.raw")
plot(1,xVars, avgVars, "surfaces", 10, 63)
#xVars, avgVars = readScalar("bubbleColumnDegass", "surfaces", "alphaMean.air_y_8cm.raw")
#plot(1,xVars, avgVars, "surfaces", 10, 8)



xHold, yHold = readScalar("bubbleColumnDegass", "holdUp", "volFieldValue.dat")
plot(2,xHold, yHold, "holdUp", 10, 8)
