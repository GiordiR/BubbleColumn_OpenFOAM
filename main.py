from pyBUMP import *

caso="walllub"

# case list: mesh, time, turbmodel, lift, turbdisp, walllub, j10, j8, j6, allj

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



    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label1 ,colorID=1,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_8cm.raw",nz=8)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label2, colorID=2,lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_8cm.raw",nz=8)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label3, colorID=3,lastCompare=False)
    xVars, avgVars = readScalar(path4, "surfaces", "alphaMean.air_y_8cm.raw",nz=8)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label4,colorID=5,)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1 ,colorID=1,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_63cm.raw",nz=8)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label2, colorID=2,lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_63cm.raw",nz=8)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label3, colorID=3,lastCompare=False)
    xVars, avgVars = readScalar(path4, "surfaces", "alphaMean.air_y_63cm.raw",nz=8)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label4,colorID=5,)


    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,colorID=1,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label2,colorID=2,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label3,colorID=3, lastCompare=False)
    xHold, yHold = readScalar(path4, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label4,colorID=5,)

    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1,colorID=1,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label2,colorID=2,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label3, colorID=3,lastCompare=False)
    xHold, yHold = readScalar(path4, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label4,colorID=5,)

elif caso=="time":
 
    path1="results/run001"
    path2="results/run005"
    path3="results/run006"

    label1="run 001"
    label2="run 005"
    label3="run 006"


    
    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label1 , colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label2,colorID=2,caso=caso, lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label3,colorID=3,caso=caso)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1 ,colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label2, colorID=2,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label3,colorID=3,caso=caso)



    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,colorID=1,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label2, colorID=2,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label3, colorID=3,caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1, colorID=1,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label2, colorID=2,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label3, colorID=3,caso=caso)
    
elif caso=="turbmodel":
 
    path1="results/run001"
    path2="results/run007"
    path3="results/run008"
    
    label1="run 001"
    label2="run 007"
    label3="run 008"


    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label1 , colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label2,colorID=2,caso=caso, lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label3,colorID=3,caso=caso)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1 ,colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label2, colorID=2,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label3,colorID=3,caso=caso)



    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,colorID=1,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label2, colorID=2,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label3, colorID=3,caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1, colorID=1,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label2, colorID=2,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label3, colorID=3,caso=caso)
    
elif caso=="lift":
 
    path1="results/run001"
    path2="results/run009"
    path3="results/run010"
    
    label1="run 001"
    label2="run 009"
    label3="run 010"


    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label1 , colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label2,colorID=2,caso=caso, lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label3,colorID=3,caso=caso)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1 ,colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label2, colorID=2,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label3,colorID=3,caso=caso)



    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,colorID=1,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label2, colorID=2,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label3, colorID=3,caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1, colorID=1,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label2, colorID=2,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label3, colorID=3,caso=caso)
    
elif caso=="turbdisp":
 
    path1="results/run001"
    path2="results/run011"
    path3="results/run012"
    
    label1="run 001"
    label2="run 011"
    label3="run 012"


    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label1 , colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label2,colorID=2,caso=caso, lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label3,colorID=3,caso=caso)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1 ,colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label2, colorID=2,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label3,colorID=3,caso=caso)



    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,colorID=1,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label2, colorID=2,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label3, colorID=3,caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1, colorID=1,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label2, colorID=2,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label3, colorID=3,caso=caso)
    

elif caso=="walllub":
 
    path1="results/run011"
    path2="results/run013"
    path3="results/run014"
    
    label1="run 011"
    label2="run 013"
    label3="run 014"


    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label1 , colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label2,colorID=2,caso=caso, lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label3,colorID=3,caso=caso)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1 ,colorID=1,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label2, colorID=2,caso=caso,lastCompare=False)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label3,colorID=3,caso=caso)



    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,colorID=1,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label2,colorID=2, caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label3,colorID=3, caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1,colorID=1, caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label2,colorID=2, caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label3,colorID=3, caso=caso)
  
  
elif caso=="j10":
 
    path1="results/run013"
    
    label1="run 013"

    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label1,colorID=1,caso=caso)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1,colorID=1,caso=caso)


    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,colorID=1, caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1,colorID=1, caso=caso)
  

elif caso=="j8":
 
    path1="results/run015"
    
    label1="run 015"

    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 8, 8, label1,colorID=2,caso=caso)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 8, 63, label1,colorID=2,caso=caso)


    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 8, 8, label1,colorID=2, caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 8, 8, label1,colorID=2, caso=caso)
  

elif caso=="j6":
 
    path1="results/run016"
    
    label1="run 016"

    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 6, 8, label1,colorID=3,caso=caso)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 6, 63, label1,colorID=3,caso=caso)


    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 6, 8, label1,colorID=3, caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 6, 8, label1,colorID=3, caso=caso)
  
elif caso=="allj":
 
    path1="results/run013"
    path2="results/run015"
    path3="results/run016"
    
    label1="run 013"
    label2="run 015"
    label3="run 016"


    #plot time-averaged aplha.air superficie 8cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 10, 8, label1, colorID=1, caso=caso,lastCompare=False, comparisonJ=True)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 8, 8, label2, colorID=2,caso=caso, lastCompare=False, comparisonJ=True)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_8cm.raw",nz=4)
    plot(1,xVars, avgVars, "surfaces", 6, 8, label3, colorID=3,caso=caso, comparisonJ=True)


    #plot time-averaged aplha.air superficie 63cm
    xVars, avgVars = readScalar(path1, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 10, 63, label1 ,colorID=1,caso=caso,lastCompare=False, comparisonJ=True)
    xVars, avgVars = readScalar(path2, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 8, 63, label2, colorID=2,caso=caso,lastCompare=False, comparisonJ=True)
    xVars, avgVars = readScalar(path3, "surfaces", "alphaMean.air_y_63cm.raw",nz=4)
    plot(2,xVars, avgVars, "surfaces", 6, 63, label3,colorID=3,caso=caso, comparisonJ=True)



    #plot media holdup da 30s
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 10, 8, label1,colorID=1,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 8, 8, label2, colorID=2,caso=caso,lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat")
    plot(3,xHold, yHold, "holdUp", 6, 8, label3, colorID=3,caso=caso)


    #plot holdup istantaneo
    xHold, yHold = readScalar(path1, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 10, 8, label1, colorID=1,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path2, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 8, 8, label2, colorID=2,caso=caso, lastCompare=False)
    xHold, yHold = readScalar(path3, "holdUp", "volFieldValue.dat", instantaneous=True)
    plot(4,xHold, yHold, "holdUpInstantaneous", 6, 8, label3, colorID=3,caso=caso)
  

