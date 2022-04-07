from random import sample
import readline
from grpc import stream_stream_rpc_method_handler
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

def readScalar(caseFolder, sampleType, fileName):
    
    #Find sample path
    sampleTypePath = os.path.join(caseFolder, "postProcessing", sampleType)
    samplePath = os.path.join(sampleTypePath, os.listdir(sampleTypePath)[-1], fileName)  
    
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

def findFirstRow(filePath):
    
    with open(filePath) as file:
        i = 0
        lines = file.readlines()
        for line in lines:
            if not line.startswith("#"):
                break
            i += 1

    return i

def cum_mean(arr):
    cum_sum = np.cumsum(arr, axis=0)    
    for i in range(cum_sum.shape[0]):       
        if i == 0:
            continue        
        cum_sum[i] =  cum_sum[i] / (i + 1)
    return cum_sum

def plot(figID, xVars, yVars, sampleType, h):
    
    # INSERIRE DATI SPERIMENTALI A CONFRONTO
    
    fig = plt.figure(figID)
    ax = fig.subplots()
    
    if sampleType=="surfaces":   
        ax.plot(xVars, yVars, label = r"$J_G$")
        ax.set_title('Gas volume fraction distribution at h = '+str(h)+' cm')
        ax.set_xlabel('x (m)')
        ax.set_ylabel('gas volume fraction (-)')
        ax.legend()
    else:
        ax.plot(xVars, yVars, label = r"$J_G$")
        ax.set_title('Global gas holdup')
        ax.set_xlabel('Time (s)')
        ax.set_ylabel('gas holdup (-)')
        ax.legend()

    plt.show()

