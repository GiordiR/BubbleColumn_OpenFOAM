from pyBUMP import *

caso="mesh"

# CONFRONTO MESH
if caso=="mesh":       
    path1="results/run001"
    path2="results/run002"
    path3="results/run003"
    path4="results/run004"

    label1="run 001"
    label2="run 002"
    label3="run 003"
    label4="run 004"

    dt1=0.05

    #plot time-averaged aplha.air superficie 8cm
    xVars1, avgVars1 = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars1, avgVars1, "surfaces", 10, 8, label1 ,lastCompare=False)
    xVars2, avgVars2 = readScalar(path2, "surfaces", "alphaMean.air_y_8cm.raw",nz=8)
    plot(1,xVars2, avgVars2, "surfaces", 10, 8, label2, lastCompare=False)
    xVars3, avgVars3 = readScalar(path3, "surfaces", "alphaMean.air_y_8cm.raw",nz=8)
    plot(1,xVars3, avgVars3, "surfaces", 10, 8, label3)
    #xVars4, avgVars4 = readScalar(path4, "surfaces", "alphaMean.air_y_8cm.raw",nz=8)
    #plot(1,xVars4, avgVars4, "surfaces", 10, 8, label4)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1 ,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_63cm.raw",nz=8)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label2, lastCompare=False)
    xVars3, avgVars3 = readScalar(path3, "surfaces", "alphaMean.air_y_63cm.raw",nz=8)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label3)
    #xVars, avgVars = readScalar(path4, "surfaces", "alphaMean.air_y_63cm.raw",nz=8)
    #plot(2,xVars4, avgVars4, "surfaces", 10, 63, label4)


    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", dt=dt1)
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", dt=dt1)
    plot(3,xHold, yHold, "holdUp", 10, 8, label2,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", dt=dt1)
    plot(3,xHold, yHold, "holdUp", 10, 8, label3)
    #xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", dt=dt1)
    #plot(3,xHold, yHold, "holdUp", 10, 8, label4)

    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label2,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label3)
    #xHold, yHold = readScalar(path4, "holdUp", "volFieldValue.dat", instantaneous=True)
    #plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label4)

elif caso=="time":
    print("ciao")    
