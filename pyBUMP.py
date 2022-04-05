from random import sample
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

def readScalar(caseFolder, sampleType, fileName):
    
    #Find sample path
    sampleTypePath = os.path.join(caseFolder, "postProcessing", sampleType)
    samplePath = os.path.join(sampleTypePath, os.listdir(sampleTypePath)[-1], fileName)  
    
    #Read sample file and sort                 
    varDf = pd.read_csv(samplePath, delimiter="\s+", skiprows=2, header=None)
    vars = varDf.to_numpy(dtype=float)
    vars = vars[np.argsort(vars[:, 0])]
    
    #Mean over equal x values
    avgVars = np.average(vars[:,3].reshape(-1, 4), axis=1)
    
    #x values
    xVars = vars[::4, 0]
    
    return xVars, avgVars


def plot(xVar, yVar, sampleType, h):
    
    fig = plt.figure()
    ax = fig.subplots()
    
    if sampleType=="surfaces":   
        ax.plot(xVar, yVar, label = r"$J_G$")
        ax.set_title('Gas volume fraction distribution at h = '+str(h)+' cm')
        ax.set_xlabel('x (m)')
        ax.set_ylabel('gas volume fraction (-)')
        ax.legend()
    else:
        ax.plot(xVar, yVar, label = 'test')

    plt.show()

