from pyBUMP import *


# CASO BASE
xVars, avgVars = readScalar("bubbleColumnDegass", "surfaces", "alphaMean.air_y_63cm.raw")
plot(1,xVars, avgVars, "surfaces", 10, 63, lastCompare=False)
xVars, avgVars = readScalar("bubbleColumnDegass", "surfaces", "alphaMean.air_y_63cm.raw")
plot(1,xVars, avgVars, "surfaces", 10, 63)



xHold, yHold = readScalar("bubbleColumnDegass", "holdUp", "volFieldValue.dat")
plot(2,xHold, yHold, "holdUp", 10, 8)

xHold, yHold = readScalar("bubbleColumnDegass", "holdUp", "volFieldValue.dat", instantaneous=True)
plot(3,xHold, yHold, "holdUpInstantaneous", 10, 8)
