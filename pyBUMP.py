import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

def readScalar(caseFolder, sampleType, fileName):
    
    #Find sample path
    sampleTypePath = os.path.join(caseFolder, "postProcessing", sampleType)
    samplePath = os.path.join(sampleTypePath, findMaxTimeFolder(sampleTypePath), fileName)  
    
    #Find data firs line
    iRow = findFirstRow(samplePath)
    
    #Read sample file and sort                 
    varDf = pd.read_csv(samplePath, delimiter="\s+", skiprows=iRow, header=None)
    vars = varDf.to_numpy(dtype=float)
    
    if sampleType=="surfaces":
        #Sort data
        vars = vars[np.argsort(vars[:, 0])]
        
        #Mean over equal x values
        yVars = np.average(vars[:,3].reshape(-1, 4), axis=1)
        
        #x values
        xVars = vars[::4, 0]
    elif sampleType=="holdUp":
        xVars = vars[:,0]
        yVars = cum_mean(vars[:,1])
        
    
    return xVars, yVars

def readExpData(fileName):
    
    dataDf = pd.read_excel(fileName, engine='openpyxl', skiprows=4)
    data = {'J6h8': dataDf.to_numpy(dtype=float)[:,:3],
            'J8h8' : dataDf.to_numpy(dtype=float)[:,3:6],
            'J10h8' : dataDf.to_numpy(dtype=float)[:-1,6:9],
            'J6h63' : dataDf.to_numpy(dtype=float)[:,10:13],
            'J8h63' : dataDf.to_numpy(dtype=float)[:,13:16],
            'J10h63' : dataDf.to_numpy(dtype=float)[:,16:19]}
    
    return data

def findExpData(J,h):
    pass

def findFirstRow(filePath):
    
    with open(filePath) as file:
        i = 0
        lines = file.readlines()
        for line in lines:
            if not line.startswith("#"):
                break
            i += 1

    return i

def findMaxTimeFolder(folderPath):
    
    folderList = os.listdir(folderPath)
    folderArray = [int(x) for x in folderList]
       
    return str(max(folderArray))

def cum_mean(arr):
    cum_sum = np.cumsum(arr, axis=0)    
    for i in range(cum_sum.shape[0]):       
        if i == 0:
            continue        
        cum_sum[i] =  cum_sum[i] / (i + 1)
    return cum_sum

def plot(figID, xVars, yVars, sampleType, J, h, lastCompare=True):
    
    # Import experimental data
    expDataDict = readExpData("Krepper_expData.xlsx")
    expData = expDataDict['J'+str(J)+'h'+str(h)]
    
    # Create figure
    fig = plt.figure(figID)
    ax = fig.subplots()
    
    if sampleType=="surfaces":   
        xNorm = xVars/max(xVars)
        ax.plot(xNorm, yVars, label = r"simulation - $J_G$="+str(J))
        ax.plot(expData[:,1], expData[:,2], label=r"experimental - $J_G$="+str(J))
        if lastCompare==True:
            ax.set_title('Gas volume fraction distribution at h = '+str(h)+' cm')
            ax.set_xlabel('x/L (-)')
            ax.set_ylabel('gas volume fraction (-)')
            ax.legend()
            plt.savefig('surfacesJ'+str(J)+'h'+str(h)+'.png')
    else:
        ax.plot(xVars, yVars, label = r"$J_G$")
        if lastCompare==True:
            ax.set_title('Global gas holdup')
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('gas holdup (-)')
            ax.legend()
            plt.savefig('holdup'+str(J)+'.png')

