from pyBUMP import *


# CASO BASE
xVars, avgVars = readScalar("bubbleColumnDegass", "surfaces", "alphaMean.air_y_8cm.raw")
plot(1,xVars, avgVars, "surfaces", 63)


xHold, yHold = readScalar("bubbleColumnDegass", "holdUp", "volFieldValue.dat")
plot(2,xHold, yHold, "holdUp", 8)